import random
import os
os.environ['LINES'] = '40'
os.environ['COLUMNS']= '80'


##HERE IS THE BOARD - YOU CAN EDIT IT TO CHANGE THE LAYOUT OF THE ROOMS, POSITIONS OF MONSTERS AND POSITIONS OF HEALING SHRINES
layout='''___________________________________________________________________________
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXX      XXXXXXXXXXXXX      A        XXXXXXXXXXXXX       ?    X      XXX|
|XXXX   O  XXXXXXXXXXXXX               XXXXXXXXXXXXX  XXXXXXXX  X  B   XXX|
|XXXX                                  XXXXXXXXXX      XXXXXXX         XXX|
|XXXX      XXXXXXXXXXXXX                               XXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXX               XXXXXXXXXX   C  XXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXXXX|
|XXXXXX                 XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX   ?    XXXXX|
|XXXXXX  XXXXX  XXXX    XXXXXX  XXXXXXXXXXXXXXXXX      XXXXXX        XXXXX|
|XXXXXX  XXXXX  XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXX  D   XXXXXXXXXXXX  XXXXX|
|XXXXXX  XXXXX                                         XXXX          XXXXX|
|XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXX     XXXXXXXXXX|
|XXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXX|
|XXXXXX       E       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXX|
|XXXXXXXXXXXXXX   F                                             XXXXXXXXXX|
|XXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
|-------------------------------------------------------------------------|
'''


## THESE GLOBAL VARIABLE DECIDE THE MONSTER AND PLAYER HIT POINTS
global health
health =  {"O":20,"A":20,"B":20,"C":20,"D":20,"E":20,"F":20}
global monsters
monsters = ['A','B','C','D','E','F']

def genBoard():
    '''This function generates the board - do not change it'''
    board = []
    row = []
    for i in layout:
        row.append(i)
        if i == '\n':
            board.append(row)
            row = []

    return board

def printBoard(board):
    '''This function prints the board - do not change it'''
    for row in board:
        for character in row:
            print(character, end=" ")

def playerTurn(board):
    '''This function decides on players actions - you could potentially add more actions in here'''
    action = input('What do you want to do ')
    if action in ['w','a','s','d']:
        move(board,'O',action)
    elif action == "attack":
        action = input ("who do you want to attack ")
        if action.upper() in monsters:
            fightMonster(board,"O",action.upper())
    return board

# finish this function so that the hero can be moved by using keys
def move(board,object_,direction):
    try:
        if direction == "w":
            if checkmove(object_,[postions[object_][0][0]-1,postions[object_][0][1]]):
                board[postions[object_][0][0]][postions[object_][0][1]] = " "
                postions[object_][0][0] -= 1
                board[postions[object_][0][0]][postions[object_][0][1]] = object_
            else:
                raise NameError('Invaild move')
        
        elif direction == "a":
            if checkmove(object_,[postions[object_][0][0],postions[object_][0][1]-1]):
                board[postions[object_][0][0]][postions[object_][0][1]] = " "
                postions[object_][0][1] -= 1
                board[postions[object_][0][0]][postions[object_][0][1]] = object_
            else:
                raise NameError('Invaild move')
        
        elif direction == "s":
            if checkmove(object_,[postions[object_][0][0]+1,postions[object_][0][1]]):
                board[postions[object_][0][0]][postions[object_][0][1]] = " "
                postions[object_][0][0] += 1
                board[postions[object_][0][0]][postions[object_][0][1]] = object_
            else:
                raise NameError('Invaild move')
        
        else:
            if checkmove(object_,[postions[object_][0][0],postions[object_][0][1]+1]):
                board[postions[object_][0][0]][postions[object_][0][1]] = " "
                postions[object_][0][1] += 1
                board[postions[object_][0][0]][postions[object_][0][1]] = object_
            else:
                raise NameError('Invaild move')
    except NameError:
        print ("Invaild move, try again")
        
def checkmove(item,new_location):
    if new_location in postions[" "] or new_location in postions["?"]:
        return True
    return False
        
def moveMonsters(board):
    '''This function moves monsters around the board'''
    movelist = []
    altlist = []
    for monster in monsters:
        vaildmoves = []
        number_moves = []
        vaildmoves.append(checkmove(monster,[postions[monster][0][0]-1,postions[monster][0][1]]))
        vaildmoves.append(checkmove(monster,[postions[monster][0][0]+1,postions[monster][0][1]]))
        vaildmoves.append(checkmove(monster,[postions[monster][0][0],postions[monster][0][1]-1]))
        vaildmoves.append(checkmove(monster,[postions[monster][0][0],postions[monster][0][1]+1]))
        if postions["O"][0][0] in range(postions[monster][0][0]-1,postions[monster][0][0]+1) and postions["O"][0][1] in range(postions[monster][0][1]-1,postions[monster][0][1]+1):
            print("ON TOP LE LENNY")
        elif postions["O"][0][0] in range(postions[monster][0][0]-3,postions[monster][0][0]+3) and postions["O"][0][1] in range(postions[monster][0][1]-4,postions[monster][0][1]+4):
            print("INRAGE")
            if postions["O"][0][0] < postions[monster][0][0]:
                if vaildmoves[0] == True:
                    movelist.append(0)
                elif vaildmoves[1] == True:
                    altlist.append(1)
            elif postions["O"][0][0] > postions[monster][0][0]:
                if vaildmoves[0] == True:
                    altlist.append(0)
                elif vaildmoves[1] == True:
                    movelist.append(1)
                
            if postions["O"][0][1] < postions[monster][0][1]:
                if vaildmoves[2] == True:
                    movelist.append(2)
                elif vaildmoves[3] == True:
                    altlist.append(3)
            elif postions["O"][0][1] > postions[monster][0][1]:
                if vaildmoves[2] == True:
                    altlist.append(2)
                elif vaildmoves[3] == True:
                    movelist.append(3)
            print(movelist)
            print (altlist)
            if len(movelist) > 0:
                moveobject(movelist[0],monster,board)
            elif len(altlist) > 0:
                moveobject(altlist[0],monster,board)
            
        else:
            move = random.randint(0,3)
            start_move = move
            try:
                print("outrange")
                while vaildmoves[move] != True:
                    print(move)
                    print(start_move)
                    print(validmoves[move])
                    if start_move == move:
                        raise NameError('Invaild move')
                        return
                    move = (move +1) %4
                print(move)
                moveobject(move,monster,board)
            except:
                pass

def moveobject (movedir,thing,board):
    board[postions[thing][0][0]][postions[thing][0][1]] = " "
    postions[" "].append([postions[thing][0][0],postions[thing][0][1]])
    if movedir == 0:                                  
        postions[thing][0][0] -=1
    elif movedir == 1:
        postions[thing][0][0] +=1 # postions[thing][0][int(((movedir*(movedir-1))*3/2)%2)] += (((movedir%2)*2)-1)
    elif movedir == 2:
        postions[thing][0][1] -= 1
    else:                                          
        postions[thing][0][1] += 1
    if not ([postions[thing][0][0],postions[thing][0][1]] in postions[" "]):
        print([postions[thing][0][0],postions[thing][0][1]])
        print(board[postions[thing][0][0]][postions[thing][0][1]])
        print(postions[" "])
    board[postions[thing][0][0]][postions[thing][0][1]] = thing
    postions[" "].remove([postions[thing][0][0],postions[thing][0][1]])
    
def getObjectPosition(board,object1):
    '''Finds specific objects on the board'''
    for y,row in enumerate(board):
        for x, thing in enumerate(row):
            if thing == object1:
                print(thing)
                position = [y,x]
    return position


def checkSquare(board,newPosition):
    'checks what is in a square'''
    square = board[newPosition[0]][newPosition[1]]
    return(square)

# finish this function so the hero "O" can fight the monsters
def fightMonster(board,attacker,defender):
    print(health[defender])
    rep = False   
    if abs(postions[attacker][0][0] - postions[defender][0][0]) <= 1 and abs(postions[attacker][0][1] - postions[defender][0][1]) <= 1:
        print("AYYYYYYYYYY")
        if attacker == "O":
           damage = random.randint(2,7)
           if health[defender] > 0:
               rep = True
        else :
            damage = 1
            
        print(str(attacker) + " hit " + str(defender) + " for " + str(damage) + " points of damage (tons)")
        health[defender] -= damage
        if health[defender] <= 0:
            postions.pop(defender, None)
            if defender == "O":
                print("You have been defeated")
                exit()
        if rep == True:
            fightMonster(board,defender,attacker)
        
    else:
        print("Too far away")
def startlocations (board):
    items = ['A','B','C','D','E','F','O','X',' ', "?"]
    locations = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'O':[],'X':[],' ':[],"?": []}
    for item in items:
        for x_value,x in enumerate(board):
            for y_value,y in enumerate(x):
                if y == item:
                    locations[item].append([x_value,y_value])
    return locations

    
def mainLoop():
    '''Runs the game'''
    while True:
        board = board1
        printBoard(board)
        startlocations (board)
        playerTurn(board)
        moveMonsters(board)
#        print('\n'*100)
        
board1 = genBoard()
global postions
postions = startlocations (board1)
mainLoop()
# also doesn't update blank spaces and ? are not blank
