import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()

#  ------------------------------  LISTADO DE METODOS  ------------------------------  #


def JugadoresElegidos(numJugadores):

    Inicio.destroy()
    InicioBotones.destroy()

    def Ganador(numJugadores):

        ListadoFinal = []
        participante = 0

        while participante < numJugadores:

            exec("ListadoFinal.append(getJugador{}.get())".format(participante + 1))
            participante += 1

        Jugadores.destroy()

        ganadorFinal = str(random.choice(ListadoFinal))

        textoParaGanador = tk.Label(MostrarGanador, text = "El ganador (o perdedor) es...", font = ('Verdana', 22), bg = "white")
        textoParaGanador.grid(row = 0, column = 0)
        
        elGanador = tk.Label(MostrarGanador, text = ganadorFinal, font = ('Verdana', 28), fg = "green", bg = "white")
        elGanador.grid(row = 1, column = 0)

        for i in ListadoFinal:
            if i.lower() == "el desarrollador":

                sorpresa = tk.Label(MostrarGanador, text = "El desarrolador siempre gana :)", font = ('Verdana', 28), fg = 'blue', bg = 'white')
                sorpresa.grid(row = 0, column = 0)

                textoParaGanador.destroy()
                elGanador.destroy()
    
    rr = 0
    cc = 0
    elem = 1

    while elem <= numJugadores:

        exec('labelJugador{}.grid(row = {}, column = {}, pady = 4)'.format(elem, rr, cc))

        cc += 1

        exec('entryJugador{}.grid(row = {}, column = {}, pady = 4)'.format(elem, rr, cc))

        rr += 1
        cc = 0
        elem += 1

    botonGanador = tk.Button(Jugadores, text = 'Mostrar al Ganador', command = lambda:Ganador(numJugadores))
    botonGanador.config(bg = "green",fg = "white", font = (None, 12), relief = "flat", overrelief = "flat", activebackground = "green")
    botonGanador.grid(row = rr, column = cc, columnspan = 2, pady = 20)


#  ------------------------------  CONFIGURACION ROOT  ------------------------------  #


root.title("Hola Suerte!")
root.iconbitmap("C:/Users/Usuario/Desktop/HolaSuerte/icono.ico")

barra_menu = tk.Menu(root)
root.config(menu = barra_menu, bg = 'white')
root.geometry('900x600')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


#  ------------------------------  BARRA SUPERIOR  ------------------------------  #


def Info_desarrollador():
    messagebox.showinfo("Información del Desarrollador", "Email:       alvarez.fing@gmail.com\nGitHub:   Mateoac12")

def Info_aplicacion():
    messagebox.showinfo("Información de la Aplicación", "Pensada para reuniones de amigos o debates en el hogar. Por ejemplo " + 
    "debatir quien va a pagar en una reunión o quien lavará los platos esta noche. Devuelve un participante de forma aleatoria, salvo que te llames 'el Desarrollador'...")


menu_opciones = tk.Menu(barra_menu, tearoff = 0)
menu_opciones.add_command(label = 'Sobre el Desarrollador', command = lambda:Info_desarrollador())
menu_opciones.add_command(label = 'Sobre la Aplicación', command = lambda:Info_aplicacion())

barra_menu.add_cascade(label = 'Información', menu = menu_opciones)


#  ------------------------------  LISTADO DE FRAMES  ------------------------------  #


Inicio = tk.Frame(root)
Inicio.grid(row = 0, column = 0)
Inicio.config(bg = 'white')



InicioBotones = tk.Frame(Inicio)
InicioBotones.grid(row = 2, column = 0)
InicioBotones.config(bg = 'white')



Jugadores = tk.Frame(root)
Jugadores.grid(row = 0, column = 0, pady = 40)
Jugadores.config(bg = 'white')



MostrarGanador = tk.Frame(root)
MostrarGanador.grid(row = 0, column = 0)
MostrarGanador.config(bg = 'white')


#  ------------------------------  CONSTRUCCION DE LOS WIDGETS  ------------------------------  #

logotipo = tk.PhotoImage(file = 'C:/Users/Usuario/Desktop/HolaSuerte/HolaSuerteLogo.png')

miLogo = tk.Label(Inicio, image = logotipo, bg = 'white')
miLogo.grid(row = 0, column = 0, padx = 20, pady = 20)

info = '¡Haz Click en el número de participantes y que comiencen los nervios!'
infoLabel = tk.Label(Inicio, text = info, bg = 'white', font = ('Verdana', 12))
infoLabel.grid(row = 1, column = 0, pady = 20, padx = 20)

numJugador = 1
jugadoresTotales = 13

while numJugador <= jugadoresTotales:

    exec('getJugador{} = tk.StringVar()'.format(numJugador))
    
    exec('labelJugador{} = tk.Label(Jugadores, text = "Integrante {}:", justify = tk.CENTER, bg = "white", font = ("Verdana", 12))'.format(numJugador, numJugador))

    exec('entryJugador{} = tk.Entry(Jugadores, textvariable = getJugador{}, font = ("Verdana", 12))'.format(numJugador, numJugador))

    numJugador += 1

r = 2
c = 0
boton = 2
botonesTotales = jugadoresTotales

while boton <= botonesTotales:

    exec('boton{} = tk.Button(InicioBotones, text = "{}", command = lambda:JugadoresElegidos({}))'.format(boton, boton, boton))

    exec('boton{}.config(bg = "lightgrey", font = (None, 20), relief = "flat", overrelief = "flat", activebackground = "lightgrey", width = 2)'.format(boton))

    if c == 6:

        r += 1
        c = 0

    exec('boton{}.grid(row = {}, column = {}, padx = 10, pady = 10)'.format(boton, r, c))

    boton += 1
    c += 1


root.mainloop()