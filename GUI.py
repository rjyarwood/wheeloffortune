# File for the actual GUI

from tkinter import *
import numpy as np
from Board import Board
from QuestionInterface import Question

root = Tk()
root.title("Wheel of Fortune")
root['bg'] = 'deep sky blue'

board = Board(root=root, question=Question(prompt="Town",
                letterloc=np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
                answer="Beloit"))
board.createPromptPanel()
display = board.createBoard()

display.pack(fill=BOTH)

root.mainloop()
