from math import sqrt
pi = 3.141592653589793
first_value = 223/71
second_value = 22/17 + 37/47 + 88/83
third_value = 99**2/(2206*sqrt(2))
fourth_value = sqrt(sqrt(sqrt(5)+6)+7)
fifth_value = (10**100/11222.11122)**(1/193)
print(first_value-pi)
print(second_value-pi)
print(third_value-pi)
print(fourth_value-pi)
print(fifth_value-pi)

d = int(input("Zadaj den: "))
m = int(input("Zadaj mesiac: "))
r = int(input("Zadaj rok: "))
def cipher_sum(n):
    result = 0
    while n > 0:
        result += n%10
        n = n//10
    return result
if cipher_sum(d) + cipher_sum(m) + cipher_sum(r) < 10:
    print("Magic number")
else:
    print("Not magic number")

