import os
from typing import Tuple


def file_path(filename_path: str) -> Tuple[str, str, str]:
    filepath, extension = os.path.splitext(filename_path)
    path, filename = os.path.split(filepath)
    return path, filename, extension

if __name__ == '__main__':
    print(file_path(r"D:\downloads\Лутц М. - Изучаем Python, том 1, 5-е издание - 2019.pdf"))
