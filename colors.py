import settings

class Colors:
    def __init__(self):
        self.colors = settings.COLORS

    def getColors(self):
        return self.colors

    def getColorDict(self):
        map = {}
        for i in range(len(self.colors)):
            map[i] = self.colors[i]
        return map