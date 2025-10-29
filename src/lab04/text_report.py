from collections import Counter
import os
file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\lib\\text")
text_path = os.path.join(file_path, "..\\data\\lab04")

def frequencies_from_text(text: str) -> dict[str, int]:
    from lib.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


    
