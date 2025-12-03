from sys import stdin, path
import os

file_path = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(file_path, "..\\lib\\text")
path.append(lib_path)

from text import normalize, tokenize, count_freq, top_n

import pytest


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик Ёлка", "ежик елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        ("this is a text", ["this", "is", "a", "text"]),
        ("  ", []),
        ("", []),
        ("this, has? punctuation!", ["this", "has", "punctuation"]),
    ],
)
def test_tokenize_basic(tokens, expected):
    assert tokenize(tokens) == expected


@pytest.mark.parametrize(
    "countfreq, expected",
    [
        (
            ["cat", "cat", "dog", "mouse", "dog", "cat"],
            {"cat": 3, "dog": 2, "mouse": 1},
        ),
        ([], {}),
    ],
)
def test_count_freq_and_top_n(countfreq, expected):
    assert count_freq(countfreq) == expected


@pytest.mark.parametrize(
    "topn, expected",
    [
        ({"cat": 3, "dog": 2, "mouse": 1}, [("cat", 3), ("dog", 2), ("mouse", 1)]),
        ({"ant": 1, "pigeon": 1, "cat": 1}, [("ant", 1), ("cat", 1), ("pigeon", 1)]),
    ],
)
def test_top_n_tie_breaker(topn, expected):
    assert top_n(topn, expected)
