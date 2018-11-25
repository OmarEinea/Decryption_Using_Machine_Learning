from keras.preprocessing.text import Tokenizer
import string, random, numpy


class __Characters:
    def __init__(self, chars=string.ascii_letters):
        self.set_chars(chars)

    def set_chars(self, chars):
        self.length = len(chars)
        self.list = chars


__tokenizer = Tokenizer(char_level=True, lower=False)
__tokenizer.fit_on_texts(string.printable[:-2])
__chars = __Characters()


def set_characters(chars):
    __chars.set_chars(chars)


def generate_text(length, limit=10000):
    text = set()
    for _ in range(int(limit*1.2)):
        text.add(''.join(random.sample(__chars.list, length)))
        if len(text) == limit: break
    return list(text)


def to_vec(text, reshape=True):
    if isinstance(text, str): text = [text]
    tokenized = numpy.array(__tokenizer.texts_to_sequences(list(text)))
    return tokenized.reshape(*tokenized.shape, 1) if reshape else tokenized


def to_txt(vector):
    vector = vector.reshape(vector.shape[1]).tolist()
    return __tokenizer.sequences_to_texts([map(round, vector)])[0].replace(' ', '')
