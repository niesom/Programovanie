from time import time
from random import randint
from datetime import datetime,timedelta
seconds = randint(-59011395460, int(time()))
date = datetime.fromtimestamp(seconds) if seconds > 0 else datetime(1970, 1, 1) + timedelta(seconds=seconds)
parsed_date = date.year, date.month, date.day
cipher_sum = sum([sum([int(y) for y in str(x)]) for x in parsed_date])
print(f"{parsed_date[2]}.{parsed_date[1]}. {parsed_date[0]} nie je magické číslo" if cipher_sum > 10 else f"{parsed_date[2]}.{parsed_date[1]}. {parsed_date[0]} je magické číslo")