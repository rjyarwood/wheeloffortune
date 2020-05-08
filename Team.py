
class Team:

    def __init__(self, id):
        self.id = id
        self.score = 0
        self.currency = 0

    def getID(self):
        return self.id

    def getScore(self):
        return self.score

    def getCurrency(self):
        return self.currency
