NI = str(input())
NOM = input()
PAT = int(input())
EST = input()
PAGMAT = 50000

if PAT > 2000000 and EST > 3:
    PAGMAT = PAGMAT + PAT * 0.03

print(f"El estudiante con numero de inscripción: {NI} y nombre: {NOM} debe pagar: ${PAGMAT}")