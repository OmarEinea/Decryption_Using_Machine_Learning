from tools import __chars
from math import ceil


def caesar_cipher(string):
    return ''.join([
        __chars.list[(__chars.list.index(char) + 3) % __chars.length]
        for char in string
    ])


def vigenere_cipher(string, key=None):
    if key: key = key*ceil(len(string)/len(key))
    else: key = (__chars.list*ceil(len(string)/len(__chars.list)))[1:]
    return ''.join([
        __chars.list[(__chars.list.index(char) + __chars.list.index(key[i])) % __chars.length]
        for i, char in enumerate(string)
    ])


def shifting_cipher(string, by=1):
    at = by % len(string)
    return string[at:] + string[:at]


def shifted_vigenere_cipher(string, by=5):
    return shifting_cipher(vigenere_cipher(string), by)


def vigenere_shifted_cipher(string, by=5):
    return vigenere_cipher(shifting_cipher(string, by))
