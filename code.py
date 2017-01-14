class Code:
    def __init__(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def toDict(self):
        map = {}
        for value in self.code:
            if map.get(value):
                map[value] = map[value] + 1
            else:
                map[value] = 1
        return map