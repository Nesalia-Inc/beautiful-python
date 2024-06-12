from typing import Sequence


def somme(nombres : Sequence[int]) -> int:
    resultat = 0
    
    for nombre in nombres:
        resultat += nombre
        
    return resultat


def double(nombres : Sequence[int]) -> Sequence[int]:
    doubles : list[int] = []
    
    for nombre in nombres:
        doubles.append(nombre * 2)
        
    return doubles


def triple(nombres : Sequence[int]) -> Sequence[int]:
    triples : list[int] = []
    
    for nombre in nombres:
        triples.append(nombre * 2)
        
    return triples


def pairs(nombres : Sequence[int]) -> Sequence[int]:
    resultat : list[int] = []
    
    for nombre in nombres:
        if nombre % 2 == 0:
            resultat.append(nombre)
        
    return resultat


if __name__ == '__main__':
    liste = [1, 2, 3, 4, 5]
    
    print(double(pairs(liste)))