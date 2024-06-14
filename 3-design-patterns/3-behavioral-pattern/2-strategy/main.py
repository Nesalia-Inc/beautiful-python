from typing import Protocol, TypeVar, Sequence

T = TypeVar("T", int, float)


class SortingStrategy(Protocol[T]):
    def sort(self, sequence : Sequence[T]) -> Sequence[T]: ...
    
    
    
class IncreasingSort(SortingStrategy):
    def sort(self, sequence : Sequence[T]) -> Sequence[T]:
        sorted_sequence = list(sequence)
        for i in range(1, len(sorted_sequence)):
            key = sorted_sequence[i]
            j = i - 1
            while j >= 0 and sorted_sequence[j] > key:
                sorted_sequence[j + 1] = sorted_sequence[j]
                j -= 1
            sorted_sequence[j + 1] = key
        return sorted_sequence
    
    
class DecresingSort(SortingStrategy):
    def sort(self, sequence : Sequence[T]) -> Sequence[T]:
        sorted_sequence = list(IncreasingSort().sort(sequence))
        sorted_sequence.reverse()
        return sorted_sequence
    
    

class EvenOddSort(SortingStrategy):
    def __get_evens(self, sequence : Sequence[T]) -> Sequence[T]:
        return list(filter(lambda x : x % 2 == 0, sequence))
    
    def __get_odds(self, sequence : Sequence[T]) -> Sequence[T]:
        return list(filter(lambda x : x % 2 == 1, sequence))


    def sort(self, sequence : Sequence[T]) -> Sequence[T]:
        evens = IncreasingSort().sort(self.__get_evens(sequence))
        odds = IncreasingSort().sort(self.__get_odds(sequence))
        
        return list(evens) + list(odds)
    
    
    
class SortingContext:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort(self, sequence: Sequence[T]) -> Sequence[T]:
        return self.strategy.sort(sequence)
        
        
    
    
if __name__ == '__main__':
    nombres = [6, 1, 4, 2, 3]
    
    strategy = SortingContext(EvenOddSort())
    
    print(strategy.sort(nombres))
    