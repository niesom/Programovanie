from re import sub
sentence = input("Zadaj vetu: ")
print(sub("[ ]{2,}", " ", sentence))