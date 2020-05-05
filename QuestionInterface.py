
class Question:

    def __init__(self, prompt, answer, letterloc):
        self.prompt = prompt
        self.answer = answer
        self.letterLoc = letterloc

    def getPrompt(self):
        return self.prompt

    def getAnswer(self):
        return self.answer

    def getLetterLoc(self):
        return self.letterLoc
