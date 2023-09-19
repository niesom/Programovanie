rodne_cislo = list(input())
if int(rodne_cislo[2]) > 1:
    print("Žena")
    mesiac = str(int(rodne_cislo[2])-5) + str(rodne_cislo[3])
else:
    print("Muž")
    mesiac = str(int(rodne_cislo[2])) + str(rodne_cislo[3])
mesiac = int(mesiac)
if int(rodne_cislo[0])==0:
    print("Rok:" + " 200" + str(rodne_cislo[1]))
else:
    rok = int(rodne_cislo[0]+rodne_cislo[1])
    print("Rok:" + " 19" + str(rok))
den = rodne_cislo[4]+rodne_cislo[5]
den = int(den)
print("Mesiac:",mesiac)
print("Deň:",den)