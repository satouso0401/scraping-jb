
import requests
from bs4 import BeautifulSoup
import json

def get_login_page():
    res = requests.get("https://jbungakukan.shogakukan.co.jp/login")
    print(res.status_code)
    print(res.text)
    print(res.cookies.get_dict())

    soup = BeautifulSoup(res.content, 'html.parser')
    elem = soup.find("input", attrs={"name": "_token"})
    print(elem["value"])


def login():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data={
        "_token": "****",
        "email": "****",
        "password": "****"
    }

    res = requests.post("https://jbungakukan.shogakukan.co.jp/login", headers=headers, data=data)

    print(res.status_code)
    print(res.text)
    print(res.cookies.get_dict())

def test():
    res = requests.get("https://jbungakukan.shogakukan.co.jp/login")
    soup = BeautifulSoup(res.content, 'html.parser')
    elem = soup.find("input", attrs={"name": "_token"})
    print(elem["value"])

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "Origin": "https://jbungakukan.shogakukan.co.jp",
        "Referer": "https://jbungakukan.shogakukan.co.jp/login",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    data = {
        "_token": elem["value"],
        "email":  "****",
        "password":  "****"
    }

    res = requests.post("https://jbungakukan.shogakukan.co.jp/login", cookies=res.cookies.get_dict(), headers=headers, data=data, allow_redirects=False)

    print(res.status_code)
    print(res.text)
    print(res.cookies.get_dict())


    url = "https://jbungakukan.shogakukan.co.jp/bibi/?book=110"

    res = requests.get(url, cookies=res.cookies.get_dict())
    print(res.status_code)
    print(res.text)
    print(res.cookies.get_dict())


def _get_auth_cookie():
    res = requests.get("https://jbungakukan.shogakukan.co.jp/login")
    soup = BeautifulSoup(res.content, 'html.parser')
    elem = soup.find("input", attrs={"name": "_token"})
    print(elem["value"])

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        "Origin": "https://jbungakukan.shogakukan.co.jp",
        "Referer": "https://jbungakukan.shogakukan.co.jp/login",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    data = {
        "_token": elem["value"],
        "email":  email,
        "password":  password
    }

    return res.cookies.get_dict()

def get_auth_cookie():
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
        "email":  email,
        "password":  password
    }

    res = requests.post("https://jbungakukan.shogakukan.co.jp/login", cookies=res.cookies.get_dict(), headers=headers, data=data, allow_redirects=False)

    # cookieの保存
    with open("auth_cookies.json", mode="wt", encoding="utf-8") as f:
        json.dump(res.cookies.get_dict(), f, indent=2)

    return res.cookies.get_dict()


def main():
    # cookie = get_auth_cookie()

    auth_cookie = get_auth_cookie()
    # url = "https://jbungakukan.shogakukan.co.jp/bibi/?book=110"
    #
    # res = requests.get(url, cookies=auth_cookie)
    # print(res.status_code)
    # print(res.text)

    # password_json = json.load(open("auth.json", "r"))
    # email = password_json["email"]
    # password = password_json["password"]
    #
    # cookie_json = json.load(open("auth_cookies.json", "r"))







if __name__ == "__main__":
    # test()
    main()
    # get_login_page()
    # login()
    # main()

