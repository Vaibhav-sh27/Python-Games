from time import sleep
theboard={'7': ' ' , '8': ' ' , '9': ' ' ,
          '4': ' ' , '5': ' ' , '6': ' ' ,
          '1': ' ' , '2': ' ' , '3': ' ' }

print("\t \t Welcome to TicTacToe!")
print()
print("\nTic-tac-toe is a game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.")
sleep(5)
input("Press Enter to Start:")
board_keys=[]
for key in theboard:
    board_keys.append(key)
    
def printboard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print("- + - + -")
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print("- + - + -")
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    
def game():
    
    turn = 'X'
    count = 0
    
    for i in range (10):
        printboard(theboard)
        print("It's", turn, "'s turn, move to where?")
        
        move = input()
         
        if theboard[move] == ' ':
            theboard[move] = turn
            count+=1
        else:
            print("The place is already filled, Please move elsewhere..")
            continue
        if count>=5:
            if theboard['7'] == theboard['8'] == theboard['9']!=' ':
                printboard(theboard)
                print("Game Over.")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['4'] == theboard['5'] == theboard['6']!=' ':
                printboard(theboard)
                print("Game over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['1'] == theboard['2'] == theboard['3']!=' ':
                printboard(theboard)
                print("Game Over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['1'] == theboard['4'] == theboard['7']!=' ':
                printboard(theboard)
                print("Game Over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['2'] == theboard['5'] == theboard['8']!=' ':
                printboard(theboard)
                print("Game Over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['3'] == theboard['6'] == theboard['9']!=' ':
                printboard(theboard)
                print("Game Over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['1'] == theboard['5'] == theboard['9']!=' ':
                printboard(theboard)
                print("Game Over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
            elif theboard['3'] == theboard['5'] == theboard['7']!=' ':
                printboard(theboard)
                print("Game Over. ")
                print("_X_X_X_", turn, "Won the match. _X_X_X_")
                break
        if count == 9:
            print("Game Over. ")
            print("_X_X_X_ It's a Tie _X_X_X_")
            break
                
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            
    restart=input("Do You Want To Start Again? (Y/N) :").upper()
    if restart=="Y":
        for key in board_keys:
            theboard[key] = ' '
            
        game()
if __name__ == "__main__":
    game()
hm= input("Move to Home Page ? (Y/N)").upper()
if hm=="Y":
    from subprocess import call
    call(["python","main.py"])
else:
    input("Press Enter to Leave: ")
                