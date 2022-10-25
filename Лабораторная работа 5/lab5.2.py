'''
Написать функцию, которая возвращает список, заполненный случайными целыми числами. Числа в списке должны быть уникальными.
Диапазон случайных чисел от -10 до 10 включительно. Размер списка 15 чисел.
'''
import random

def get_unique_list_numbers() -> list[int]:
    list_ = []
    already_exist = set()
    for i in range(15):
        numb = random.randint(-10, 10)
        while numb in already_exist:
            numb = random.randint(-10, 10)
        already_exist.add(numb)
        list_.append(numb)
    return list_



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))