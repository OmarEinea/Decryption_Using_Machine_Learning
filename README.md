# Decryption using Machine Learning

An attempt to decrypt a collection of encryption methods using Machine Learning.
This project uses Keras on top of TensorFlow to build a Neural Networks model that could predict the original text given a cipher text.


### Results

| Method Name      | Implementation  | Accuracy |
| ---------------- | --------------- | -------: |
| Caesar Cipher    | char + 3        | 100%     |
| Vigenère Cipher  | char + shift++  | 100%     |
| Shifting Cipher  | rotates string  | 100%     |
| Shifted Vigenère | rotated shift++ | 97.5%    |

Tests done on 62 letters (0-9a-zA-Z) with string length of 10 letters.


### Files

- model.ipynb: Jupyter notebook which generates data, trains model and predicts.
- tools.py: contains project tool methods like data generator and text to vectors.
- encrypt.py: encryption functions using in the project.


### References

- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)
