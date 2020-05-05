# File for the actual GUI

from tkinter import *
import Board

root = Tk()
root.title("Wheel of Fortune")
root['bg'] = 'deep sky blue'

board = Board.createBoard(root)
board.pack(fill=BOTH)

prompt = Board.createPromptPanel(root)
prompt.pack(fill=BOTH)

root.mainloop()
