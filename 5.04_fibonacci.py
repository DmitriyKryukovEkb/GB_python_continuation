from typing import Iterable


def fib() -> Iterable[int]:
    a = 0
    b = 1
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b

if __name__ == '__main__':
    for number in fib():
        print(number)
        if number > 1000:
            break
