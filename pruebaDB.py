import sqlite3
import random

con = sqlite3.connect('jugadores.sqlite')

c = con.cursor()
rnd1 = random.randint(0, 5)
rnd2 = random.randint(0, 10)
rnd3 = random.randint(0, 10)
rnd4 = random.randint(0, 10)
des = 1     #PRESERVAR
posicionStr = None

def sacar_pos():
    if separado[2] == 0:
        posicionStr = "lateral derecho"
    if separado[2] == 0:
        posicionStr = "central"
    if separado[2] == 2:
        posicionStr = "lateral izquierdo"
    if separado[2] == 3:
        posicionStr = "extremo derecho"
    if separado[2] == 4:
        posicionStr = "pivot"
    if separado[2] == 5:
        posicionStr = "extremo izquierdo"

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tablaJugadores\
            (apellido TEXT,\
            nombre TEXT,\
            posicion INT,\
            lanz_tot INT,\
            lanz_conv INT,\
            lanz_err INT) ")


def dynamic_data_entry():
    c.execute("INSERT INTO tablaJugadores VALUES\
              (?, ?, ?, ?, ?, ?)",
              (apellidoAct, nombreAct, rnd1, rnd2, rnd3, rnd4))
    con.commit()


def add_player(apell, nomb, pos):
    c.execute("INSERT INTO tablaJugadores VALUES\
              (?, ?, ?, 0, 0, 0)",
              (apell, nomb, pos))
    con.commit()


def read_from_db(apell, nomb):
    c.execute("SELECT * FROM tablaJugadores WHERE apellido = ? AND nombre = ?",
              (apell, nomb))
    unido = str(c.fetchall())
    if unido != "[]":
        separado = unido.split(", ")
        # print(separado)
        # print(separado[0].strip("[('")) #Nombre
        # print(separado[1].strip("'"))   #APELLIDO
        # print(separado[2])              #posicion
        # print(separado[3])              #lanz_tot
        # print(separado[4])              #lanz_conv
        # print(separado[5].strip(")]"))  #lanz_esrr
        #sacar_pos()
        print ("Seleccionó al jugador " + separado[0].strip("[('") + ", " +
               separado[1].strip("'") + ". \nRealizó " + separado[3] +
               " lanzamientos de los cuales " + separado[4] + " fueron "
               "goles y " + separado[5].strip(")]") + " no lo fueron.")
        #print("Este jugador juega de " + posicionStr)
    else:
        while True:
            print("No se encontró al jugador " + apell + ", " + nomb)
            print("¿Desea agregar un jugador con ese nombre?")
            des = input("\n1.Sí                                 2.No    ")

            if des == '1':
                print("Ingrese posicion del jugador")
                print("1.Lateral Derecho     2.Central    3.Lateral Izquierdo")
                print("4.Extremo Derecho     5.Pivot      6.Extremo Izquierdo")
                pos = input()
                add_player(apell, nomb, pos)
                break
            elif des == '2':
                print("PIOLA 2")
                break
            else:
                print("Incorrecto. Reingresar")


def del_and_update():
    c.execute('UPDATE tablaJugadores SET lanz_tot = ? \
              AND lanz_conv = ? AND lanz_err = ? WHERE apellido = ?', ())


create_table()

apellidoAct = input("Ingrese apellido del jugador: ")
apellidoAct = apellidoAct.upper()

print("Se guarda como", apellidoAct)

nombreAct = input("Ingrese nombre del jugador: ")
nombreAct = nombreAct.title()

print("Se guarda como", nombreAct)

# c.execute("SELECT * FROM tablaJugadores WHERE apellido = ?",
#           (apellidoAct.lower(),))
# for row in c.fetchall():
#     print(row)

# data_entry()
# dynamic_data_entry()

read_from_db(apellidoAct, nombreAct)


c.close()
con.close()
