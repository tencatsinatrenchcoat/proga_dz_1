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
    result = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:n]
    return result