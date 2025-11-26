import argparse 
from helpersforproperimport.helpers import json_to_csv, csv_to_json, csv_to_xlsx

def convert():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    json_csv_parser = sub.add_parser("json2csv")
    json_csv_parser.add_argument("--in", dest="input", required=True, help="путь к файлу ввода")
    json_csv_parser.add_argument("--out", dest="output", required=True, help="путь в файлу куда будет записан результат")

    csv_json_parser = sub.add_parser("csv2json")
    csv_json_parser.add_argument("--in", dest="input", required=True, help="путь к файлу ввода")
    csv_json_parser.add_argument("--out", dest="output", required=True, help="путь в файлу куда будет записан результат")

    csv_xlsx_parser = sub.add_parser("csv2xlsx")
    csv_xlsx_parser.add_argument("--in", dest="input", required=True, help="путь к файлу ввода")
    csv_xlsx_parser.add_argument("--out", dest="output", required=True, help="путь в файлу куда будет записан результат")

    conv_args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """
    if conv_args.cmd is None:
        parser.print_help()

    if conv_args.cmd == "json2csv":
        json_to_csv(conv_args.input, conv_args.output)

    elif conv_args.cmd == "csv2json":
        csv_to_json(conv_args.input, conv_args.output)

    elif conv_args.cmd == "csv2xlsx":
        csv_to_xlsx(conv_args.input, conv_args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    convert()