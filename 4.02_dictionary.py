"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""
from typing import Hashable, Any

def keys_from_values(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[hashable_value(value)] = key
    return result

def hashable_value(value: Any) -> Hashable:
    return value if isinstance(value, Hashable) else str(value)

if __name__ == '__main__':
    example = {'list_name': [1, 2, 3], 'dict_name': {'one': 1, 'two': 2}}
    print(example)
    print(keys_from_values(**example))