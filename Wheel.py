# 24 segment wheel

class WheelSegment:

    def __init__(self, value, text, color):
        self.value = value
        self.text = text
        self.color = color

    def getValue(self):
        return self.value

    def getText(self):
        return self.text

    def getColor(self):
        return self.color
