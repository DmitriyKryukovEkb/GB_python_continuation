"""
Напишите функцию для транспонирования матрицы.
"""
from typing import List
def matrix_transposition(matrix: List[List]) -> List[List]:
    """
    Транспонировать матрицу.
    :param matrix: матрица в виде списка списков.
    :return: транспонированная матрица.
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

if __name__ == '__main__':
    matrix_1 = [[1, 2], [3, 4], [5, 6]]
    print(matrix_1)
    print(matrix_transposition(matrix_1))