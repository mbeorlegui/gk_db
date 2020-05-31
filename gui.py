from tkinter import *
import sqlite3

# Init sql
con = sqlite3.connect('jugadores.sqlite')
c = con.cursor()

# Init windows
window = Tk()
window.title("GK 1.0")
window.geometry('410x400')

# Set labels
ins_ape = Label(window, text="Ingrese apellido")
ins_ape.grid(column=0, row=0)
ins_nom = Label(window, text="Ingrese nombre")
ins_nom.grid(column=0, row=1)
ape = Label(window, text="Apellido")
ape.grid(column=0, row=3)
nom = Label(window, text="Nombre")
nom.grid(column=0, row=4)
pos = Label(window, text="Posicion")
pos.grid(column=0, row=5)
lanz_tot = Label(window, text="Lanzamientos totales")
lanz_tot.grid(column=0, row=6)
lanz_conv = Label(window, text="Lanzamientos convertidos")
lanz_conv.grid(column=0, row=7)
lanz_err = Label(window, text="Lanzamientos errados")
lanz_err.grid(column=0, row=8)


# Set entrys
ape_e = Entry(window, width=15)
ape_e.grid(column=1, row=0, padx=5)
nom_e = Entry(window, width=15)
nom_e.grid(column=1, row=1, padx=5)

def sacar_pos(pos):
    if pos == 1:
        posicionStr = "Lateral derecho"
    if pos == 2:
        posicionStr = "Central"
    if pos == 3:
        posicionStr = "Lateral izquierdo"
    if pos == 4:
        posicionStr = "Extremo derecho"
    if pos == 5:
        posicionStr = "Pivot"
    if pos == 6:
        posicionStr = "Extremo izquierdo"
    return posicionStr


def query():
    con = sqlite3.connect('jugadores.sqlite')
    c = con.cursor()
    c.execute("SELECT * FROM tablaJugadores")
    lista = c.fetchall()
    # print ("Seleccionó al jugador " + str(lista[0]) + ", " +
    #        str(lista[1]) + ". \nRealizó " + str(lista[2]) +
    #        " lanzamientos de los cuales " + str(lista[3]) + " fueron "
    #        "goles y " + str(lista[4]) + " no lo fueron.")

    mostrarDatos = ''
    for ls in lista:
        mostrarDatos += str(ls[0]) + ", " + str(ls[1]) + "\
         " + str(ls[2]) + " " + str(ls[3]) + " " + str(ls[4]) + "\n"

    query_label = Label(window, text=mostrarDatos)
    query_label.grid(row=13, column=0, columnspan=2)

    con.commit()
    con.close()


def submit():
    c.execute("SELECT * FROM tablaJugadores WHERE apellido = ? AND nombre = ?",
              (ape_e.get().upper(), nom_e.get().title()))
    lista = c.fetchone()
    if not lista:
        print("Lista vacia")
        while True:
            print("No se encontró al jugador ", ape_e.get(), ", ", nom_e.get())
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
    else:
        print("Lista NO vacia")
        print("Seleccionó al jugador " + str(lista[0]) + ", " +
              str(lista[1]) + ". \nRealizó " + str(lista[3]) + 
              " lanzamientos de los cuales " + str(lista[4]) +
              " fueron goles y " + str(lista[5]) + " no lo fueron.")

        pos = sacar_pos(lista[2])

        show_ape = Label(window, text=str(lista[0]))
        show_ape.grid(column=1, row=3)
        show_nom = Label(window, text=str(lista[1]))
        show_nom.grid(column=1, row=4)
        show_pos = Label(window, text=pos)
        show_pos.grid(column=1, row=5)
        show_tot = Label(window, text=str(lista[3]))
        show_tot.grid(column=1, row=6)
        show_con = Label(window, text=str(lista[4]))
        show_con.grid(column=1, row=7)
        show_err = Label(window, text=str(lista[5]))
        show_err.grid(column=1, row=8)



    con.commit()
    con.close()

    ape_e.delete(0, END)
    nom_e.delete(0, END)

query_btn = Button(window, text="Mostrar todos los datos", command=query)
query_btn.grid(row=10, column=0, columnspan=2)

search_btn = Button(window, text="Buscar", command=submit)
search_btn.grid(row=0, column=2)

window.mainloop()
