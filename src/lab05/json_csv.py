import json, csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    input_json = Path(json_path)
    output_csv = Path(csv_path)

    if not input_json.exists():
        raise FileNotFoundError("файла нет")

    if input_json.is_absolute():
        raise ValueError("путь не относительный")
    if output_csv.is_absolute():
        raise ValueError("путь не относительный")

    if input_json.suffix.lower() != ".json":
        raise ValueError("неверный тип input файла")
    if output_csv.suffix.lower() != ".csv":
        raise ValueError("неверный тип output файла")

    try:
        with open(input_json, "r", encoding="utf8") as r:
            text = json.load(r)
            if not text or text is None:
                raise ValueError("файл пустой")
            if not isinstance(text, list):
                raise ValueError("в файле не список")
            for values in text:
                if not isinstance(values, dict):
                    raise ValueError("в файле не cписок словарей")
            headers = set()
            for item in text:
                headers.update(item.keys())
    except json.JSONDecodeError:
        raise ValueError

    with open(output_csv, "w", encoding="utf8") as w:
        w = csv.DictWriter(w, fieldnames=headers)
        w.writeheader()
        w.writerows(text)


def csv_to_json(csv_path: str, json_path: str) -> None:
    input_csv = Path(csv_path)
    output_json = Path(json_path)

    if not input_csv.exists():
        raise FileNotFoundError("файла нет")

    if input_csv.is_absolute():
        raise ValueError("путь не относительный")
    if output_json.is_absolute():
        raise ValueError("путь не относительный")

    if input_csv.suffix.lower() != ".csv":
        raise ValueError("неверный тип input файла")
    if output_json.suffix.lower() != ".json":
        raise ValueError("неверный тип output файла")

    with open(input_csv, "r", encoding="utf8") as r:
        read = csv.DictReader(r)
        if read.fieldnames is None:
            raise ValueError("нет заголовков")
        row1 = next(read, None)
        if row1 is None:
            raise ValueError("файл пустой")
        readfordump = [row1] + list(read)

    with open(output_json, "w", encoding="utf8") as w:
        json.dump(readfordump, w, ensure_ascii=False, indent=2)


json_to_csv("data/samples/people.json", "data/out/output.csv")
