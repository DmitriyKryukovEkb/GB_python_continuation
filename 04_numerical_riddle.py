"""
4. Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
from random import randint

def numerical_riddle(target_number: int, number_of_attempts: int) -> bool:
    for attempt_number in range(1, number_of_attempts + 1):
        user_number = int(input(f"Это твоя {attempt_number} попытка. Введи своё предположение: "))
        if user_number < target_number:
            print("Моё число больше.")
        elif user_number > target_number:
            print("Моё число меньше.")
        else:
            return True
    return False

if __name__ == '__main__':
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    NUMBER_OF_ATTEMPTS = 10

    randint_num = randint(LOWER_LIMIT, UPPER_LIMIT)

    print("Я загадал число от 0 до 1000. Представь, что ты алгоритм бинорного поиска и угадай это число.")
    if numerical_riddle(randint_num, NUMBER_OF_ATTEMPTS):
        print(f"Верно, загаданное число - {randint_num}.")
    else:
        print(f"Не удалось отгадать загаданное число. Было загадано число {randint_num}.")