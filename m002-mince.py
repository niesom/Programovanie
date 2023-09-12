import random

"""
# spocita celkovy pocet bankoviek pre vsetkych robotnikov dokopy
b = [0 for x in range(8)]
for worker in range(5):
    salary = random.choice(range(500,2000))
    arr = [500,200,100,50,20,10,5,1]
    print(salary)
    for x in range(len(arr)):
        b[x] += salary//arr[x]
        salary = salary%arr[x]
answer = '\n'.join([f"{arr[x]}:{b[x]}" for x in range(len(arr))])
print(answer)
"""
# spocita celkovy pocet bankoviek pre kazdeho robotnika zvlast
for worker in range(5):
    salary = random.choice(range(500,2000))
    b = [0 for x in range(8)]
    arr = [500,200,100,50,20,10,5,1]
    print(salary)
    for x in range(len(arr)):
        b[x] += salary//arr[x]
        salary = salary%arr[x]
    answer = '\n'.join([f"{arr[x]}:{b[x]}" for x in range(len(arr))])
    print(answer)
    print()

    




