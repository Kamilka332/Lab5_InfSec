import re
import pickle
from rc5 import RC5


def get_byte_key(key_str):
    with open('key.dat', 'wb') as file:
        pickle.dump(key_str, file)
    with open('key.dat', 'rb') as file:
        return file.read()


def get_text_entered_from_keyboard(text):
    pattern = r'[А-я,.:;? ]+'
    received_text = input(text)
    while re.fullmatch(pattern, received_text) is None:
        received_text = input('Введенная строка некоректна, повторите ввод: ')
    return received_text


if __name__ == '__main__':
    phrase = get_text_entered_from_keyboard('Введите фразу с клавиатуры: ')
    with open('input_file.txt', 'w') as file:
        file.write(phrase)

    key = get_text_entered_from_keyboard('Введите ключ с клавиатуры: ')

    byte_key = get_byte_key(key)

    rc5 = RC5(32, 16, byte_key)
    rc5.encryptFile('input_file.txt', 'output_file.dat')
    with open('output_file.dat', 'rb') as file:
        encrypted_phrase = file.read()
    print(f'Зашифрованная фраза: {encrypted_phrase}')

    while True:
        key = get_text_entered_from_keyboard('Введите ключ с клавиатуры: ')
        print(f'Введенный ключ: {key}')
        byte_key = get_byte_key(key)
        rc5 = RC5(32, 16, byte_key)
        rc5.decryptFile('output_file.dat', 'input_file.dat')
        with open('input_file.dat', 'r') as file:
            decrypted_phrase = file.read()
        print(f'Расшифрованная фраза: {decrypted_phrase}')
