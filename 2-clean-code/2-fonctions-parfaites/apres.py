from typing import Sequence, TypeGuard





def get_pairs(nombres : Sequence[int]) -> Sequence[int]:
    """Renvoie uniquement les nombres pairs d'une séquence de nombres

    ### Args:
        nombres (`Sequence[int]`): La séquence de nombres à filtrer

    ### Raises:
        `TypeError`: Si la séquence n'est pas une séquence d'entiers

    ### Returns:
        `Sequence[int]`: La séquence filtrée
        
    ### Exemples:
        >>> pairs([1, 2, 3, 4, 5])
        [2, 4]
    """
    def est_sequence_entiers(nombres : Sequence[int]) -> TypeGuard[Sequence[int]]:
        return all([isinstance(nombre, int) for nombre in nombres])
    
    if est_sequence_entiers(nombres):
        return list(filter(lambda x : x % 2 == 0, nombres))

    raise TypeError("On peut récupérer uniquement les nombres pairs d'une séquence d'entiers")


def somme(nombres : Sequence[int]) -> int:
    """Renvoie la somme d'une séquence d'entiers.

    ### Args:
        nombres (`Sequence[T]`): La séquence d'entiers dont on va faire la somme

    ### Raises:
        `TypeError`: Dans le cas où un nombre n'est pas un entier

    ### Returns:
        `int`: La somme des entiers
        
    ### Exemples:
        >>> somme([1, 2, 3, 4, 5]) # liste
        15 
        
        >>> somme((1, 2, 3, 4, 5, 6)) # tuple
        21
    """
    resultat = 0
    
    for nombre in nombres:
        if not isinstance(nombre, int):
            raise TypeError(f'{nombre} n\'est pas un entier')
        
        resultat += nombre
        
    return resultat





if __name__ == '__main__':
    print(somme([1, 2, 3, 4, 5]))
    print(somme(get_pairs((1, 2, 3, 4))))
    