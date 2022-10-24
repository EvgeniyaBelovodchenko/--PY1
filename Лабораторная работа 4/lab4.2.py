'''
Реализовать функцию delete, принимающую список и индекс, по которому надо удалить элемент.
По умолчанию удается последний элемент из списка.
Результатом вернуть измененный список.
'''
def delete(list_, index=None):
    if index is None:
        new_list = list_[:-1]
        return new_list
    else:
        left_part = list_[:index]
        right_part = list_[index + 1:]
        new_list = left_part + right_part
        return new_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
