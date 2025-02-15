import os
from typing import Tuple


def files_renamer(

        output_names: str,
        numbers_county: int,
        input_extension: str,
        output_extension: str,
        filename_slice: Tuple[int, int],
        path_dir: str=None
) -> None:
    """
     Функция группового переименования файлов.
    :param path_dir: Путь к директории с файлами для переименования.
    :param output_names: Желаемое конечное имя файлов, в конце прибавляется порядковый номер.
    :param numbers_county: Количество цифр в порядковом номере.
    :param input_extension: Расширение исходных файлов.
    :param output_extension: Расширение конечных файлов.
    :param filename_slice: Диапазон сохраняемого оригинального имени.
    :return: None
    """
    i = 1
    objects = os.listdir(path_dir)
    for obj in objects:
        if os.path.isfile(os.path.join(path_dir, obj)) and obj.split('.')[-1] == input_extension:
            result_name = (
                    obj[filename_slice[0] + 1 : filename_slice[1] + 2] +
                    output_names +
                    f'{i:0{numbers_county}d}' +
                    '.' +
                    output_extension
                    )
            os.rename(os.path.join(path_dir, obj), os.path.join(path_dir, result_name))
            i += 1
