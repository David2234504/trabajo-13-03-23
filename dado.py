print("-------------------------------------------")
print("--------------Cara opuesta-----------------")
print("-------------------------------------------")

# input
cara = int(input("Digite el número de la cara: "))

# processing
if 1 <= cara <= 6:
    if cara == 1:
        rta = "La cara opuesta es 6"
    elif cara == 2:
        rta = "La cara opuesta es 5"
    elif cara == 3:
        rta = "La cara opuesta es 4"
    elif cara == 4:
        rta = "La cara opuesta es 3"
    elif cara == 5:
        rta = "La cara opuesta es 2"
    elif cara == 6:
        rta = "La cara opuesta es 1"
else:
    rta = "Hubo un problema con el cara digitada"

# output
print("-------------------------------------------")
print(str(rta))
print("-------------------------------------------")

