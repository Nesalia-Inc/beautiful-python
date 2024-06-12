

def somme(nombres : list[int]) -> int:
    resultat = 0
    
    for nombre in nombres:
        resultat += nombre
        
    return resultat


def double(nombres : list[int]):
    for i in range(len(nombres)):
        nombres[i] *= 2
        
        
        
        
if __name__ == '__main__':
    liste = [1, 2, 3, 4, 5]
    double(liste)
    print(liste)