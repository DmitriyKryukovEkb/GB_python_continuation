"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""
import fractions
from typing import Tuple

def fraction_input(input_message: str) -> Tuple[int, int]:
    """
    Пользовательский ввод дроби с разделителем.
    :param input_message: сообщение для пользователя при вводе.
    :return: кортеж с числителем и знаменателем.
    """
    user_input = input(input_message)
    numerator, denominator = user_input.split(sep='/')
    return (int(numerator), int(denominator))

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Найти наибольше общее частное двух чисел.
    :param a: первое число.
    :param b: второе число.
    :return: наибольший делитель.
    """
    bigger, smaller = (a, b) if a > b else (b, a)
    for i in range(smaller, 0, -1):
        if bigger % i == 0 and smaller % i == 0:
            return i

def fraction_sum(first: Tuple[int, int], second: Tuple[int, int]) -> Tuple[int, int]:
    """
    Сложить две дроби
    :param first: кортеж из числителя и знаменателя первой дроби.
    :param second: кортеж из числителя и знаменателя второй дроби.
    :return: кортеж из числителя и знаменателя результирующей дроби.
    """
    first_numerator, first_denominator = first
    second_numerator, second_denominator = second
    result_numerator = first_numerator * second_denominator + second_numerator * first_denominator
    result_denominator = first_denominator * second_denominator
    common_divisor = greatest_common_divisor(result_numerator, result_denominator)
    return (int(result_numerator / common_divisor), int(result_denominator / common_divisor))

def fraction_multiplication(first: Tuple[int, int], second: Tuple[int, int]) -> Tuple[int, int]:
    """
    Умножить две дроби
    :param first: кортеж из числителя и знаменателя первой дроби.
    :param second: кортеж из числителя и знаменателя второй дроби.
    :return: кортеж из числителя и знаменателя результирующей дроби.
    """
    first_numerator, first_denominator = first
    second_numerator, second_denominator = second
    result_numerator = first_numerator * second_numerator
    result_denominator = first_denominator * second_denominator
    common_divisor = greatest_common_divisor(result_numerator, result_denominator)
    return (int(result_numerator / common_divisor), int(result_denominator / common_divisor))

def fraction_string(numerator: int, denominator: int) -> str:
    """
    Вернуть строку с записью дроби в виде "a/b".
    :param numerator: чисдитель.
    :param denominator: знаменатель.
    :return: строка с дробью
    """
    return str(numerator) + "/" + str(denominator)



if __name__ == '__main__':
    a = fraction_input('Введите первую дробь в виде "a/b": ')
    b = fraction_input('Введите вторую дробь в виде "a/b": ')
    print(f"{fraction_string(*a)} + {fraction_string(*b)} = {fraction_string(*fraction_sum(a, b))}")
    print(f"{fraction_string(*a)} * {fraction_string(*b)} = {fraction_string(*fraction_multiplication(a, b))}")
    print("\nПроверка результата с помощью модуля fractions:")
    m = fractions.Fraction(*a)
    n = fractions.Fraction(*b)
    print(f"Сумма равна {m + n}")
    print(f"Произведение равно {m * n}")

