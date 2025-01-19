"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

Напишите программу банкомат.
Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти.
Суммы пополнения и снятия кратны 50 у.е.
Процент за снятие - 1,5% от суммы, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнния или снятия начисляются проценты
Нельзя снять больше, чем на счете
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
Любое действие выводит сумму денег
"""

from typing import Tuple
from datetime import datetime

RICHNESS_THRESHOLD = 5 * 10 ** 6
MAIN_MENU = {1: 'Пополнить', 2: 'Снять', 3: "Показать историю операций", 4: 'Завершить обслуживание'}

def print_balance(balance_sum: float) -> None:
    print(f"Текущий баланс {balance_sum:.2f} у.е.")

def richness_tax(balance: float, operations: list) -> float:
    if balance > RICHNESS_THRESHOLD:
        print("Вычтен налог на богатство.")
        tax = current_balance * 0.1
        operations.append(f"{datetime.now()} Налог на богатство: {tax:.2f} у.е. Баланс: {balance - tax:.2f}")
        return balance - tax
    return balance


def change_balance(
        start_balance: float, change_sum: float, counter: int, percent: float, operations: list
) -> Tuple[float, int]:
    change_sum = round(change_sum, 2)
    operation_type = "Пополнение" if change_sum > 0 else "Снятие"
    counter += 1
    result = start_balance + change_sum
    operations.append(f"{datetime.now()} {operation_type}: {change_sum:.2f} у.е. Баланс: {result:.2f}")
    if counter % 3 == 0:
        percents_sum = result * percent
        result += percents_sum
        print(f"Начислены проценты ({percents_sum} у.е.)")
        operations.append(f"{datetime.now()} Начислены проценты: {percents_sum:.2f} у.е. Баланс: {result:.2f}")
    return result, counter

def menu_function(menu_variants: dict) -> int:
    while True:
        print("\nГлавное меню")
        for key, value in menu_variants.items():
            print(f"{key}: {value}")
        user_input = int(input("Выберите интересующий вас пункт: "))
        if user_input in menu_variants.keys():
            return user_input
        print("Недопустимый выбор. Выберите пожалуйста один из возможных вариантов.")

def sum_check(sum: str) -> bool:
    try:
        return True if int(sum) % 50 == 0 else False
    except ValueError:
        print("Ошибка при вводе.")


def replenish(balance: float, counter: int, percent: float, operations: list) -> Tuple[float, int]:
    balance = richness_tax(balance, operations)
    replenish_sum = input("Введите сумму для пополнения счета: ")
    if sum_check(replenish_sum):
        return change_balance(
            start_balance=balance,
            change_sum=int(replenish_sum),
            counter=counter,
            percent=percent,
            operations=operations
        )
    else:
        print("Недопустимая сумма.")
        return balance, counter

def get_cash(balance: float, counter: int, percent: float, operations: list) -> Tuple[float, int]:
    balance = richness_tax(balance, operations)
    cash_sum = input("Введите сумму для снятия средств: ")
    if sum_check(cash_sum):
        if int(cash_sum) <= balance:
            if int(cash_sum) * 1.5 / 100 <= 30:
                commission = 30
            elif int(cash_sum) * 1.5 / 100 > 600:
                commission = 600
            else:
                commission = int(cash_sum) * 1.5 / 100
            print(f"Комиссия за операцию {commission} у.е.")
            return change_balance(
                start_balance=balance,
                change_sum= -1 * (int(cash_sum) + commission),
                counter=counter,
                percent=percent,
                operations=operations
            )
        else: print("Недостаточно средств.")
        return balance, counter
    else:
        print("Недопустимая сумма.")
        return balance, counter

def print_operations(operations: list) -> None:
    print(*operations, sep="\n")


def exit_menu(balance: float) -> None:
    print("Спасибо за использование наших услуг. \nДо скорых встреч!")
    quit()

if __name__ == '__main__':
    current_balance = 0
    operations_history = []
    operations_counter = 0
    percent = 5.5 / 100

    while True:
        print_balance(current_balance)
        user_choice = menu_function(MAIN_MENU)
        match user_choice:
            case 1:
                current_balance, operations_counter = replenish(
                    balance=current_balance, counter=operations_counter, percent=percent, operations=operations_history
                )
            case 2:
                current_balance, operations_counter = get_cash(
                    balance=current_balance, counter=operations_counter, percent=percent, operations=operations_history
                )
            case 3:
                print_operations(operations_history)
            case 4:
                exit_menu(current_balance)
