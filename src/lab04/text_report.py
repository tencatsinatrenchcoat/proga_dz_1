from collections import Counter
import sys
import os
import csv
from sys import path
from pathlib import Path
file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\lib\\text")
path.append(lib_path)

from text import normalize, tokenize, top_n, count_freq
def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise TypeError
    for i in freq:
        if not isinstance(i, (str, int)):
            raise TypeError
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def report_generator():
    inputfile=Path("data/lab04/input.txt")
    outputfile=Path("data/report.csv")
    with open(inputfile, "r", encoding = "utf8") as r:
        text = r.read()
    if inputfile.suffix.lower() != '.txt':
        raise ValueError 
    if outputfile.suffix.lower() != '.csv':
        raise ValueError 
    try:
        with open(outputfile, "w", newline = "", encoding = "utf8") as f:
            writer = csv.DictWriter(f, fieldnames=["word", "count"])
            writer.writeheader()
            for word, count in sorted_word_counts(frequencies_from_text(text)):
                writer.writerow({"word": word, "count": count})
    except FileNotFoundError:
        print("файла нет") 
        sys.exit(1)      
    print(f"всего слов: {len(tokenize(text))}")
    print(f"уникальных: {len(set(tokenize(text)))}")
    print(f"топ-5: {top_n(count_freq(tokenize(normalize(text))))}")
if __name__ == "__main__":
    report_generator()

#check for json/csv




    
