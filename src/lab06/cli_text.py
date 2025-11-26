import argparse 
from helpersforproperimport.helpers import top_n, normalize, tokenize, count_freq
from pathlib import Path

def cat_stats():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6 для работы с текстом")
    subparsers = parser.add_subparsers(dest="command")

        # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="путь к файлу с текстом")
    cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

        # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="путь к файлу с текстом")
    stats_parser.add_argument("--top", type=int, default=5, help="количество выводимых слов")

    stat_args = parser.parse_args()
    input_path = Path(stat_args.input)
    if not input_path.exists():
        parser.error("файл не найден")

    if stat_args.command == "cat":
        """ Реализация команды cat """
        try:
            lines = 0
            with open(stat_args.input , "r", encoding = "utf8") as r:   
                for line in r:
                    lines += 1
                    print(lines, line.rstrip())
        except:
            parser.error
            "ошибка чтения файла"
           

    if stat_args.command == "stats":

            """ Реализация команды stats """
    try:
        with open(stat_args.input, 'r', encoding='utf-8') as f:
            text = f.read()
            normalized_text = normalize(text)
            if len(normalized_text.strip()) == 0:
                return ValueError
            tokens = tokenize(normalized_text)
            freq = count_freq(tokens)
            top_words = top_n(freq, stat_args.top)
            print(top_words)
    except:
         parser.error
         "ошибка чтения файла"

if __name__ == "__main__":
    cat_stats()

