from collections import deque
from typing import Any, Optional

class Stack:
    def __init__(self, items: Optional[list[Any]] = None):  # Fixed: added items param
        self._data: list[Any] = []
        if items is not None:
            self._data.extend(items)
        
    def push(self, num) -> None:
        self._data.append(num)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("стэк пустой")
        else:
            return self._data.pop()


    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        else:
            return self._data[-1]
        

    def is_empty(self) -> bool:
        if len(self._data) == 0:
            return True
        else:
            return False
        
    def __len__(self) -> int:
        return len(self._data)
    
class Queue:
    def __init__(self, items: Optional[list[Any]] = None):
        self._data: deque[Any] = deque()
        if items is not None:
            for item in items:
                self.enqueue(item)

    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("очередь пустая")
        return self._data.popleft()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        else:
            return self


    def is_empty(self) -> bool:   
        if len(self._data)==0:
            return True
        else:
            return False
    
    def __len__(self) -> int:
        return len(self._data)
    

print("------Stack------")

stack = Stack([12,24,36,48])

print(f'убираем верхний элемент : {stack.pop()}')
print(f'пустой ли стек? {stack.is_empty()}')
print(f'число сверху : {stack.peek()}')
stack.push(10000)
print(f'значение сверху после добавления числа в стек : {stack.peek()}')
print(f'длина: {len(stack)}')

print("------Queue------")

q = Queue([12,24,36,48])

print(f'первый элемент: {q.peek()}')
q.dequeue()
print(f'первый элемент после удаления числа: {q.peek()}')
q.enqueue(52)
print(f'первый элемент после добавления: {q.peek()}')
print(f'пустая ли очередь? {q.is_empty()}')
print(f'количество элементов в очереди : {len(q)}')
