edad =  int(input("Cuantos años tienes : "))
distancia = int(input("Distancia a recorrer : "))

if 6<=edad and edad<=18:
    if distancia<=20:
        print(1.50)
    else:
        print(2.50)
else:
    if distancia<=20:
        print(2.50)
    else:
        print(4.00)

