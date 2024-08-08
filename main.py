import requests
from bs4 import BeautifulSoup
import json
import dataclasses
import re
import os
import lxml

def get_auth_cookie() -> dict:
    # 保存済みのcookieが使えるかテスト
    cookies = json.load(open("auth_cookies.json", "r", encoding="utf-8"))
    res = requests.get("https://jbungakukan.shogakukan.co.jp/", cookies=cookies)
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find("title")

    if "本棚" in title.get_text():
        print("保存済みのcookieが有効なので再利用する")
        return cookies

    print("認証切れなので認証用のcookieを取得する")
    password_json = json.load(open("auth.json", "r"))
    email = password_json["email"]
    password = password_json["password"]

    res = requests.get("https://jbungakukan.shogakukan.co.jp/login")
    soup = BeautifulSoup(res.content, 'html.parser')
    elem = soup.find("input", attrs={"name": "_token"})

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "Origin": "https://jbungakukan.shogakukan.co.jp",
        "Referer": "https://jbungakukan.shogakukan.co.jp/login",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    data = {
        "_token": elem["value"],
        "email": email,
        "password": password
    }

    res = requests.post("https://jbungakukan.shogakukan.co.jp/login", cookies=res.cookies.get_dict(), headers=headers,
                        data=data, allow_redirects=False)

    # cookieの保存
    with open("auth_cookies.json", mode="wt", encoding="utf-8") as f:
        json.dump(res.cookies.get_dict(), f, indent=2)

    return res.cookies.get_dict()


@dataclasses.dataclass
class BookLink:
    title: str
    book_id: str


def get_book_links(auth_cookie: dict) -> list[BookLink]:
    url = "https://jbungakukan.shogakukan.co.jp/"
    res = requests.get(url, cookies=auth_cookie)

    soup = BeautifulSoup(res.content, 'html.parser')
    titles = soup.select('div.bookshelf-all-detail p.bookshelf-all-detail-title a')

    links = []
    for title in titles:
        book_id = re.findall("/bibi/\\?book=(.*)", title["href"])[0]
        links.append(BookLink(title.get_text(), book_id))

    for link in links:
        print(link)

    return links


def download_book(auth_cookie: dict, book_id: str) -> None:
    local_base = "download/" + book_id

    if not os.path.exists(local_base):
        os.makedirs(local_base)

    # 書籍のbase urlを取得する
    res = requests.get(base_url + "/bibi/?book=" + book_id, cookies=auth_cookie)
    soup = BeautifulSoup(res.content, 'html.parser')
    bookshelf = soup.select_one('body')["data-bibi-bookshelf"]

    download_base_url = base_url + bookshelf + "/" + book_id

    # container.xmlの取得
    local_file = download_file(auth_cookie, download_base_url, "/META-INF/container.xml", local_base)
    soup = BeautifulSoup(open(local_file, encoding="utf-8"), 'lxml-xml')
    root_file = soup.find("rootfile")["full-path"]

    # root_file(opf file)のダウンロード
    local_file = download_file(auth_cookie, download_base_url, "/" + root_file, local_base)
    soup = BeautifulSoup(open(local_file, encoding="utf-8"), 'lxml-xml')
    items = soup.find_all("item")
    item_path = []
    for item in items:
        item_path.append("/item/" + item["href"])

    # itemのダウンロード
    for item in item_path:
        download_file(auth_cookie, download_base_url, item, local_base)



def download_file(auth_cookie: dict, download_base_url: str, download_path: str, local_base) -> str:
    # 保存先のフォルダの作成
    save_path = local_base + download_path
    save_directory = os.path.dirname(save_path)
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # ダウンロード
    print("download: " + download_path)
    res = requests.get(download_base_url + download_path, cookies=auth_cookie, stream=True)

    # if download_path.endswith("xhtml"):
    #     with open(save_path, 'w', encoding="utf-8") as f:
    #         f.write(res.text)
    #         f.flush()
    # else:
    with open(save_path,  'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()

    return save_path



base_url = "https://jbungakukan.shogakukan.co.jp"


def main():
    auth_cookie = get_auth_cookie()
    # get_book_links(auth_cookie)

    download_book(auth_cookie, "001")


if __name__ == "__main__":
    # test()
    main()
    # get_login_page()
    # login()
    # main()
