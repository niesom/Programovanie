# Zadanie úlohy explicitne nevyžaduje validáciu dátumu, preto toto riešenie neoveruje, či sa vygenerovaný dátum nachádza v kalendári. 
# Kód, ktorý to kontroluje je zakomentovaný na konci tohto súboru.
import random
month = random.randint(1,12)
year = random.randint(100,2022)
day = random.randint(1,31)
def cipher_sum(n):
    result = 0
    while n > 0:
        result += n%10
        n = n//10
    return result
if cipher_sum(day) + cipher_sum(month) + cipher_sum(year) < 10:
    print(day,month,year,"is magic number")
else:
    print(day,month,year,"is not magic number")
"""
import random
month = random.randint(1,12)
year = random.randint(100,2022)
if month in [1,3,5,7,8,10,12]:
    day = random.randint(1,31)
elif month in [4,6,9,11]:
    day = random.randint(1,30)
else:
    if year%400==0 or (year%4==0 and year%100!=0):
        day = random.randint(1,29)
    else:
        day = random.randint(1,28)
def cipher_sum(n):
    result = 0
    while n > 0:
        result += n%10
        n = n//10
    return result
if cipher_sum(day) + cipher_sum(month) + cipher_sum(year) < 10:
    print(day,month,year,"is magic number")
else:
    print(day,month,year,"is not magic number")
"""
