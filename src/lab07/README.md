# A
```python
from sys import stdin, path
import os

file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\lib\\text")
path.append(lib_path)

from text import normalize, tokenize, count_freq, top_n

import pytest


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик Ёлка", "ежик елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        ("this is a text", ["this", "is", "a", "text"]),
        ("  ", []),
        ("", []),
        ("this, has? punctuation!", ["this", "has", "punctuation"]),
    ],
)
def test_tokenize_basic(tokens, expected):
    assert tokenize(tokens) == expected


@pytest.mark.parametrize(
    "countfreq, expected",
    [
        (
            ["cat", "cat", "dog", "mouse", "dog", "cat"],
            {"cat": 3, "dog": 2, "mouse": 1},
        ),
        ([], {}),
    ],
)
def test_count_freq_and_top_n(countfreq, expected):
    assert count_freq(countfreq) == expected


@pytest.mark.parametrize(
    "topn, expected",
    [
        ({"cat": 3, "dog": 2, "mouse": 1}, [("cat", 3), ("dog", 2), ("mouse", 1)]),
        ({"ant": 1, "pigeon": 1, "cat": 1}, [("ant", 1), ("cat", 1), ("pigeon", 1)]),
    ],
)
def test_top_n_tie_breaker(topn, expected):
    assert top_n(topn, expected)
```

# B
```python
import pytest
import json, csv
from pathlib import Path

from sys import path
import os

file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\lib\\text")
path.append(lib_path)
from text import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "output.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "output.json"

    with src.open("w", encoding="utf8", newline="") as w:
        write = csv.DictWriter(w, fieldnames=["name", "age"])
        write.writeheader()
        write.writerow({"name": "OldPerson", "age": "98"})
    csv_to_json(str(src), str(dst))
    with dst.open(encoding="utf8") as f:
        res = json.load(f)
        assert isinstance(res, list)
        assert res[0]["name"] == "OldPerson"
        assert res[0]["age"] == "98"


def test_empty_file_json_to_csv(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "output.csv"
    data = []
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_empty_file_csv_to_json(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "output.json"
    src.write_text("", encoding="utf8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_no_file_json_to_csv(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        json_to_csv("nojson.json", "nocsv.csv")


def test_no_file_csv_to_json(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        csv_to_json("nocsv.csv", "output.json")
```

## black --check

![Тест](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab07_images/blackcheck.png)

## pytest

![Тест](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab07_images/pytest.png)

## pytest --cov

![Тест](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab07_images/cov1.png)


при запуске 
```
pytest --cov=src --cov-report=term-missing
```
```
src\lib\text\text.py  90     16    82%   
8, 25, 34, 37, 46, 49, 52-53, 68, 70, 78, 81, 86, 102, 104, 112
```
Непокрытыми остались проверки isinstance, проверки типа input/output файла в функциях 5 лабораторной
