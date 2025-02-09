import sys
from datetime import datetime as dt
from calendar import isleap


def check_date(date: str) -> bool:
    try:
        t = dt.strptime(date, "%d.%m.%Y")
        _isleap(t.year)
        return True
    except ValueError:
        return False

def _isleap(year: int) -> bool:
    print("Високосный." if isleap(year) else "Не високосный.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(check_date(sys.argv[1]))
    else:
        print("Проверьте количество аргументов.")

    from games import *

