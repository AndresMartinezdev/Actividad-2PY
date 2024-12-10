VALCOMP = float(input())
COLOR = input()

if COLOR == "BLANCO":
    PDES = 0
elif COLOR == "VERDE":
    PDES = 10
elif COLOR == "AMARILLO":
    PDES = 25
elif COLOR == "AZUL":
    PDES = 50
else:
    PDES = 100


VALPAG = VALCOMP - (PDES * VALCOMP / 100)

print(f"EL CLIENTE DEBE PAGAR: ${VALPAG}")
