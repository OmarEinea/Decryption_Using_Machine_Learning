from keras.preprocessing.text import Tokenizer
from itertools import product
import string, random, numpy

class __Characters:
    range_start = 0
    range_length = 10**10
    list = string.ascii_letters

__tokenizer = Tokenizer(char_level=True, lower=False)
__tokenizer.fit_on_texts(string.printable[:-2])
__chars = __Characters()


def set_characters(chars):
    __chars.list = chars
    __chars.range_start = ord(chars[0])
    __chars.range_length = len(chars)

def generate_text(length, limit=float('inf')):
    products = list(product(__chars.list, repeat=length))
    return list(map(''.join, random.sample(products, min(limit, len(products)))))

def to_vec(text):
    if isinstance(text, str): text = [text]
    tokenized = numpy.array(__tokenizer.texts_to_sequences(list(text)))
    return tokenized.reshape(*tokenized.shape, 1)

def to_txt(vector):
    vector = vector.reshape(vector.shape[1]).tolist()
    return __tokenizer.sequences_to_texts([map(round, vector)])[0].replace(' ', '')

def caesar_cipher(string):
    return ''.join([
        chr(__chars.range_start + (ord(char) + 3 - __chars.range_start) % __chars.range_length)
        for char in string
    ])
