TAUX_TVA = 0.20

class CalculateurFacture:
    def __init__(self, articles: list[float]):
        self.articles = articles

    def calculer_somme(self) -> float:
        return sum(self.articles)

    def appliquer_tva(self) -> float:
        somme = self.calculer_somme()
        return somme + somme * TAUX_TVA

def afficher_facture(articles: list[float]) -> None:
    facture = CalculateurFacture(articles)
    total_ht = facture.calculer_somme()
    total_ttc = facture.appliquer_tva()
    print(f"Total HT: {total_ht:.2f} €")
    print(f"Total TTC: {total_ttc:.2f} €")



if __name__ == '__main__':   
    articles = [10.0, 20.0, 30.0]
    afficher_facture(articles)
