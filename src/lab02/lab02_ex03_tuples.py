def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
         return TypeError
    if not isinstance(rec[0], str):
         return TypeError
    if not isinstance(rec[1], str):
         return TypeError
    fio = rec[0].strip().split()
    group = rec[1].strip()
    gpa = rec[2]
    if not isinstance(gpa, float):
        return TypeError, "неправильно введен gpa"
    if not group:
        return ValueError, "неправильно введена группа"
    if len(fio) < 2:
        return ValueError, "неправильно введено фио"  
    if len(fio) == 2:
            fio_altered = f"{fio[0].capitalize()}, {fio[1][0].capitalize()}."
    if len(fio) == 3:
            fio_altered = f"{fio[0].capitalize()} {fio[1][0].capitalize()}.{fio[2][0].capitalize()}."
    result = f"{fio_altered}, гр.{group}, {gpa:.2f}"  
    return result

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))


