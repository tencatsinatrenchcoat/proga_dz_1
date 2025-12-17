from group import *

group = Group("data\\lab09\\students.csv")  # maybe here also pass it the path

read = group.list()
print(read)

# added = group.add(Student('Петров Петр','2003-10-10','BIVT-999',5.0))

found = group.find("пет")
print(f'we found{found}')

removed = group.remove("Петров Петр,2003-10-10,BIVT-999,5.0")
print(removed)
