# proga_dz_1 wow

Lab01

Задание 1  
```python
name = input()
age = input()

print(f"имя: {name}")
print(f"привет {name}! через год тебе будет {int(age)+1}")
```

![Тест задание 1](images/lab01/test_lab_01_ex01_corrected.png)

Задание 2 
```python
a = input()
b = input()

if "," in a:
    a = a.replace(",", ".", 1)
if "," in b:
    b = b.replace(",", ".", 1)

sum = float(a) + float(b)
avg = float((float(a) + float(b))/2)

print(f"sum:{sum:.2f}; avg:{avg:.2f}")
``` 

![Тест задание 2](images/lab01/test_lab_01_ex02_corrected.png)

Задание 3 
```python
price = float(input("цена, $ "))
discount = float(input("скидка, % "))
vat = float(input("ндс, % "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"база после скидки {base:.2f} $")
print(f"ндс {(vat_amount):.2f} $")
print(f"итого к оплате {(total):.2f} $")
```

![Тест задание 3](images/lab01/test_lab_01_ex03_corrected.png)

Задание 4
```python
m = int(input())
hours = m // 60
minutes = m % 60

print(f"{hours}:{minutes}")
```

![Тест задание 4](images/lab01/test_lab_01_ex04_corrected.png)

Задание 5  
```python
fio = input().strip().split()

result = str(fio[0][0]+fio[1][0]+fio[2][0])
print(result.upper())

fio_2 = " ".join(fio)
count = 0
for i in fio_2:
    count += 1
print(count)
```

![Тест задание 5](images/lab01/test_lab_01_ex5_corrected.png)
