"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

def int_to_hex(number: int) -> str:
    """
    Перевести число в шестнадцатиричную систему
    :param number: число для перевода.
    :return: строка с  записью полученного числа в шестнадцитиричной системе.
    """
    HEX_SYMBOLS = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
        13: 'd', 14: 'e', 15: 'f'
    }
    BASE = 16
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
    if 0 <= number < BASE:
        return str(
            HEX_SYMBOLS[number]
        )
    return sign + int_to_hex(number // BASE) + int_to_hex(number % BASE)

if __name__ == '__main__':
    user_number = int(input("Введите число: "))
    print(f"Число в шестнадцатиричном виде: {int_to_hex(user_number)}")
    print(f"Проверка вcтроенной функцией hex: {hex(user_number)}")
