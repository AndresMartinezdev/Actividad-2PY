A = float(input())
B = float(input())
C = float(input())

def ESFERA_MAYOR(A, B, C):
    if A > B and A > C:
        return "La esfera de mayor peso es A"
    elif B > A and B > C:
        return "La esfera de mayor peso es B"
    else:
        return "La esfera de mayor peso es C"

resultado = ESFERA_MAYOR(A, B, C)
print(resultado)
