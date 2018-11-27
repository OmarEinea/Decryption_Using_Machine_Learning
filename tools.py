from keras.preprocessing.text import Tokenizer as __Tokenizer
import random as __random, numpy as __numpy, string as __string


__tokenizer = __Tokenizer(char_level=True, lower=False)
__tokenizer.fit_on_texts(__string.printable[:-2])
__chars = list(__string.ascii_letters)


def set_characters(chars):
    __chars.clear()
    __chars.extend(chars)


def generate_text(length, limit=10000):
    text = set()
    for _ in range(int(limit*1.2)):
        text.add(''.join(__random.sample(__chars, length)))
        if len(text) == limit: break
    return list(text)


def to_vec(text, reshape=True):
    if isinstance(text, str): text = [text]
    tokenized = __numpy.array(__tokenizer.texts_to_sequences(list(text)))
    return tokenized.reshape(*tokenized.shape, 1) if reshape else tokenized


def to_txt(vector):
    vector = vector.reshape(vector.shape[1]).tolist()
    return __tokenizer.sequences_to_texts([map(round, vector)])[0].replace(' ', '')
