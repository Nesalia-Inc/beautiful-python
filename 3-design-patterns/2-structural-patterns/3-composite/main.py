from typing import Protocol


class FileSystemComponent(Protocol):
    def get_size(self) -> int: ...
    def display(self, indentation : int) -> None: ...
    
    
class File(FileSystemComponent):
    def __init__(self, name : str, size : int):
        self.name = name
        self.size = size 
        
    
    def get_size(self) -> int:
        return self.size
    
    def display(self, indentation: int) -> None:
        print('  ' * indentation + f'- File: {self.name}, Size: {self.size}')
        
        
class Directory(FileSystemComponent):
    def __init__(self, name : str) -> None:
        self.name = name
        self.__children : list[FileSystemComponent] = []
        
    
    def append(self, component : FileSystemComponent) -> None:
        self.__children.append(component)
        
    def remove(self, component : FileSystemComponent) -> None:
        self.__children.remove(component)
        
    
    def get_size(self) -> int:
        total_size = 0
        for child in self.__children:
            total_size += child.get_size()
        return total_size
    
    def display(self, indentation: int) -> None:
        print('  ' * indentation + f'- Directory: {self.name}')
        for child in self.__children:
            child.display(indentation + 1)
            
            
            
if __name__ == '__main__':
    directory1 = Directory("dir1")
    directory2 = Directory("dir2")
    directory3 = Directory("dir3")
    
    directory1.append(directory2)
    directory1.append(directory3) 
    
    directory1.append(File("file1.txt", 100))

    directory2.append(File("file2.txt", 200))
    directory2.append(File("file3.txt", 150))
    
    directory3.append(File("file4.txt", 300))
    
    directory1.display(0)
    
    print(f"Total Size : {directory1.get_size()}")
