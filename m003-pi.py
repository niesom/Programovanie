from math import pi, sqrt
arr = [223/71, 22/17 + 37/47 + 88/83, 99**2/(2206*sqrt(2)), sqrt(sqrt(sqrt(5)+6)+7), (10**100/11222.11122)**(1/193)]
diff = list(map(lambda x: abs(pi-x),arr))
print(diff.index(min(diff)))