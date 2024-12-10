Codigo_Empleado = int(input())
Nombre_Empleado = input()
Horas_trabajadas_al_mes = int(input())
Valor_Hora_trabajada = float(input())
Retencion_fuente = float(input())

Porcentaje_de_retencion = Retencion_fuente / 100

Salario_bruto = Horas_trabajadas_al_mes * Valor_Hora_trabajada
Salario_Neto = Salario_bruto - Porcentaje_de_retencion

print(f"Código:{Codigo_Empleado}")
print(f"Nombre: {Nombre_Empleado}")
print(f"Salario bruto: {Salario_bruto}")
print(f"Salario neto: {Salario_Neto}")