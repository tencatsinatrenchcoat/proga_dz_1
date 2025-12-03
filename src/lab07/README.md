# A
```python

```

# B
```python

```

## black --check

![Тест](images/lab06_images/lab06_stats_filenotexist.png)

## pytest

![Тест](images/lab06_images/lab06_stats_filenotexist.png)

## pytest --cov

![Тест](images/lab06_images/lab06_stats_filenotexist.png)


при запуске 
```
pytest --cov=src --cov-report=term-missing
```
```
src\lib\text\text.py  90     16    82%   
8, 25, 34, 37, 46, 49, 52-53, 68, 70, 78, 81, 86, 102, 104, 112
```
Непокрытыми остались проверки isinstance, проверки типа input/output файла в функциях 5 лабораторной
