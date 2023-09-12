from math import pi, sqrt
arr = [223/71, 22/17 + 37/47 + 88/83, 99**2/(2206*sqrt(2)), sqrt(sqrt(sqrt(5)+6)+7), (10**100/11222.11122)**(1/193)]
diff = list(map(lambda x: abs(pi-x),arr))
print(diff.index(min(diff)))
# Answer: (10**100/11222.11122)**(1/193) = 5. moznost 

d = input("Zadaj den: ")
m = input("Zadaj mesiac: ")
r = input("Zadaj rok: ")
d, m, r = sum([int(x) for x in d]), sum([int(x) for x in m]), sum([int(x) for x in r])
print("Magic number" if d+m+r<10 else "Not magic number")
