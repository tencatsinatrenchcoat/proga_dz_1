import csv
from pathlib import Path
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

    if input_csv.suffix.lower() != ".csv":
        raise ValueError
    if output_xlsx.suffix.lower() != ".xlsx":
        raise ValueError

    with open(input_csv, "r", encoding="utf8") as r:
        read = csv.DictReader(r)
        if not read.fieldnames:
            raise ValueError("нет заголовков")
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


csv_to_xlsx("data/samples/cities.csv", "data/out/output.xlsx")
