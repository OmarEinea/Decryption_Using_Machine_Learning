from tools import __chars

def caesar_cipher(string):
    return ''.join([
        __chars.list[(__chars.list.index(char) + 3) % __chars.length]
        for char in string
    ])

def vigenere_cipher(string):
    return ''.join([
        __chars.list[(__chars.list.index(char) + shift) % __chars.length]
        for shift, char in enumerate(string, 1)
    ])

def shifting_cipher(string, by=1):
    at = by % len(string)
    return string[at:] + string[:at]
