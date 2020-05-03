import pprint, random

print('Welcome to Noughts and Crosses')
print('Do you want to be an X or O?')
XorO = input()

while XorO != 'X' and XorO !='O':
    print('Enter X or O only')
    XorO = input()

print('The computer will go first.')
if XorO == 'X':
    comIcon = 'O'
else:
    comIcon = 'X'

theBoard = {'low-L': ' ', 'low-M': ' ' , 'low-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'top-L':' ', 'top-M':' ', 'top-R': ' '}
# theBoard['low-M'] = comIcon

PositionsUsed = []
positions = list(theBoard.keys())
checker = False
check = False
check1 = False

def ComputersPositions(Board,Icon):
    comPos = random.randint(0, 8)
    
    if len(PositionsUsed) == 0:
        Board[positions[comPos]] = Icon
    else:
        while comPos in PositionsUsed:
            comPos = random.randint(0, 8)
        Board[positions[comPos]] = Icon
    PositionsUsed.append(comPos)    

def UserMove(XO):
    print('What is your move? (top-, mid-, low- & L, M, R)')
    userPosistion = input()
    theBoard[userPosistion] = XO
    userPos = positions.index(userPosistion)
    PositionsUsed.append(userPos)
    

def printBoard(theBoard):
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('------')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('------')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])



##theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X'
##theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X'
##theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X'
##
##theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X'
##theBoard['low-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['top-R'] == 'X'
##
##theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X'
##theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X'
##theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X'


markers = [XorO, comIcon]
moves = []

def checkForWin(moves, markers, comIcon,theBoard):
    moves = list(theBoard.values())
    indicator=''
    for icon in markers:
        winCheck = moves[0:3] 
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[3:6] 
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[6:9] 
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[2:7:2]
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[0:9:4]
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[0:7:3]
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[1:8:3]
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        winCheck = moves[2:9:3]
        if icon not in winCheck and ' ' not in winCheck:
            indicator = icon
            break
        
    
    if indicator == XorO:
        print('Computer Wins!')
        checker = True
        return checker
    elif indicator == comIcon:
        printBoard(theBoard)
        print('You win! Congratulations!')
        checker = True
        return checker
        
    


while check1 != True: 
    ComputersPositions(theBoard, comIcon)
    printBoard(theBoard)
    check = checkForWin(moves, markers, comIcon, theBoard)
    if check == True:
        break
    UserMove(XorO)
    check1 = checkForWin(moves, markers, comIcon, theBoard)
    
    





##theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O'
##theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O'
##theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O'
##theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O'
##theBoard['low-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['top-R'] == 'O'
##theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O'
##theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O'
##theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O'



##ComputersPositions(theBoard, comIcon)
##printBoard(theBoard)
##UserMove(XorO)
##ComputersPositions(theBoard, comIcon)
##printBoard(theBoard)
##UserMove(XorO)
##ComputersPositions(theBoard, comIcon)
##printBoard(theBoard)


##print(theBoard)pprint.pprint(theBoard)

# theBoard['low-L'] = 'X'
# theBoard['top-M'] = 'O'
# pprint.pprint(theBoard)




