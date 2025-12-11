# A
## models.py
```python
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
        date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
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

```
![test](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab08_images/modelsoutput.png)

# B
## serialize.py
```python
from pathlib import Path
import json
from models import Student


def students_to_json(students, path):
    input_json = Path(path)

    if input_json.suffix.lower() != ".json":
        raise ValueError("не json")

    try:
        data = [s.to_dict() for s in students]
    except TypeError:
        raise TypeError("неверный тип данных студентов")

    with open(input_json, "w", encoding="utf-8") as w:
        json.dump(data, w, ensure_ascii=False, indent=2)


def students_from_json(path):
    try:
        with open(path, "r", encoding="utf-8") as r:
            data = json.load(r)
        if not isinstance(data, list):
            raise ValueError("в json не список")
    except FileNotFoundError:
        raise FileNotFoundError("такого файла нет")
    except json.JSONDecodeError:
        raise ValueError

    output_list = []

    for info in data:
        if not isinstance(info, dict):
            raise ValueError
        if not isinstance(info.get("fio"), str):
            raise ValueError("тип данных фио не строка")
        if not isinstance(info.get("birthdate"), str):
            raise ValueError("тип данных даты рождения не строка")
        if not isinstance(info.get("group"), str):
            raise ValueError("тип данных группы не строка")
        if not isinstance(info.get("gpa"), float):
            raise ValueError("тип данных gpa не float")

        output_list.append(Student.from_dict(info))

        return output_list
```

записанный json
![test](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab08_images/savedjson.png)

json для валидации
![test](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab08_images/serializejson.png)