



def somme_nombres_pairs(nombres : list[int]) -> int:
    def est_pair(nombre : int) -> int:
        return nombre % 2 == 0
    
    resultat = 0 
    
    for nombre in nombres:
        if est_pair(nombre):
            resultat += nombre 
            
    return resultat 