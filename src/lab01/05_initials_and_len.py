fio = input()

print(len(fio.strip())) 

fio = fio.split()

result = str(fio[0][0]+fio[1][0]+fio[2][0])
print(result.upper())