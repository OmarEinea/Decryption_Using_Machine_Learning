from tools import __chars, __named_lambda


@__named_lambda
def caesar_cipher():
    return lambda string: ''.join([
        __chars[(__chars.index(char) + 3) % len(__chars)]
        for char in string
    ])


@__named_lambda
def vigenere_cipher(key=None):
    if not key: key = __chars
    return lambda string: ''.join([
        __chars[(__chars.index(char) + __chars.index(key[i % len(key)])) % len(__chars)]
        for i, char in enumerate(string)
    ])


@__named_lambda
def shifting_cipher(by=1):
    return lambda string: string[by:] + string[:by]


@__named_lambda
def shifted_vigenere_cipher(by=5):
    return lambda string: shifting_cipher(vigenere_cipher(string), by)


@__named_lambda
def vigenere_shifted_cipher(by=5):
    return lambda string: vigenere_cipher(shifting_cipher(string, by))


@__named_lambda
def transposition_cipher(order):
    def transpose(sub):
        if len(sub) < 8: sub = sub + '\t' * (8 - len(sub))
        return ''.join(sub[-int(index)] for index in order).replace('\t', '')
    check = set(order)
    if len(check) != 8 or max(check) != '8' or min(check) != '1': raise Exception('Wrong Order!')
    return lambda string: ''.join(transpose(string[i:i+8]) for i in range(0, len(string), 8))
