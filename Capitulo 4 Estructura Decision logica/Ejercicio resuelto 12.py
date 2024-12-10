NOM = input()
NHT = int(input())
VHN = float(input())

if NHT > 40:
    HET = NHT - 40
    if HET > 8:
        HEE8 = HET - 8
        SALARIO = 40 * VHN + 16 * VHN + HEE8 * 3 * VHN
    elif 8 > HET:
        SALARIO = 40 * VHN + HET * 2 * VHN
else:
    SALARIO = NHT * VHN

print(f"El trabajador: {NOM} devengó: ${SALARIO}")