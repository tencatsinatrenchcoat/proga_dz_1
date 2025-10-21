from sys import stdin
import sys
sys.path.append('library')

from library.text import normalize, top_n, count_freq
def read():
    text = stdin.read() 
    normalize_text = normalize(text)  
    print(f"всего слов: {len(normalize_text)}")
    print(f"уникальных слов: {len(set(normalize_text))}")
    freq = count_freq(list(normalize_text))
    print(f"топ-5: {top_n(freq, 5)}")
if __name__ == "__main__":
    read()

# запускается только с команды "echo "Привет, мир! Привет!!!" | py src/lab03/text_stats.py" без $ и с py вместо python
# не видит модули несмотря на __init__.py и module_path