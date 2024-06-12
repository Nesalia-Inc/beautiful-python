from collections.abc import Collection
from typing import Iterator, TypeVar

T = TypeVar("T")


class Stack(Collection[T]):
    def __init__(self, *elements : T) -> None:
        self._elements : list[T] = list(elements)
        
        
    def push(self, element : T) -> None:
        self._elements.append(element)
        
    def pop(self) -> T:
        return self._elements.pop()
    
    
    def __len__(self) -> int:
        return len(self._elements)
    
    def __contains__(self, x: object) -> bool:
        return x in self._elements
    
    def __iter__(self) -> Iterator[T]:
        while not len(self) == 0:
            yield self.pop()
    
    
    
if __name__ == '__main__':
    pile = Stack(1, 2, 3, 4)
    
    pile.push(1)
    
    for element in pile:
        print(element)
        
        
    print(len(pile))