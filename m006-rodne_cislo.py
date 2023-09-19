rodne_cislo = list(input("Zadaj rodné číslo: "))
rodne_cislo = list(map(int, rodne_cislo))
gender = "Muž" if rodne_cislo[2] < 2 else "Žena"
rok = f"200{rodne_cislo[1]}" if rodne_cislo[0] == 0 else f"19{rodne_cislo[0]}{rodne_cislo[1]}"
mesiac = f"{rodne_cislo[2]}{rodne_cislo[3]}" if gender == "Muž" else f"{rodne_cislo[2]-5}{rodne_cislo[3]}"
den = f"{rodne_cislo[4]}{rodne_cislo[5]}"
print(f"{gender}\n{int(den)}.{int(mesiac)}.{rok}")