import csv
from pathlib import Path
from modelstudent.studentclass import Student


class Group:
    headers = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            with open(self.path, "w", newline="", encoding="utf-8") as w:
                writer = csv.DictWriter(w)
                writer.writeheader()

    def _read_all(self):
        student_list = []
        with open(self.path, "r", encoding="utf-8") as r:
            reader = csv.DictReader(r)
            if reader.fieldnames != self.headers:
                raise ValueError()
            for row in reader:
                if not all(row.values()):
                    continue

                student_list.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                )

        return student_list

    def list(self):
        return self._read_all()

    def add(self, student: Student):
        with open(self.path, "a", newline="", encoding="utf-8") as a:
            writer = csv.DictWriter(a)
            writer.writerow(
                [student.fio, student.birthdate, student.group, student.gpa]
            )
        return

    def find(self, substr: str):
        substr = substr.lower()
        return [s for s in self._read_all() if substr in s.fio.lower()]

    def remove(self, fio: str):
        students = self._read_all()
        students = [s for s in students if s.fio != fio]
        with open(self.path, "w", newline="", encoding="utf-8") as w:
            writer = csv.writer(w)
            writer.writerow(self.headers)
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])


def update(self, fio: str, **fields) -> bool:
    students = self._read_all()
    updated = False

    for student in students:
        if student.fio == fio:
            for key, value in fields.items():
                if hasattr(student, key):
                    new_value = float(value) if key == "gpa" else value
                    setattr(student, key, new_value)
            updated = True

    if updated:
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

    return updated
