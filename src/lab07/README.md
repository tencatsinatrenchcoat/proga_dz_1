# A
```python

```

# B
```python

```

## black --check

![Тест](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab07_images/blackcheck.png)

## pytest

![Тест](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab07_images/pytest.png)

## pytest --cov

![Тест](https://github.com/tencatsinatrenchcoat/proga_dz_1/blob/main/images/lab07_images/cov1.png)


при запуске 
```
pytest --cov=src --cov-report=term-missing
```
```
src\lib\text\text.py  90     16    82%   
8, 25, 34, 37, 46, 49, 52-53, 68, 70, 78, 81, 86, 102, 104, 112
```
Непокрытыми остались проверки isinstance, проверки типа input/output файла в функциях 5 лабораторной
