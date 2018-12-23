# Decryption using Machine Learning

An attempt to decrypt a collection of encryption methods using Machine Learning.
This project uses Keras on top of TensorFlow to build a Neural Networks model that could predict the original text given a cipher text.


### Results

Tests done on 62 letters (0-9a-zA-Z) with string length of 10 letters.

##### Classical encryption
| Method Name      | Implementation  | Accuracy |
| ---------------- | --------------- | -------: |
| Caesar Cipher    | char + 3        | 100%     |
| Vigenère Cipher  | char + shift++  | 100%     |
| Shifting Cipher  | rotates string  | 100%     |
| Transposition    | reorder by map  | 100%     |
| Shifted Vigenère | rotated shift++ | 97.5%    |
| Keyed Vigenère   | char + key      | 97.1%    |

##### Modern encryption

| Method Name      | Accuracy |
| ---------------- | -------: |
| Fernet Cipher    | 10.1%    |
| DES Cipher       | 8.3%     |
| AES Cipher       | 8.1%     |

These results include predicted padding and encoding characters.


### Files

- [research_paper.pdf](./research_paper.pdf): unpublished, research-like paper I wrote about this project.
- [text_from_cipher.ipynb](./text_from_cipher.ipynb): main notebook that trains a model to get text from cipher.
- [key_from_ciphers.ipynb](./key_from_ciphers.ipynb): Jupyter notebook which trains a model to get key from ciphers.
- [tools.py](./tools.py): contains project tool methods like data generator and text to vectors.
- [encrypt.py](./encrypt.py): list of all encryption functions used in the project (classical & modern).
- [models/](./models/): a folder that contains all the trained models on different encryption functions.


### References

- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)
