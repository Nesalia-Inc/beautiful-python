


# Cette fonction semble petite mais il y a beaucoup de problèmes 
# Déjà, elle a plusieurs responsabilités :
# 1. Récupérer uniquement les nombres pairs 
# 2. Faire le double des nombres 
# 3. Faire la somme de tous ces nombres
def somme_double_pairs(nombres : list[int]) -> int:
    resultat = 0
    
    for nombre in nombres:
        
        # On peut créer des fonctions qui s'occupent des ces tâches 
        # Même si ça rend le code moins performant
        # On aurait du O(3n) au lieu de O(n + 3) environ mais
        # Le code serait plus simple à comprendre.
        if nombre % 2 == 0:
            resultat += nombre * 2
            
    return resultat


# Alors bien sûr, ici le code n'est pas horrible et reste simple. 
# Dans ce cas, si le projet est assez court, tu peux laisser le code comme il est.
# Mais si tu vois d'autres fonctions du projet qui cherche de nombres pairs ou 
# fais le double des nombres d'une liste, tu peux extraire ces fonctions. 