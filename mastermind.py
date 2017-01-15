import move
import colors
import code
import pegDiff
import settings
import random

class Mastermind:

    def __init__(self, answerCode):
        self.remainingMoves = settings.DEFAULT_MOVE_COUNT
        self.answerCode = code.Code(answerCode)
        self.colors = colors.Colors()
        self.moves = []
        self.ruleset = pegDiff.PegDiff()
        self.winState = False

    def makeMove(self, compareCode):
        self.remainingMoves -= 1
        self.moves.append(compareCode)
        return self.ruleset.getPegsAsTuple(self.answerCode, compareCode)

    def hasSolution(self):
        return self.getLastMoveDiff()[0] == 4

    def getAnswerCode(self):
        return self.answerCode

    def getRemainingMoveCount(self):
        return self.remainingMoves

    def hasRemainingMove(self):
        return self.remainingMoves > 0

    def getMoveDiff(self, moveNumber):
        return self.ruleset.getPegsAsTuple(self.answerCode, self.moves[moveNumber])

    def getLastMoveDiff(self):
        return self.ruleset.getPegsAsTuple(self.answerCode, self.moves[len(self.moves) - 1])

    def generateRandomCode(self):
        colors = self.colors.getColors()
        generatedCode = []
        for i in range(len(self.answerCode.getCode())):
            generatedCode.append(colors[random.randint(0, len(colors) - 1)])
        return code.Code(generatedCode)


mastermind = Mastermind(['Y', 'B', 'G', 'Y'])
while mastermind.hasRemainingMove():
    generatedCode = mastermind.generateRandomCode()
    print 'Generated ' + str(generatedCode.getCode()) + ' against ' + str(mastermind.getAnswerCode().getCode())
    print 'Move resulted in ' + str(mastermind.makeMove(generatedCode))
print 'Game complete'
