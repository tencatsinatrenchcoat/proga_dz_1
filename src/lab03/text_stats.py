from sys import stdin, path
import os
file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\lib\\text")
path.append(lib_path)
from text import normalize, tokenize, count_freq, top_n

def read():
    text = stdin.read() 
    normal_text = normalize(text) 
    token_text = tokenize(text)
    print(f"всего слов:{len(token_text)}")
    print(f"уникальных слов:{len(tokenize(normal_text))}")
    freq = count_freq(list(tokenize(normal_text)))
    print(f"топ-5:{top_n(freq, 5)}")
if __name__ == "__main__":
    read()

#echo "Privet, mir! Privet!!!" | py src/lab03/text_stats.py