from typing import NamedTuple



class GameState(NamedTuple):
    level : int 
    hp : int 
    inventory : list[str] 
    
    
    @classmethod
    def create_initial(cls) -> "GameState":
        return cls(1, 100, [])
    
    
class GameMemento:
    def __init__(self, state : GameState) -> None:
        self.__state = state
        
    @property
    def state(self) -> GameState:
        return self.__state
    
    
class Game:
    def __init__(self) -> None:
        self.__state = GameState.create_initial()
    
    
    @property
    def state(self) -> GameState:
        return self.__state
    
        
    def play(self, level : int, hp : int, inventory : list[str]) -> None:
        self.__state = GameState(level, hp, inventory)
        
        print(f"Playing game... Current state: {self.state}")
        
    
    def save(self) -> GameMemento:
        return GameMemento(self.state)
    
    def restore(self, memento : GameMemento) -> None:
        self.__state = memento.state
        print(f"Restored game... Current state: {self.state}")
        
        
class SaveManager:
    def __init__(self, game : Game) -> None:
        self.__game = game 
        self.__saves : list[GameMemento] = []
        
    def save(self) -> None:
        print("Saving game...")
        self.__saves.append(self.__game.save())
        
    def load_last_save(self) -> None:
        if not self.__saves:
            print("No saves to load.")
            return
        
        memento = self.__saves.pop()
        print("Loading last save...")
        self.__game.restore(memento)
        
        
        
if __name__ == '__main__':
    
    game = Game()
    save_manager = SaveManager(game)

    # Jouer au jeu et faire des sauvegardes
    game.play(level=1, hp=90, inventory=["Sword", "Shield"])
    save_manager.save()

    game.play(level=2, hp=80, inventory=["Sword", "Shield", "Potion"])
    save_manager.save()

    game.play(level=3, hp=70, inventory=["Sword", "Shield", "Potion", "Armor"])

    # Charger la dernière sauvegarde
    save_manager.load_last_save()  # Restore to level 2

    # Charger la sauvegarde précédente
    save_manager.load_last_save()  # Restore to level 1