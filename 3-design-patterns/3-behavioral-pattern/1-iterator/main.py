from turtle import listen
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data : T) -> None:
        self.data = data
        self.next : Optional["Node[T]"] = None


class LinkedList(Generic[T]):
    def __init__(self, value : T):
        self.head = Node(value)

    def append(self, data : T) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __iter__(self) -> "LinkedListIterator[T]":
        return LinkedListIterator(self.head)


class LinkedListIterator(Generic[T]):
    def __init__(self, node: Optional[Node[T]]) -> None:
        self.current = node

    def __iter__(self) -> "LinkedListIterator[T]":
        return self

    def __next__(self) -> T:
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data




if __name__ == '__main__':
    liste = LinkedList[int](1) 
    
    liste.append(2)
    liste.append(3)
    liste.append(4)
    
    
    for number in liste:
        print(number)