class TicTacToe():
    def __init__(self):
        self.game_state = [[None for _ in range(3)] for _ in range(3)]
        self.y_coor = {
            'A': 0,
            'B': 1,
            'C': 2,
        }
        self.turn = 'X'
        self.move = ''
        self.x = None
        self.y = None

    def promptUserInput(self):
        self.move = input(f"\nEnter a coordinate to place {self.turn}: ")

    def isValidInput(self):
        if len(self.move) == 2:
            if self.move[0].isalpha() and self.move[1].isnumeric():
                self.x = int(self.move[1]) - 1
                self.y = self.y_coor[self.move[0].upper()]
                return True
        return False

    def isValidGameState(self):

        if self.game_state[self.x][self.y] is None:
            self.game_state[self.x][self.y] = self.turn
            return True
        else:
            return False

    def updateTurn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def printGameState(self):
        print('\n  --A-------B-------C-----')
        for row in range(3): # Row
            print(f"{row + 1}|", end='')
            for col in range(3): #Col
                if self.game_state[row][col] is None:
                    print(f"\t \t", end='')
                else:
                    print(f"\t{self.game_state[row][col]}\t", end='')

                if col != 2:
                    print("|", end='')

            if row != 2:
                print('\n  ------------------------')
    def isWin(self):
        if self.isWinRow() or self.isWinCol() or self.isWinDiag():
            return True
        else:
            return False

    def isWinRow(self):
        for item in self.game_state[self.x]:
            if item != self.turn:
                return False
        else:
            return True

    def isWinCol(self):
        for x in range(3):
            if self.game_state[x][self.y] != self.turn:
                return False
        else:
            return True

    def isWinDiag(self):
        left_diag = True
        right_diag = True
        for i in range(3):
            if left_diag == True:
                if self.game_state[i][i] != self.turn:
                    left_diag = False
            if right_diag == True:
                if self.game_state[2-i][2-i] != self.turn:
                    right_diag = False
        if left_diag or right_diag == True:
            return True
        else:
            return False

    def resetGameState(self):
        self.game_state = [[None for _ in range(3)] for _ in range(3)]
        self.turn = 'X'

t = TicTacToe()
while(True):
    t.printGameState()
    t.promptUserInput()
    if t.isValidInput():
        if t.isValidGameState():
            if t.isWin():
                print("You Win!")
                t.resetGameState()
                if input("Play Again? (y): ").lower() != 'y':
                    break
                continue
            t.updateTurn()
        else:
            print("Invalid placement")
    else:
        print("Invalid input")





