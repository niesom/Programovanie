date = input("Zadaj dátum: ")
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])
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