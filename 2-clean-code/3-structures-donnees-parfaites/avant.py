

class Stack:
    def __init__(self, *elements : int) -> None:
        self._elements : list[int] = list(elements)
        
        
    def push(self, element : int) -> None:
        self._elements.append(element)
        
        
    def pop(self) -> int:
        return self._elements.pop()
    
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    
    
    
if __name__ == '__main__':
    stack = Stack(1, 2, 3, 4)
    
    stack.push(1)
    while not stack.is_empty():
        print(stack.pop())
        
    print(stack.is_empty())