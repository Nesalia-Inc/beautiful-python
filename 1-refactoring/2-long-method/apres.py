



def double(nombres : list[int]) -> list[int]:
    return [nombre * 2 for nombre in nombres]


def pairs(nombres : list[int]) -> list[int]:
    return [nombre for nombre in nombres if nombre % 2 == 0]


def somme(nombres : list[int]) -> int:
    return sum(nombres)


if __name__ == '__main__':
    print(somme(double(pairs([1, 2, 3, 4, 5]))))
    
    
    