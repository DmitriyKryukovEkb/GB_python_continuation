"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

def entering_number() -> int:
    """
    Запрос целого положительного числа до 100 тыс у пользователя.
    :return: int
    """
    a = -1
    while True:
        if 0 < a < 100000:
            break
        a = int(input("Введите целое число от 0 до 100000: "))
    return a

def is_simple(number: int) -> bool:
    """
    Проверка, является ли переданное число простым.
    :param number: число для проверки
    :return: bool
    """
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    user_number = entering_number()
    if is_simple(user_number):
        print('Это простое число.')
    else:
        print('Это составное число.')
