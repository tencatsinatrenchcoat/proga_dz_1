import csv
from pathlib import Path
from modelstudent.studentclass import Student


class Group:
    headers = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            raise ValueError
        with open(self, "w", newline="", encoding="utf-8") as w:
            writer = csv.DictWriter(w)
            writer.writeheader()

    def add(self, student: Student):
        fieldnames = ["fio", "birthdate", "group", "gpa"]
        with open(self, "a", newline="", encoding="utf-8") as a:
            writer = csv.DictWriter(a, fieldnames=fieldnames)
            writer.writerow(
                {
                    "fio": student.fio,
                    "birthdate": student.birthdate,
                    "group": student.group,
                    "gpa": student.gpa,
                }
            )

    def find(self, substr: str):
        with open(self, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            res = []
            for row in reader:
                if substr.lower() in row[0].lower():
                    res.append(row)
            return res

    def _read_all(self):
        students = []
        with open(self, "r", encoding="utf-8") as r:
            reader = csv.DictReader(r)
            for row in reader:
                students.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                )
        return students

    def remove(self, fio: str):
        students = self._read_all()
        students = [s for s in students if s[0] != fio]
        with open(self.path, "w", newline="", encoding="utf-8") as w:
            writer = csv.DictWriter(w, fieldnames=self.headers)
            writer.writeheader()
            for s in students:
                writer.writerow(dict(zip(self.headers, s)))


#     def update(self, fio: str, **fields) -> bool:
#         students = self._read_all()
#         updated = False

#         for student in students:
#             if student.fio == fio:
#                 for key, value in fields.items():
#                     if hasattr(student, key):
#                         new_value = float(value) if key == "gpa" else value
#                         setattr(student, key, new_value)
#                 updated = True

#         if updated:
#             with open(self.path, "w", encoding="utf-8", newline="") as f:
#                 writer = csv.writer(f)
#                 writer.writerow(self.headers)
#                 for s in students:
#                     writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

#         return updated


# Group.add("data\\lab09\\students.csv", Student("Simonov Ivan Ivanovich", "1997-03-04", "ISIT-3", 4.33))
Group.remove("data\\lab09\\students.csv", "Simonov Ivan Ivanovich")
