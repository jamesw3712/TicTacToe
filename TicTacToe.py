#James Warda CS 474 UIC Computer Science Fall 2018
#import board class which handles board opperations such as checking for a win and making a move
from Board import Board


def main():
	playAgain = "y"
	
	while playAgain.lower() == 'y':
		b = Board(3,3)
		print("Type the row and column in which you wish to move")
		gameResult = playGame(b)

		if gameResult == -1:
			playAgain = input("Tie Game!  Play again? (y/n): ")
		else:
			playAgain = input("Player " + str(gameResult) + " Wins! Play again? (y/n) ")
	
	print("Goodbye!")

#function runs the game loop until player has won or tie
def playGame(board):
	numTurns = 0

	while True:
		board.printBoard()
		numTurns += 1
		player = 1 if numTurns % 2 != 0 else 2
		playerPiece = 'X' if player == 1 else 'O'
		userInput = getPlayerInput(numTurns, board, player, playerPiece)
		board.addMove(userInput[0], userInput[1], userInput[2])
		print("")
		if board.checkForWin() != 0:#if a player has won or tie
			board.printBoard()
			return board.checkForWin()
		
#function gets the users next move		
def getPlayerInput(turn, board, player, playerPiece):

	userInput = input("Turn " + str(turn) + ": Player " + str(player) + " (" + playerPiece + "), choose your move: ")
	
	while True:
		userInput = userInput.strip()
		userInput = userInput.split(" ")
		
		if len(userInput) != 2:
			userInput = input("Invlaid move, only enter two integers seperated by a space, try again: ")
		elif board.isMoveValid(userInput[0], userInput[1]) != "":
			userInput = input("Invlaid move, " + board.isMoveValid(userInput[0], userInput[1]) + ", try again: ")
		else:
			userInput.append(playerPiece)
			return userInput


if __name__ == '__main__':
	main()







