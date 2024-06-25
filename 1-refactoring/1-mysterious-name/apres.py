
TAUX_TVA = 0.20


class CalculateurPrixFacture:
    def __init__(self, articles: list[float]):
        self.articles = articles

    def calculer_prix_total(self) -> float:
        return sum(self.articles)

    def appliquer_tva(self) -> float:
        somme = self.calculer_prix_total()
        return somme + somme * TAUX_TVA


def afficher_facture(articles: list[float]) -> None:
    calculateur_facture = CalculateurPrixFacture(articles)
    total_ht = calculateur_facture.calculer_prix_total()
    total_ttc = calculateur_facture.appliquer_tva()
    
    print(f"Total HT: {total_ht:.2f} €")
    print(f"Total TTC: {total_ttc:.2f} €")



if __name__ == '__main__':   
    articles = [10.0, 20.0, 30.0]
    afficher_facture(articles)
    
    
    