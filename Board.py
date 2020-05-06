# Actual Board
from tkinter import *
import tkinter.font as tk

class Board:

    BOARDBACKGROUND = 'deep sky blue'
    font = tk.Font(size=50)
    NULLLABEL = 'light sea green'
    EMPTYLABEL = 'white'


    def __init__(self, root, question):
        self.root = root
        self.question = question

    def createBoard(self):

        board = Frame(self.root, bg=self.BOARDBACKGROUND)


        # Row 1 Character Entries
        coord0_0 = Label(board, bg=self.EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_0.grid(row=0, column=1)

        coord0_1 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_1.grid(row=0, column=2)

        coord0_2 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_2.grid(row=0, column=3)

        coord0_3 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_3.grid(row=0, column=4)

        coord0_4 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_4.grid(row=0, column=5)

        coord0_5 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_5.grid(row=0, column=6)

        coord0_6 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_6.grid(row=0, column=7)

        coord0_7 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_7.grid(row=0, column=8)

        coord0_8 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_8.grid(row=0, column=9)

        coord0_9 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_9.grid(row=0, column=10)

        coord0_10 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_10.grid(row=0, column=11)

        coord0_11 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord0_11.grid(row=0, column=12)

        # Row 2 character entries

        coord1_0 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_0.grid(row=1, column=0)

        coord1_1 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_1.grid(row=1, column=1)

        coord1_2 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_2.grid(row=1, column=2)

        coord1_3 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_3.grid(row=1, column=3)

        coord1_4 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_4.grid(row=1, column=4)

        coord1_5 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_5.grid(row=1, column=5)

        coord1_6 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_6.grid(row=1, column=6)

        coord1_7 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_7.grid(row=1, column=7)

        coord1_8 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_8.grid(row=1, column=8)

        coord1_9 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_9.grid(row=1, column=9)

        coord1_10 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_10.grid(row=1, column=10)

        coord1_11 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_11.grid(row=1, column=11)

        coord1_12 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_12.grid(row=1, column=12)

        coord1_13 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord1_13.grid(row=1, column=13)

        # Row 3

        coord2_0 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_0.grid(row=2, column=0)

        coord2_1 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_1.grid(row=2, column=1)

        coord2_2 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_2.grid(row=2, column=2)

        coord2_3 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_3.grid(row=2, column=3)

        coord2_4 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_4.grid(row=2, column=4)

        coord2_5 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_5.grid(row=2, column=5)

        coord2_6 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_6.grid(row=2, column=6)

        coord2_7 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_7.grid(row=2, column=7)

        coord2_8 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_8.grid(row=2, column=8)

        coord2_9 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_9.grid(row=2, column=9)

        coord2_10 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_10.grid(row=2, column=10)

        coord2_11 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_11.grid(row=2, column=11)

        coord2_12 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_12.grid(row=2, column=12)

        coord2_13 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord2_13.grid(row=2, column=13)

        # Row 4

        coord3_0 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_0.grid(row=3, column=1)

        coord3_1 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_1.grid(row=3, column=2)

        coord3_2 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_2.grid(row=3, column=3)

        coord3_3 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_3.grid(row=3, column=4)

        coord3_4 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_4.grid(row=3, column=5)

        coord3_5 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_5.grid(row=3, column=6)

        coord3_6 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_6.grid(row=3, column=7)

        coord3_7 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_7.grid(row=3, column=8)

        coord3_8 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_8.grid(row=3, column=9)

        coord3_9 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_9.grid(row=3, column=10)

        coord3_10 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_10.grid(row=3, column=11)

        coord3_11 = Label(board, bg=EMPTYLABEL, bd=3, relief=SUNKEN, width=1, height=1, font=font)
        coord3_11.grid(row=3, column=12)

        return board


    def createPromptPanel(self):

        promptPanel = Frame(self.root)

        BACKGROUND = 'midnight blue'

        prompt = Label(promptPanel, bg=BACKGROUND, text="currentPrompt", fg='white')
        prompt.pack(fill=BOTH)

        return promptPanel
