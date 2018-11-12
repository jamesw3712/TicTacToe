#class board is incharge of making a move, checking a win, and printing the board
class Board():
    

	def __init__(self, numRows, numCols):
		self.numRows = numRows
		self.numCols = numCols
		self.board = [[" " for x in range(self.numRows)] for x in range(self.numCols)]
	
	
	#public check for win returns -1 if tie 0 if no solution and player num if there is a winner
	def checkForWin(self):
		if self._checkForWin(self.board) != -1: return self._checkForWin(self.board)
		if self._checkForWin(self.getCols()) != -1: return self._checkForWin(self.getCols())
		if self._checkForWin(self.getDiagonals()) != -1: return self._checkForWin(self.getDiagonals())
		if self.isBoardFull(): return -1
		else: return 0
	
	#private helper function to check for a win
	def _checkForWin(self, list):
		for item in list:
			if item[1:] == item[:-1] and not " " in item:
				return 1 if item[0] == "X" else 2
		return -1

	#private function returns columns in board
	def getCols(self):
		cols = [[], [], []]
		for rowIndex in range(0,self.numRows):
			for colIndex in range(0,self.numCols):
				cols[colIndex].append(self.board[rowIndex][colIndex])
		return cols

	#private function returns diagonals from board
	def getDiagonals(self):
		return [[self.board[0][0], self.board[1][1], self.board[2][2]], [self.board[0][2], self.board[1][1], self.board[2][0]]]
	
	#private function returns if the board is full
	def isBoardFull(self):
		for row in self.board:
			if " " in row:
				return False
		return True

	#public function adds move to board
	def addMove(self, row, col, boardValue):
		if self.isMoveValid(row, col) != "":
			return
		row = int(row)-1
		col = int(col)-1
		self.board[row][col] = boardValue

	#public function checks if a move is valid
	def isMoveValid(self, row, col):
		outsideBoardError = "outside board"
		positionTakenError = "position already taken"
		row = int(row)-1
		col = int(col)-1
		if row < 0 or col < 0:
			return outsideBoardError
		if row > self.numRows-1 or col > self.numCols-1:
			return outsideBoardError
		if self.board[row][col] != " ":
			return positionTakenError
		return ""

	#public function prints the board
	def printBoard(self):

		print("+", end = "")
		print(("---+")*self.numCols)

		for currentRow in range(0, self.numRows):
			for currentCol in range(0, self.numCols):
				print("+", end = "") if currentCol == 0 else print(end = "")
				print(" " + str(self.board[currentRow][currentCol]), end = "")
				print(" +") if currentCol == self.numCols-1 else print(" |", end = "")

			print("+", end = "")
			print(("---+")*self.numCols, end = "")
			print("")