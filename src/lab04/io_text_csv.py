from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    try: 
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        print("такого файла нет")
    except UnicodeDecodeError:
        print("неправильная кодировка, добавь encoding = ваша кодировка")

from pathlib import Path
import csv
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if rows:
        length = len(rows[0])
        for row in rows:
            if len(row) != length:
                raise ValueError ("длины рядов разные")
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

import os
from sys import path
file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\data\\lab04")
path.append(lib_path)

print(read_text("data/lab04/input.txt"))  # должен вернуть строку
Path("data").mkdir(exist_ok=True)
write_csv([("word","count"),("test",3)], "data/check.csv")
