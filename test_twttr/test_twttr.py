from twttr import shorten

def test_shorten():
    assert shorten("AaAaHhHhAaAa")=="HhHh"
    assert shorten("CS50-12314*&^%$#@!")=="CS50-12314*&^%$#@!"
    assert shorten("aeiouAEIOU1")=="1"
