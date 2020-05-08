from tkinter import *
import tkinter.font as tk

class AnswerPanel:

    def enterKeyPress(self, event):
        self.checkForLetter(letter=self.getLetter())

    def __init__(self, root, board):
        self.root = root
        self.guessedLetters = StringVar()
        self.guessedLetters.set(" ")
        self.Board = board
        self.font = tk.Font(family="Arial", size=30, weight=tk.BOLD)
        self.answerbox = Entry(root, bg='snow', font=self.font, relief=FLAT, width=2, justify=CENTER)
        self.answerbox.bind('<Return>', self.enterKeyPress)
        self.answerbox.pack()
        self.GuessedPanel = Label(root, bg=board.PROMPTBACKGROUND, font=self.font, relief=SUNKEN,
                                  textvariable=self.guessedLetters, justify=LEFT)
        self.GuessedPanel.pack(fill=BOTH)

    def getLetter(self):
        return self.answerbox.get()

    def checkForLetter(self, letter):
        answer = self.Board.question.getAnswer()
        found = False
        count = 0

        for char in answer:
            if char == letter:
                found = True
                print("found")
                print(letter)
                print(count)
                self.updateBoard(count=count, letter=letter)
            else:
                print("Not Correct")

            count += 1

        if not found:
            self.guessedLetters.set(self.guessedLetters.get() + " " + letter)

    def updateBoard(self, count, letter):
        letterLoc = self.Board.question.getLetterLoc().copy()
        x = 0
        y = 0
        for row in letterLoc:
            y = 0
            for cell in row:
                if cell == self.Board.EMPTYLABEL:
                    if count == 0:
                        (self.Board.solutionVar[x][y]).set(letter)
                        break
                    else:
                        count -= 1
                y += 1
            x += 1

        self.Board.root.update()
