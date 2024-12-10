A = int(input())
B = int(input())

def Comparar_orden(A,B):
    if A > B:
        return "A mayor que B"   
    if A == B:
        return "A es igual a B"
    else:
        return "B es mayor que A"
    
    
print(Comparar_orden(A,B))