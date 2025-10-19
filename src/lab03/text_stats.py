from sys import stdin
from src.lib.text import normalize, top_n, count_freq
def read():
    text = stdin.read(input()) 
    normalize_text = normalize(text)  
    print(f"всего слов: {len(normalize_text)}")
    print(f"уникальных слов: {len(set(normalize_text))}")
    freq = count_freq(normalize_text)
    print(f"топ-5: {top_n(freq, 5)}")
if __name__ == "__main__":
    read()