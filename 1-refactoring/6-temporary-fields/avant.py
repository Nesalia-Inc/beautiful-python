import random


class Entite:
    def __init__(self, est_joueur):
        self.est_joueur = est_joueur
        self.position = [0, 0]

    def deplacer(self, direction=None):
        if self.est_joueur:
            if direction == "haut":
                self.position[1] += 1
            elif direction == "bas":
                self.position[1] -= 1
            elif direction == "gauche":
                self.position[0] -= 1
            elif direction == "droite":
                self.position[0] += 1
        else:
            self.position[0] += random.choice([-1, 1])
            self.position[1] += random.choice([-1, 1])

    def attaquer(self):
        if self.est_joueur:
            return "Le joueur attaque!"
        else:
            return "Le monstre attaque!"


if __name__ == '__main__':
    joueur = Entite(est_joueur=True)
    monstre = Entite(est_joueur=False)

    joueur.deplacer("haut")
    monstre.deplacer()

    print(joueur.position)  # [0, 1]
    print(monstre.position)  # Position aléatoire

    print(joueur.attaquer())  # "Le joueur attaque!"
    print(monstre.attaquer())  # "Le monstre attaque!"
