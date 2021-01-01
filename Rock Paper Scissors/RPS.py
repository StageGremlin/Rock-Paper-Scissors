import random
import time

# moves = ['Rock','Paper','Scissors', 'Dave']

def moves(list):
    list = []
    n = int(input("Enter number of players: "))
    for i in range(0,n):
        ele = str(input("Enter what you want to play with.: "))

        list.append(ele)
    print(list)

moves(list)
wins = [[2,3],[0],[1],[1,2]]

#move1 = 0(Rock) move2 = 2(scissors)
def beats(move1,move2):
    winningCombos = wins[move1]
    for combo in winningCombos:
        if combo == move2:
            return True
    return False

def findResult(move1,move2):
    if beats(move1,move2):
        return 1
    elif beats(move2,move1):
        return 2
    else:
        return 0

def indexToMove(index):
    return moves[index]
    
def aiMove():
    time.sleep(3)
    selectedMove = random.randint(0,len(moves)-1)
    return selectedMove

def initialToIndex(initial):
    for x in range(0,len(moves)):
        move = moves[x]
        if initial.lower() == move[:1].lower():
            return x
    return False
    
def validateInput(input):
    for move in moves:
        if input.lower() == move[:1].lower():
            return True
    return False 

def userMove():
    validInput = False
    while validInput == False:
        inputMessage = "Enter your move "
        for move in moves: 
            inputMessage += "[" + move[:1].lower() + "]" + move[1:] + " "
        inputMessage += ": "
        userInput = input(inputMessage)
        if validateInput(userInput):
            return initialToIndex(userInput)
        else:
            print("Invalid input. Please try again.")

def getResultMessage(result):
    if result == 1:
        return "AI Wins!"

    elif result == 2:
        return "User Wins!"
    
    elif result == 0:
        return "It's a draw!"
    
    else:
        return "There was an error"

def playAgain ():
    input("Would you like to play again? (y or n): ")
    if "y":
        return play()
    elif "n":
        return None
    else:
        return None

def play():
    print("AI's turn")
    move1 = aiMove()
    print("User's turn")
    move2 = userMove()

    print("AI: " + indexToMove(move1))
    print("User: " + indexToMove(move2))

    print(getResultMessage(findResult(move1,move2))+ "\n")

while True:
    play()