# File for the actual GUI
from tkinter import *
from Board import Board
from QuestionandAnswerDict import QUESTIONDICTIONARY
from Team import Team
from answerPanel import AnswerPanel

root = Tk()
root.title("Wheel of Fortune")
root['bg'] = 'deep sky blue'

board = Board(root=root, question=QUESTIONDICTIONARY.get(1))

display = board.createBoard()

display.pack(fill=BOTH)
promptPanel = board.promptPanel.pack(fill=BOTH)

Teams = []
def createNewTeam():
    Teams.append(Team(id=newTeamEntry.get()))



AnswerPanel(root=root, board=board)

newTeamButton = Button(root, text="Create New Team", command=createNewTeam)
newTeamButton.pack(side=RIGHT)

newTeamEntry = Entry(root)
newTeamEntry.pack(side=RIGHT)


root.mainloop()
