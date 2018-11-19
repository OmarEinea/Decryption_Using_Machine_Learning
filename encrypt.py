from tools import __chars

def caesar_cipher(string):
    return ''.join([
        chr(__chars.range_start + (ord(char) + 3 - __chars.range_start) % __chars.range_length)
        for char in string
    ])

def vigenere_cipher(string):
    return ''.join([
        chr(__chars.range_start + (ord(char) + shift + 1 - __chars.range_start) % __chars.range_length)
        for shift, char in enumerate(string)
    ])

def shifting_cipher(string, by=1):
    at = by % len(string)
    return string[at:] + string[:at]
