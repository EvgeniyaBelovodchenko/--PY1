'''
Написать функцию для генерации случайных паролей заданной длины n (по умолчанию 8 символов). В качестве алфавита следует использовать:
Буквы верхнего регистра: A - Z
Буквы нижнего регистра: a - z
Цифры: 0 - 9
Для того чтобы сгенерировать случайную выборку, следует использовать функцию sample из модуля random.
'''

import random
import string

def get_random_password() -> str:
    str_password = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.sample(str_password, 8)
    final_password = ''.join(password)
    return final_password


print(get_random_password())
