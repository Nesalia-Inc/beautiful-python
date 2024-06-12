from functools import reduce
from typing import Sequence


def somme(nombres : Sequence[int]) -> int:
    return reduce(lambda x, y : x + y, nombres)


def double(nombres : Sequence[int]) -> Sequence[int]:
    return list(map(lambda x : x * 2, nombres))


def triple(nombres : Sequence[int]) -> Sequence[int]:
    return list(map(lambda x : x * 3, nombres))


def pairs(nombres : Sequence[int]) -> Sequence[int]:
    return list(filter(lambda x : x % 2 == 0, nombres))



if __name__ == '__main__':
    liste = [1, 2, 3, 4, 5]
    
    print(somme(liste))
    print(double(pairs(liste)))