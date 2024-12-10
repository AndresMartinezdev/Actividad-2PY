N1 = int(input())
N2 = int(input())
N3 = int(input())

if N1 > N2 and N1 > N3:
    MAYOR = N1
if N2 > N1 and N2 > N3:
    MAYOR = N2
else:
    MAYOR = N3
    
print(f"El mayor entre N1, N2 y N3 es: {MAYOR}")