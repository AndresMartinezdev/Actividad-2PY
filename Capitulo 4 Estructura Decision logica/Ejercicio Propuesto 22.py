NOM = str(input("INGRESE SU NOMBRE: "))
SALARX = float(input("INGRESE SU SALARIO POR HORA: "))
NUMHT = float(input("INGRESE SU NUMERO DE HORAS TRABAJADAS: "))

SALARMEN = SALARX * NUMHT

if SALARMEN > 450000:
    print(f"Nombre: {NOM}")
    print(f"Salario mensual: {SALARMEN}")
else:
    print(f"Nombre: {NOM}")
