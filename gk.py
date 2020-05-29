pos = ["Lateral Derecho", "Central", "Lateral Izquierdo",
       "Extremo Izquierdo", "Pivot", "Extremo Derecho"]
gol = ["si", "no"]


def ingreso():
    print("Comenzando el ingreso de lanzamiento...\n")

    nameAct = input("Ingrese nombre de jugador: ")
    print("El nombre ingresado es", nameAct)

    while True:
        print("Ingrese posicion del jugador")
        print("1.Lateral Derecho      2.Central      3.Lateral Izquierdo")
        print("4.Extremo Derecho      5.Pivot        6.Extremo Izquierdo")

        numPos = input()

        if (int(numPos) > 6 or int(numPos) < 1):
            print("Posición incorrecta. Reingresar\n")
        else:
            break
    print("La posicion ingresada es", pos[int(numPos) - 1])

    while True:
        print("¿El lanzamiento fue gol?")
        print("1.Si                2.No")
        numGol = input()

        if numGol != '2' and numGol != '1'):
            print("Incorrecto. Reingresar\n")
        else:
            break

    print ("El lanzamiento " + gol[int(numGol) - 1] + " fue gol")

ingreso()
