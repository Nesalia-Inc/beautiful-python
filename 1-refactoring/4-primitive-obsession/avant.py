

def creer_ville(nom : str, code_postal : int, habitants : int) -> list[int | str]:
    return [nom, code_postal, habitants]



if __name__ == '__main__':
    paris = creer_ville("Paris", 75000, 2_610_000)
    
    print(f"La ville de {paris[0]} possède {paris[2]} habitants.")