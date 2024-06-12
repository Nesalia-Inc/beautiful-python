


from typing import Sequence


def somme(nombres : Sequence[int]) -> int:
    resultat = 0
    
    for nombre in nombres:
        resultat += nombre 
        
    return resultat


def double(nombres : Sequence[int]) -> Sequence[int]:
    resultat : list[int] = []
    
    for nombre in nombres:
        resultat.append(nombre * 2)
        
    return resultat



if __name__ == '__main__':
    print(double([1, 2, 3, 4, 5]))