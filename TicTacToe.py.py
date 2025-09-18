import numpy as np
import random

board = np.array([ [" "," "," "],
                   [" "," "," "],
                   [" "," "," "]
                ])

FilledCellsBlocked = np.array([])


def DisplayBoard():
    for i in range(3):
        print("----------------------")
        
        for j in range(3):
            print("|"," ",board[i,j]," ",end="")
        print("|")
    print("----------------------")


def SetSymbol(boxnum,Symbol):
    global FilledCellsBlocked
    if boxnum == 1:
        board[0,0] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 2:
        board[0,1] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 3:
        board[0,2] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 4:
        board[1,0] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 5:
        board[1,1] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 6:
        board[1,2] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 7:
        board[2,0] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 8:
        board[2,1] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
        
    if boxnum == 9:
        board[2,2] = Symbol
        FilledCellsBlocked = np.append(FilledCellsBlocked, boxnum)
    
def EasyMode():
    randomBox = random.randint(1,10)
    
    if randomBox not in FilledCellsBlocked:
        SetSymbol(randomBox,"O")

    
    else:
        while randomBox in FilledCellsBlocked:
            randomBox = random.randint(1,10)
            
        SetSymbol(randomBox,"O")


def MediumMode():
    global FilledCellsBlocked
    randomBox = random.randint(1,10)
    
    if SeizetheOpportunity("O","O"):
        pass
    elif SeizetheOpportunity("X","O"):
        pass
    else:
        if randomBox not in FilledCellsBlocked:
            SetSymbol(randomBox, "O")


        else:
            while randomBox in FilledCellsBlocked:
                randomBox = random.randint(1, 10)

            SetSymbol(randomBox, "O")


## check your chances of winning then, look for opportunuity for opponent to win,if none then randomly place symbol
def SeizetheOpportunity(player_symbol,opponent_symbol):
    if board[0,0] == player_symbol and board[0,1]== " " and board[0,2]==player_symbol:
        SetSymbol(2,opponent_symbol)
        return True
        
    elif board[1,0] == player_symbol and board[1,1]== " " and board[1,2]==player_symbol:
        SetSymbol(5,opponent_symbol)
        return True
    elif board[2,0] == player_symbol and board[2,1]== " " and board[2,2]==player_symbol:
        SetSymbol(8,opponent_symbol)
        return True
        
    
    elif board[0,0] == player_symbol and board[0,1]== player_symbol and board[0,2]==" ":
        SetSymbol(3,opponent_symbol)
        return True
    elif board[1,0] == player_symbol and board[1,1]== player_symbol and board[1,2]==" ":
        SetSymbol(6,opponent_symbol)
        return True
    elif board[2,0] == player_symbol and board[2,1]== player_symbol and board[2,2]==" ":
        SetSymbol(9,opponent_symbol)
        return True
    
    
    elif board[0,0] == " " and board[0,1]== player_symbol and board[0,2]==player_symbol:
        SetSymbol(1,opponent_symbol)
        return True
    elif board[1,0] == " " and board[1,1]== player_symbol and board[1,2]==player_symbol:
        SetSymbol(4,opponent_symbol)
        return True
    elif board[2,0] == " " and board[2,1]== player_symbol and board[2,2]==player_symbol:
        SetSymbol(7,opponent_symbol)
        return True
    
    
    elif board[0,0] == " " and board[0,1]== player_symbol and board[0,2]==player_symbol:
        SetSymbol(1,opponent_symbol)
        return True
    elif board[1,0] == " " and board[1,1]== player_symbol and board[1,2]==player_symbol:
        SetSymbol(4,opponent_symbol)
        return True
    elif board[2,0] == " " and board[2,1]== player_symbol and board[2,2]==player_symbol:
        SetSymbol(7,opponent_symbol)
        return True
    
    
    elif board[0,0] == player_symbol and board[1,0]==" " and board[2,0]==player_symbol:
        SetSymbol(4,opponent_symbol)
        return True
    elif board[0,1] == player_symbol and board[1,1]==" " and board[2,1]==player_symbol:
        SetSymbol(5,opponent_symbol)
        return True
    elif board[0,2] == player_symbol and board[1,2]==" " and board[2,2]==player_symbol:
        SetSymbol(6,opponent_symbol)
        return True
    
    
    elif board[0,0] == " " and board[1,0]==player_symbol and board[2,0]==player_symbol:
        SetSymbol(1,opponent_symbol)
        return True
    elif board[0,1] == " " and board[1,1]==player_symbol and board[2,1]==player_symbol:
        SetSymbol(2,opponent_symbol)
        return True
    elif board[0,2] == " " and board[1,2]==player_symbol and board[2,2]==player_symbol:
        SetSymbol(3,opponent_symbol)
        return True
        
    
    elif board[0,0] == player_symbol and board[1,0]==player_symbol and board[2,0]==" ":
        SetSymbol(7,opponent_symbol)
        return True
    elif board[0,1] == player_symbol and board[1,1]==player_symbol and board[2,1]==" ":
        SetSymbol(8,opponent_symbol)
        return True
    elif board[0,2] == player_symbol and board[1,2]==player_symbol and board[2,2]==" ":
        SetSymbol(9,opponent_symbol)
        return True
        
    
    
    elif board[0,0] == player_symbol and board[1,1]==player_symbol and board[2,2]==" ":
        SetSymbol(9,opponent_symbol)
        return True
    
    elif board[0,0] == player_symbol and board[1,1]==" " and board[2,2]==player_symbol:
        SetSymbol(5,opponent_symbol)
        return True
    
    elif board[0,0] == " " and board[1,1]==player_symbol and board[2,2]==player_symbol:
        SetSymbol(1,opponent_symbol)
        return True
        
        
    elif board[0,2] == player_symbol and board[1,1]==player_symbol and board[2,0]==" ":
        SetSymbol(7,opponent_symbol)
        return True
    
    elif board[0,2] == player_symbol and board[1,1]==" " and board[2,0]==player_symbol :
        SetSymbol(5,opponent_symbol)
        return True
    
    elif board[0,2] == " " and board[1,1]==player_symbol and board[2,0]==player_symbol :
        SetSymbol(3,opponent_symbol)
        return True
    
    else:
        return False
    
    
    
    
    
def CheckforPattern(symbol):
    if board[0,0] == symbol and board[0,1]==symbol and board[0,2]==symbol:
        return True    
    elif board[1,0] == symbol and board[1,1]==symbol and board[1,2]==symbol:
        return True
    elif board[2,0] == symbol and board[2,1]==symbol and board[2,2]==symbol:
        return True
        
  
        
    elif board[0,0] == symbol and board[1,0]==symbol and board[2,0]==symbol:
        return True
    elif board[0,1] == symbol and board[1,1]==symbol and board[2,1]==symbol:
        return True
    elif board[0,2] == symbol and board[1,2]==symbol and board[2,2]==symbol:
        return True
    
    
    elif board[0,0] == symbol and board[1,1]==symbol and board[2,2]==symbol:
        return True
    elif board[0,2] == symbol and board[1,1]==symbol and board[2,0]==symbol:
        return True
            

def RunComputerAlgorithm(mode_num):
    if mode_num == 1:
        EasyMode()
        
    if mode_num == 2:
        MediumMode()
#     if mode_num == 3:
#         HardMode()
    
def PlayGame():
    global FilledCellsBlocked
    DisplayBoard()
   
    print("Please choose a mode to play:")
    
    
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")

    while True:
        try:
            Modes_Selector = int(input("Please type 1,2 or 3 for Easy,Medium or Hard"))
            print()
            if Modes_Selector <1 or Modes_Selector> 3:
                print("Please select a number between 1 and 3 only")
                print()
                continue
            break
        except ValueError:
            print("Invalid input, Please enter a number between 1 and 3")
            print()


    isFull = np.all(board!=" ")
    
    while not isFull:        
        while True:
            try:
                Box_Selector = int(input("Please select a number between 1 and 9"))
                if (Box_Selector < 1 or Box_Selector > 9):
                    continue
                
                else:
                    if Box_Selector in FilledCellsBlocked:
                        print("This cell has been occupied, please choose another cell")
                        print()
                        continue
                    else:
                        break
            
            except:
                print("Invalid input, Please enter a number between 1 and 3")
        
        SetSymbol(Box_Selector,"X")
        FilledCellsBlocked = np.append(FilledCellsBlocked,Box_Selector)
        
        
        isFull = np.all(board!=" ")
        DisplayBoard()
        
        PPattern = CheckforPattern("X")
        
        if PPattern:
            print("Player 1 wins!")
            break
        else:
            pass
        
        if isFull:
            break


        
        else:
            RunComputerAlgorithm(Modes_Selector)
            DisplayBoard()
            CPattern = CheckforPattern("O")
            if CPattern:
                print("Computer wins!")
                break
            else:
                pass
        

        
        isFull = np.all(board!=" ")

choice = "y"
while choice!="n":
    PlayGame()
    try:
        while True:
            choice = input("Please enter y for a new game and n to quit")
            choice.lower()
            if choice == "y" or choice == "n":
                break
            else:
                print("Choose between y and no only, y for a new game, n to quit")
                continue

        if choice=="y":
            board.fill(" ")
            FilledCellsBlocked = np.array([])
            PlayGame()

        if choice=="n":
            print("Thanks for playing our game!")
            break



    except ValueError:
        print("Invalid Input, please type in y for new game and n to quit")






            
    
    

        