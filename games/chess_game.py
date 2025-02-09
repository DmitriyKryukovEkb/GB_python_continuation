import random
from typing import Tuple, List


BOARD_SIZE = 8
QUEENS_COUNTY = 8
SUCCESS_POSITIONS_COUNTY = 4


def chess_check(coordinates: List[Tuple[int, int]]) -> bool:
    for i in range(BOARD_SIZE):
        for j in range(i +1, BOARD_SIZE):
            if coordinates[i][0] == coordinates[j][0] or coordinates[i][1] == coordinates[j][1]:
                return False
            if abs(coordinates[i][0] - coordinates[j][0]) == abs(coordinates[i][1] - coordinates[j][1]):
                return False
    return True


def random_feet() ->  List[Tuple[int, int]]:
    result = []
    while len(result) < QUEENS_COUNTY:
        temp = random.randint(1, BOARD_SIZE), random.randint(1, BOARD_SIZE)
        if temp not in result:
            result.append(temp)
    return result


def success_positions(positions_county: int) -> List[List[Tuple[int, int]]]:
    result = []
    while len(result) < positions_county:
        temp = random_feet()
        if chess_check(temp):
            result.append(temp)
    return result


def print_solution(coordinates: List[Tuple[int, int]]) -> str:
    return f"{"Успешная расстановка: " if chess_check(coordinates) else "Неудачная расстановка: "}{coordinates}"


if __name__ == '__main__':
    print("Тестовые расстановки: ")
    print(print_solution([(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]))
    print(print_solution([(1, 3), (2, 8), (3, 4), (4, 7), (5, 1), (6, 6), (7, 2), (8, 5)]))
    print(print_solution([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]))
    print(f"\nНайдём {SUCCESS_POSITIONS_COUNTY} случайные успешные расстановки: ")
    for i, position in enumerate(success_positions(SUCCESS_POSITIONS_COUNTY), start=1):
        print(f"{i}: {print_solution(position)}")
