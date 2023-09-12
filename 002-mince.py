import random
for x in range(8):
    salary = random.randrange(100,5000)
    arr = [500,200,100,50,20,10,5,1]
    print(salary)
    for y in arr:
        print(y,":",salary//y)
        salary = salary % y
    print()
