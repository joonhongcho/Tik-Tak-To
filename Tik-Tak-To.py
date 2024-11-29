def intro():
    print(' 1 | 2 | 3 ')
    print(' 4 | 5 | 6 ')
    print(' 7 | 8 | 9 ')
    Press_Y=input('''\nEnter 'Y' to start.\n''')
    if Press_Y=='y' or Press_Y=='Y':
        print('Game Start')
        loby()
    else:
        close=print('\nClose')

def loby():
    select=int(input("\n1. Play Game\n2. Change Board\n3. Match History\n"))
    if select==1:
        game_play()
    elif select==2:
        change_board()
    elif select==3:
        match_history()

show_board=1

def change_board():
    global show_board
    print('1.                2.                     3.         ')
    print(' X | ○ |          ┌───┬───┬───┐           X ┃ ○ ┃   ')
    print('   |   |          │ X │ ○ │   │          ━━━╋━━━╋━━━')
    print('   |   |          ├───┼───┼───┤             ┃   ┃   ')
    print("                  │   │   │   │          ━━━╋━━━╋━━━")
    print("                  ├───┼───┼───┤             ┃   ┃   ")
    print("                  │   │   │   │                     ")
    print("                  └───┴───┴───┘                     ")
    while True:
        selected_board=int(input('Select Board\n'))
        if selected_board==1:
            print('Board Selected!')
            show_board=1
            break
        elif selected_board==2:
            print('Board Selected!')
            show_board=2
            break
        elif selected_board == 3:
            print('Board Selected!')
            show_board =3
            break
        else:
            print("Try again.")
    loby()

empty=' '

board=['fake',empty,empty,empty,empty,empty,empty,empty,empty,empty]

def print_board_1():
    print(' {0} | {1} | {2} '.format(board[1],board[2],board[3]))
    print(' {0} | {1} | {2} '.format(board[4],board[5],board[6]))
    print(' {0} | {1} | {2} '.format(board[7],board[8],board[9]))

def print_board_2():
    print('┌───┬───┬───┐')
    print('│ {0} │ {1} │ {2} │'.format(board[1],board[2],board[3]))
    print('├───┼───┼───┤')
    print('│ {0} │ {1} │ {2} │'.format(board[4],board[5],board[6]))
    print('├───┼───┼───┤')
    print('│ {0} │ {1} │ {2} │'.format(board[7],board[8],board[9]))
    print('└───┴───┴───┘')

def print_board_3():
    print(" {0} ┃ {1} ┃ {2} ".format(board[1],board[2],board[3]))
    print("━━━╋━━━╋━━━")
    print(" {0} ┃ {1} ┃ {2} ".format(board[4],board[5],board[6]))
    print("━━━╋━━━╋━━━")
    print(" {0} ┃ {1} ┃ {2} ".format(board[7],board[8],board[9]))

def print_board():
    global show_board
    if show_board==1:
        print_board_1()
    elif show_board==2:
        print_board_2()
    elif show_board==3:
        print_board_3()

def P1_turn():
    print('Turn='+P1)
    while True:
        P1_decision=int(input('Enter (1~9) to place.\n'))
        if P1_decision>=1 and P1_decision<=9 and board[P1_decision]==empty:
            board[P1_decision]='○'
            break
        else:
            print('Try again.')
    print_board()

def P2_turn():
    print('Turn='+P2)
    while True:
        P2_decision=int(input('Enter (1~9) to place.\n'))
        if P2_decision>=1 and P2_decision<=9 and board[P2_decision]==empty:
            board[P2_decision]='X'
            break
        else:
            print('Try again.')
    print_board()

win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]

win_result = None

def P1_win():
    global win_result
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == '○':
            print(P1+' Win!')
            win_result=P1

def P2_win():
    global win_result
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == 'X':
            print(P2+' Win!')
            win_result=P2

def tie():
    global win_result
    if empty not in board:
        print('Tie')
        win_result='tie'

def again():
    while True:
        print('\nDo you wanna play again?\n1. Play again\n2. Go to Loby\n3. Exit')
        again=int(input())
        if again==1:
            print('Game Start!')
            game_play()
            break
        elif again==2:
            loby()
            break
        elif again==3:
            print('Exit')
            break
        else:
            print('Try again')

def game_play():
    global win_result
    global board
    win_result=None
    board=['fake',empty,empty,empty,empty,empty,empty,empty,empty,empty]
    player_name()
    print_board()
    turn=P1
    while True:
        if turn==P1:
            tie()
            if win_result=='tie':
                match_save()
                break
            P1_turn()
            P1_win()
            if win_result==P1:
                match_save()
                break
            turn=P2
        elif turn==P2:
            tie()
            if win_result=='tie':
                match_save()
                break
            P2_turn()
            P2_win()
            if win_result==P2:
                match_save()
                break
            turn=P1
    again()

P1=None
P2=None

def player_name():
    global P1
    global P2
    if P1!=None and P2!=None:
        pass
    else:
        P1=input("\nEnter P1\'s name:\n")
        print('P1='+P1+'\n')
        while True:
            P2=input('Enter P2\'s name:\n')
            if P2==P1:
                print("Can't use same name.")
            else:
                print('P2='+P2+'\n')
                break

def match_history():
    f=open('C:/Temp/Tik-Tak-To/Match History.txt','a')
    f.close()
    f=open('C:/Temp/Tik-Tak-To/Match History.txt','r')
    print(f.read())
    f.close()
    loby()

import datetime
def match_save():
    time_save=time.asctime(time.localtime(time.time()))
    save_win=time_save+'\n'+P1+' VS '+P2+'\nresult='+win_result+' Win!\n'
    save_tie=time_save+'\n'+P1+' VS '+P2+'\nresult=Tie\n'
    p=open('C:/Temp/Tik-Tak-To/Match History.txt','a')
    if win_result==P1 or win_result==P2:
        p.write(save_win)
        p.close()
    elif win_result=='tie':
        p.write(save_tie)
        p.close()
intro()