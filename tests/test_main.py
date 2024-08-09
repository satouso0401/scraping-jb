from src import main


def test_decrypt():
    assert main.decrypt("/bibi-bookshelf-6968781cfb976892be1a676e928da9df3e92ae9295de47dca9", "94f885c659", "<title>U+10a2019;U+0f4fa01;U+0399068;U+0aba216;U+02eac44;U+10e0ca9;U+03232d8;</title>") == "<title>アーサー王物語</title>"
