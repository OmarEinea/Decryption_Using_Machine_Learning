from tools import __chars, __named


@__named
def caesar_cipher():
    return lambda string: ''.join([
        __chars[(__chars.index(char) + 3) % len(__chars)]
        for char in string
    ])


@__named
def vigenere_cipher(key=None):
    if not key: key = __chars
    return lambda string: ''.join([
        __chars[(__chars.index(char) + __chars.index(key[i % len(key)])) % len(__chars)]
        for i, char in enumerate(string)
    ])


@__named
def shifting_cipher(by=1):
    return lambda string: string[by:] + string[:by]


@__named
def shifted_vigenere_cipher(by=5):
    return lambda string: shifting_cipher(vigenere_cipher(string), by)


@__named
def vigenere_shifted_cipher(by=5):
    return lambda string: vigenere_cipher(shifting_cipher(string, by))

