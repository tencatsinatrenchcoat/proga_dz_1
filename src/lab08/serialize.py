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
