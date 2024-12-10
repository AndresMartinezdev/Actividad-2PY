PESOA = float(input())
PESOB = float(input())
PESOC = float(input())
PESOD = float(input())

if (PESOA == PESOB) or (PESOA == PESOC):
    if PESOD > PESOA:
        print("LA ESFERA D ES LA DIFERENTE Y ES DE MAYOR PESO")
    else:
        print("LA ESFERA D ES LA DIFERENTE Y ES DE MENOR PESO")
elif (PESOA == PESOB) and (PESOA == PESOD):
    if PESOC > PESOA:
        print("LA ESFERA C ES LA DIFERENTE Y ES DE MAYOR PESO")
    else:
        print("LA ESFERA C ES LA DIFERENTE Y ES DE MENOR PESO")
elif (PESOA == PESOC) and (PESOA == PESOD):
    if PESOB > PESOD:
        print("LA ESFERA B ES LA DIFERENTE Y ES DE MAYOR PESO")
    else:
        print("LA ESFERA B ES LA DIFERENTE Y ES DE MENOR PESO")
else:
    if PESOA > PESOB:
        print("LA ESFERA A ES LA DIFERENTE Y ES DE MAYOR PESO")
    else:
        print("LA ESFERA A ES LA DIFERENTE Y ES DE MENOR PESO")
