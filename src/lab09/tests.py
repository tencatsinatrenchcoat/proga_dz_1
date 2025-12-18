from group import *

group = Group("data\\lab09\\students.csv")

# added = group.add(Student('Петров Петр','2003-10-10','BIVT-999',5.0))

# found = group.find("пет")
# print(f'we found{found}')

# removed = group.remove("Петров Петр")

altered = group.update("Иванов Иван", gpa=2.777, group="BIVT-999")
