from game import Game
from tkinter import *

def processNewGame(window, e, i, k, players):
    window.destroy()
    if e.get() + i.get() + k.get() == 0:
        popup = Toplevel()
        error = Label(popup, text = "Must choose at least 1 deck")
        error.pack()
        ok = Button(popup, text = "OK", command = lambda: newGameMenu(popup))
        ok.pack()
    # Create deck strings
    numPlayers = ["", "1"]
    if (players.get() >= 3):
        numPlayers.append("3")
        if (players.get() >= 4):
            numPlayers.append("4")
    decks = []
    for x in [(e.get(), "E"), (i.get(), "I"), (k.get(), "K")]:
        if x[0]:
            decks += [x[1]]
    # cross lists
    crossDecks = [x + y for x in numPlayers for y in decks]
    print(crossDecks)
    game = Game(players.get(), crossDecks)  

def newGameMenu(window = None):
    if window != None:
        window.destroy()
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
    finished = Button(popup, text = "OK", command = lambda: processNewGame(popup, eEnabled, iEnabled, kEnabled, players))
    finished.pack()

master = Tk()
newGame = Button(master, text = "New Game", command = newGameMenu)
newGame.pack()

mainloop()
