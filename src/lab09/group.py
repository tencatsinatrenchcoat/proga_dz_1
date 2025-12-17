import csv
from pathlib import Path
from modelstudent.studentclass import Student


class Group:
    headers = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")

    def _read_all(self):
        # TODO: реализовать чтение строк из csv
        students = []
        with self.path.open("r", newline="", encoding="utf-8") as r:
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

    def list(self):
        return self._read_all()

    def add(self, student: Student):
        with self.path.open("a", newline="", encoding="utf-8") as a:
            writer = csv.DictWriter(a, fieldnames=self.headers)
            writer.writerow(
                {
                    "fio": student.fio,
                    "birthdate": student.birthdate,
                    "group": student.group,
                    "gpa": student.gpa,
                }
            )
  

    def find(self, substr: str):
        # TODO: реализовать метод find()
        substr = substr.casefold()
        with self.path.open('r', newline='', encoding='utf-8') as r:
            reader = csv.reader(r)
            res = []
            for row in reader:
                if substr.lower() in row[0].lower():
                    res.append(row)
            return res

    def remove(self, fio: str):
        with open(self.path,'r', newline='', encoding='utf-8') as r:
            reader = csv.reader(r)
            # idk tf to do here honestly 

        with self.path.open('w', newline='', encoding='utf-8') as w:
            writer = csv.DictWriter(w, fieldnames=self.headers)
            writer.writerow(self.headers)
            students = #idk what to make it take here besides [s for s in students if s[0] != fio] which doesnt seem to work
            for student in students:
                writer.writerow(           #it doesnt see student as possessing the attributes  
                    {
                    "fio": student.fio,
                    "birthdate": student.birthdate,
                    "group": student.group,
                    "gpa": student.gpa,
                    }

                )

    # def update(self, fio: str, **fields):
    #     # TODO: реализовать метод update()
