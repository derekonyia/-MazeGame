import sys

import random
import math

''' todo : fuct =>
    MAKE SURE THE BOMB OR EXIT POINT IS NOT [25, 5] == STARTING POINT 
    draw[win, bomb, looser],
    random_exit,
    Help
    '''


def getNewBoard():
    # create a new board 10 X 10 
    board = []
    for x in range(46):
        board.append([])
        for y in range(10):
            if not x % 5:
                board[x].append('.')
            else:
                board[x].append(' ')
            
    return board


def random_bombs(numBombs):
    #  create list of bomb data structures
    bombs = []
    nums = [5, 10, 15, 20, 20, 35, 40]
    while len(bombs) < numBombs:
        newBomb = [nums[random.randint(2, 6)], random.randint(2, 7)]
        if newBomb not in bombs:  # make sure it dosent exist already
            bombs.append(newBomb)
        
    return bombs 

def bombCheck(bomb, cLocation):
    if cLocation in bomb:
        bomb.remove(cLocation)
        return 'you just lost a token'
    else:
        pass
    

def bombLocations(bombs):
    bombs.remove(bombs[(len(bombs))-1])
    return bombs
    

def random_exits(numExits=4):
    #  create list of exit data structures
    exits =[]
    yexits=[2, 3, 4, 5, 6, 7, 8 ]
    xexits=[0,45]
    while len(exits) < numExits:
        newExit = [xexits[random.randint(-0, 1)], yexits[random.randint(-0,6)]]
        if newExit not in exits:  # make sure it dosent exist already
            exits.append(newExit)
    return exits

def exitCheck(cLocation, exits):
    if cLocation in exits:
        return 'you found it'
    else:
        pass

def exitLocations(exits):
    return exits
    

def updateMove(board, move, oldMove):
    
    a, b, *kwargs = oldMove
    x, y, *kwargs = move
    board[a][b] = '.'
    board[x][y] = 'X'
    # for proper spacing of digits, numbers are placed above zero mark
    zeroMarknums = ''
    # initial space for numbers on left side of board
    for i in range(0, 10):
        zeroMarknums += (' ' * 4) + str(i)
    print(zeroMarknums)
##    print('    ' + ('0123456789' * 5))
    print()

    # drawing the grid

    for row in range(10):
        # padding of single digits
        if row < 10:
            extraspace = ' '
        else:
            extraspace = ''

    # printing row

        boadRow = ''
        for column in range(46):
            boadRow += board[column][row]
            
        print(f'{extraspace},{row},{boadRow},{row}')

        
    # printing the numbers across the bottom of the board
    print()
##    print('    ' + ('0123456789' * 5))
    print(zeroMarknums)
    
def constraints(Xmove):
    message = ''
    x, y = Xmove
    if x == 50:
        Xmove = [45, y]
        message = 'invalid move'
    if x == -5:
        Xmove = [0, y]
        message = 'invalid move'
    if y == -1:
        Xmove = [x, 0]
        message = 'invalid move'
    if y == 10:
        Xmove = [x, 9]
        message = 'invalid move'
    else:
        pass
    return Xmove, message
        
def enterPlayerMove(previousMoves, tokens):
    # player enters move
    move = ''
    x, y = previousMoves
    print(' use up(W), down(S), left(A), right(D) to move or use (N)  to quit')
    while True:
        direction = input()
        splitDirection = direction.split()
        if len(splitDirection) >= 2:
            print('take one step at a time')
            continue
        elif direction.lower() == 'w'or's'or'a'or'd' or 'n' or 'b' or 'e':
            if direction.lower() == 'n':
                print('Thanks for playing')
                sys.exit()
            elif direction.lower() == 'b':
                return 'the price you pay is a token'
                move =([x, y])
            elif direction.lower() == 'e':
                return 'the price you pay is double a token' 
                tokens -= 2
                move =([x, y])
            elif direction.lower() == 'w':
                y-=1
                move =([x, y])
            elif direction.lower() == 'a':
                x-=5
                move =([x, y])
            elif direction.lower() == 's':
                y+=1
                move =([x, y])
            elif direction.lower() == 'd':
                x+=5
                move = ([x, y])
            else:
                continue
        
        return move

def lastPreviousMove(previousMoves):
    lastMove = previousMoves[len(previousMoves)-1]
    return lastMove

def oldLocation(previousMoves):
    oldMove = previousMoves[len(previousMoves)-2]
    return oldMove
                
def showInstructions():
    print('''
        Rule of the Game
            1. Initial life token = 5
            2. To move : press W(up), S(down), D(right), A(left)
            3. Special Key
                    a. press B. the bomb locations would be revealed except for 1 for a price(1 token)
                    b. press E. the exit locations would be revealed for a price(2 tokens)
                    c. press N, to quit game
            4. Avoid the bomb. Minus 1 token for each bomb crash
            5, to win, find one of the hidden exits
            HAPPY PLAYING .. :)
        ''')
    input()

    


def listMaker(x, y):
    made = []
    if x == 0:
        x = x
    else:
        x = int(x/5)
    made.append(x)
    made.append(y)
    print (made)
    

print('BLIND MAZE')
print()
print('would you like to view instructions (yes/no)')
if input().lower() == 'yes':
    showInstructions()
        
while True:
    previousMoves = [[25, 5]]
    theBoard = getNewBoard()
    theExits = random_exits()
    theBombs = random_bombs(20)
    displayMoves = []
    tokens = 5
    made = []
    
    while tokens > 0:
        currentTokens = tokens
        lastMove = lastPreviousMove(previousMoves)# provides the last list is the list if previousMoves(current_move)
        x, y = lastMove
        if x == 0:
            x = 0
        else:
            x= int(x/5)
        cLastMove = [x, y]
        displayMoves.append(cLastMove)
        print(displayMoves)
        print(f'you have {tokens} tokens left')
        updateMove(theBoard, lastMove, oldLocation(previousMoves))# updates the board with the current location of X
        if bombCheck(theBombs, lastMove)== 'you just lost a token':
            tokens -=1
            print('b oo OO O MM')
            if tokens == 0:
                print('tokens : 0')
                print('GAME OVER')
                break
        elif exitCheck(lastMove, theExits)== 'you found it':
            print('You won')
            print('would you like to play again ?')
            input()
            if input().lower() == 'yes':
                break
            else:
                sys.exit()
        else:
            try:
                play = enterPlayerMove(lastMove, tokens)
                preMove = constraints(play)
                move = preMove[0]
                message = preMove[1]
                previousMoves.append(move)
                print(message)
            except ValueError as e:
                if play ==  'the price you pay is a token':
                    tokens -= 1
                    if tokens <= 1 :
                        print ('so sorry move cannot be made')
                        tokens = 1
                    else:
                        for x, y in bombLocations(theBombs):       
                            listMaker(x, y) 
                elif play == 'the price you pay is double a token':
                    if tokens <= 2 :
                        print ('so sorry move cannot be made')
                    else:
                       for x, y in exitLocations(theExits):
                           listMaker(x=x, y=y)
                       tokens-=2
                else:
                    continue 
                
        
    
            

