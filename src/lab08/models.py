from dataclasses import *
from datetime import *


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):

        if not isinstance(self.fio, str):
            raise TypeError
        if not isinstance(self.birthdate, str):
            raise TypeError
        if not isinstance(self.group, str):
            raise TypeError
        if not isinstance(self.gpa, float):
            raise TypeError

        try:
            date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
            if date > datetime.now().date():
                raise ValueError("date of brith is in the future")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")

        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError("gpa должен быть от 0 до 5")

    def age(self) -> int:
        # TODO: добавить нормальную валидацию формата даты и диапазона gpa
        date = datetime.strptime(self.birthdate, "%Y-%m-%d").date() #перевод строки в дату bez vremeni
        today = datetime.today().date() 
        current_age = today.year - date.year
        if date.month < today.month or (
            date.month == today.month and date.day < today.day
        ):
            current_age -= 1
        return current_age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        if not isinstance(d, dict):
            raise TypeError
        keys = {"fio", "birthdate", "group", "gpa"}
        if set(d.keys()) != keys:
            raise ValueError
        return cls(d["fio"], d["birthdate"], d["group"], d["gpa"])

    def __str__(self):
        return f"фио: {self.fio}, группа: ({self.group}), дата рождения: {self.birthdate}, средний балл: {self.gpa}"


data = [
    Student("Ivanov Ivan Ivanovich", "2007-12-30", "BIVT-14", 5.00),
    Student("Petrov Petr Petrovich", "2004-02-20", "BIVT-1", 3.84),
]
for students in data:
    print(students)
    print(f"возраст: {students.age()}")
