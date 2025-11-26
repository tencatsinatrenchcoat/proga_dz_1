#top-n
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True, no_punctation: bool = True) -> str:
    if not isinstance(text, str):
        return TypeError
    if casefold:
        text = text.casefold()
    if yo2e:
        while "ё" in text or "Ё" in text:
            text = text.replace("ё", "e", 1).replace("Ё", "Е", 1)
    text = text.replace("\t", " ").replace("\r", " ")
    text = ' '.join(text.split())
    if no_punctation:
        text = re.sub(r'[^\w\s]', '', text)
    return text

import re
def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        return TypeError
    result = []
    result = re.findall(r'\w+(?:-\w+)*', text)
    return result

def count_freq(tokens: list[str]) -> dict[str, int]:
    counts = {}
    if not isinstance(tokens, list):
        return TypeError
    for word in tokens:
        if not isinstance(word, str):
            return TypeError
    for word in tokens:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    result = []
    if not isinstance(freq, dict):
        return TypeError
    for element in freq:
        if not isinstance(element, (str, int)):
            return TypeError
    if not isinstance(n, int) or n <= 0:
        return TypeError
    result = sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
    return result
#lab05 funcs

import json, csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    input_json = Path(json_path)
    output_csv = Path(csv_path)

    if not input_json.exists():
        raise FileNotFoundError ("файла нет")
    
    if input_json.is_absolute():
        raise ValueError ("путь не относительный")
    if output_csv.is_absolute():
        raise ValueError ("путь не относительный")
    
    if input_json.suffix.lower() != '.json':
        raise ValueError ("неверный тип input файла")
    if output_csv.suffix.lower() != '.csv':
        raise ValueError ("неверный тип output файла")
    
    try:
        with open(input_json, "r", encoding = "utf8") as r:
            text = json.load(r)
            if not text:
                raise ValueError ("файл пустой")
            if not isinstance(text, list):
                raise ValueError("в файле не список")
            for values in text:
                if not isinstance(values, dict):
                    raise ValueError("в файле не cписок словарей")
            headers = set()
            for item in text:
                headers.update(item.keys())
    except json.JSONDecodeError:
        "json decode error"

    with open(output_csv, "w", encoding = "utf8") as w:
        w = csv.DictWriter(w, fieldnames=headers)
        w.writeheader()
        w.writerows(text)


def csv_to_json(csv_path: str, json_path: str) -> None:
    input_csv = Path(csv_path)
    output_json = Path(json_path)

    if not input_csv.exists():
        raise FileNotFoundError ("файла нет")
    
    if input_csv.is_absolute():
        raise ValueError ("путь не относительный")
    if output_json.is_absolute():
        raise ValueError ("путь не относительный")
    
    if input_csv.suffix.lower() != '.csv':
        raise ValueError ("неверный тип input файла")
    if output_json.suffix.lower() != '.json':
        raise ValueError ("неверный тип output файла")
    
    with open(input_csv, "r", encoding = "utf8") as r:
        read = csv.DictReader(r)
        if read.fieldnames is None:
            raise ValueError ("нет заголовков")
        row1 = next(read, None)
        if row1 is None:
            raise ValueError("файл пустой")
        readfordump = [row1] + list(read)


       
    with open(output_json, "w", encoding = "utf8") as w:
        json.dump(readfordump, w, ensure_ascii=False, indent = 2)


from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    input_csv = Path(csv_path)
    output_xlsx = Path(xlsx_path)
    if not input_csv.exists():
        raise FileNotFoundError 

    if input_csv.is_absolute():
        raise ValueError
    if output_xlsx.is_absolute():
        raise ValueError
    
    if input_csv.suffix.lower() != '.csv':
        raise ValueError 
    if output_xlsx.suffix.lower() != '.xlsx':
        raise ValueError 
    
    with open(input_csv, "r", encoding = "utf8") as r:
        read = csv.DictReader(r)
        if not read.fieldnames:
            raise ValueError ("нет заголовков")
        rows = list(read)
        if not rows:
           return ValueError
            
    w = Workbook()
    sheet1 = w.active
    sheet1.title = "sheet 1"
    sheet1.append(read.fieldnames)

    for row in rows:
        sheet1.append(list(row.values()))

    for column in sheet1.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            if cell.value is not None:
                max_length = max(max_length, len(str(cell.value)))
                sheet1.column_dimensions[column_letter].width = max(max_length + 2, 8)
    w.save(output_xlsx)

