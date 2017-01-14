import random
import mastermind
import pegDiff

class MastermindSolver:
    def __init__(self, mastermindInstance):
        self.mastermindInstance = mastermindInstance
        self.pegs = []
        self.configurations = []
        self.colorOptions = ['R','G','B','O','W','Y']
        self.matrix = [[[[]]]]

    def generateRandomSequence(self):
        array = []

        for i in range(0, 4):
            array.append(self.colorOptions[random.randint(0, len(self.colorOptions) - 1)])
        return array

    def possibilityMatrix(self):
        for color1 in range(0, len(self.colorOptions)):
            for color2 in range(0, len(self.colorOptions)):
                for color3 in range(0, len(self.colorOptions)):
                    for color4 in range(0, len(self.colorOptions)):
                        self.matrix[color1][color2][color3][color4] = [self.colorOptions[color1], self.colorOptions[color2], self.colorOptions[color3], self.colorOptions[color4]]

    def makeMove(self):
        sequence = self.generateRandomSequence()
        self.configurations.append(sequence)
        self.mastermindInstance.makeMove(sequence)
        print 'Move made: ' + str(sequence) + ' against ' + str(self.mastermindInstance.getAnswerCode()) + ' resulted in ' + str(self.mastermindInstance.getPins())

    def generateSequence(self):
        return self.generateRandomSequence()

mastermindGame = mastermind.Mastermind(['Y', 'O', 'W', 'Y'])
mastermindSolver = MastermindSolver(mastermindGame)
for i in range(0, 10):
    mastermindSolver.makeMove()