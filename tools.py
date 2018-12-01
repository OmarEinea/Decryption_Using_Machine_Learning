from keras.preprocessing.text import Tokenizer as __Tokenizer
import numpy as __numpy, string as __string
from random import choices as __choices
from functools import wraps as __wraps


__tokenizer = __Tokenizer(char_level=True, lower=False)
__tokenizer.fit_on_texts(__string.printable[:-2])
__chars = list(__string.ascii_letters)


def set_characters(chars):
    __chars.clear()
    __chars.extend(chars)


def generate_text(length, limit=10000):
    text = set()
    for _ in range(int(limit*1.2)):
        text.add(''.join(__choices(__chars, k=length)))
        if len(text) == limit: break
    return list(text)


def to_vec(text, reshape=True):
    if isinstance(text, str): text = [text]
    vector = __numpy.array(__tokenizer.texts_to_sequences(list(text)))
    return vector.reshape(*vector.shape, 1) if reshape else vector


def to_txt(vector):
    return __tokenizer.sequences_to_texts([map(round, vector.reshape(-1).tolist())])[0].replace(' ', '')


def __named_lambda(wrapper):
    @__wraps(wrapper)
    def named_lambda(*args):
        method = wrapper(*args)
        method.name = wrapper.__name__
        return method
    return named_lambda
