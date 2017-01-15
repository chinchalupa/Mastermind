import random
import mastermind
import pegDiff

class MastermindSolver:



mastermindGame = mastermind.Mastermind(['Y', 'O', 'W', 'Y'])
mastermindSolver = MastermindSolver(mastermindGame)
for i in range(0, 10):
    mastermindSolver.makeMove()