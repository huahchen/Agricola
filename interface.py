from game import Game
from tkinter import *

def processNewGame(window):
    window.destroy()

def newGameMenu():
    popup = Toplevel()
    players = IntVar()
    players.set(1)
    numPlayers = OptionMenu(popup, players, 1, 2, 3, 4, 5)
    numPlayers.pack()
    eEnabled = IntVar()
    iEnabled = IntVar()
    kEnabled = IntVar()
    e = Checkbutton(popup, text = "E", variable = eEnabled)
    i = Checkbutton(popup, text = "I", variable = iEnabled)
    k = Checkbutton(popup, text = "K", variable = kEnabled)
    e.pack()
    i.pack()
    k.pack()
    finished = Button(popup, text = "OK", command = lambda: processNewGame(popup))
    finished.pack()

master = Tk()
newGame = Button(master, text = "New Game", command = newGameMenu)
newGame.pack()

mainloop()
