TAXE = 0.20

class Calculateur:
    def __init__(self, arti: list[float]):
        self.arti = arti

    def calcu(self) -> float:
        return sum(self.arti)

    def appl(self) -> float:
        s = self.calcu()
        return s + s * TAXE

def facture(arti: list[float]) -> None:
    facture = Calculateur(arti)
    ttht = facture.calcu()
    ttttc = facture.appl()
    print(f"Total HT: {ttht:.2f} €")
    print(f"Total TTC: {ttttc:.2f} €")



if __name__ == '__main__':   
    articles = [10.0, 20.0, 30.0]
    facture(articles)
