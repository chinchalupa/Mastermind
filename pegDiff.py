import code

class PegDiff:
    def getPegsAsTuple(self, code, compareCode):
        blackPegs = self.getBlackPegs(code, compareCode)

        return blackPegs, self.getColorDiffCount(code, compareCode) - blackPegs

    def getBlackPegs(self, code, compareCode):
        blackPegs = 0
        for i in range(len(code.getCode()) - 1):
            if code.getCode()[i] == compareCode.getCode()[i]:
                blackPegs += 1
        return blackPegs

    def getColorDiffCount(self, code, compareCode):
        diff = 0
        for value in code.toDict():
            if compareCode.toDict().get(value):
                diff += min(compareCode.toDict().get(value), code.toDict().get(value))
        return diff