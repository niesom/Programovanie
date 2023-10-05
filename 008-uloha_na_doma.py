sentence = input("Zadaj vetu: ")
last_char = ""
output = ""
for char in sentence:
    if last_char != " " or last_char == " " and char != " ":
        output += char
        last_char = char
print(output)
