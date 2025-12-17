from typing import Any, Iterator, Optional

class Node:
    def __init__(self, value: Any): 
        self.value = value
        self.next: Optional[Node] = None

class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node  # Fixed: set tail when list is empty
        else:
            self.tail.next = new_node  # Fixed: link current tail to new node
            self.tail = new_node         # Fixed: update tail
        self._size += 1

    def prepend(self, value) -> None:
        node = Node(value)
        node.next = self.head  # Fixed: properly set next pointer
        self.head = node
        if self._size == 0:
            self.tail = node
        self._size += 1
        

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("индекс меньше нуля или больше размера списка")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
    
    def remove(self, value) -> None:
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None: 
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None: 
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self._size -= 1
            return

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
            return self._size

    def __repr__(self) -> str:
        values = list(self)
        return (f"SinglyLinkedList({values}")


sll = SinglyLinkedList()
print(f'длина : {len(sll)}')

sll.append(11)
sll.append(22)
sll.append(99)

print(f'длина после добавления элементов: {len(sll)}') 
print(f'односвязаный список : {list(sll)}')

sll.insert(1, 0.999)
print(f'длина списка после добавления на 1 индекс числа 0.999 : {len(sll)}')
print(f'односвязаный список : {list(sll)}')
sll.append(1000)
print(f'односвязанный список после добавления числа в конец : {list(sll)}')
print(f'длина после добавления элементa: {len(sll)}')