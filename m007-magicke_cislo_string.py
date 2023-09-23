def get_magic_number(date): 
    if int(date) < 10:
        return date
    else:
        return get_magic_number(str(sum([int(x) for x in date])))
date = input("Zadaj dátum: ")
day = date[0:2]
month = date[3:5]
year = date[6:10]
print(f"Magické číslo dátumu {day}.{month}. {year} je: {get_magic_number(day+month+year)}")
