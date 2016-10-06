# Helper function to unzip the rows, columns, diagonals for checking the state function
def unzip_mtx(board_mtx):

    eval_mtx = []

    for i in range(len(board_mtx)):
        a = [a[i] for a in board_mtx]
        eval_mtx.append(a) # --> mtx columns
        eval_mtx.append(board_mtx[i]) # --> mtx rows

    # mtx diagonals
    diagonal_a = [board_mtx[0][0], board_mtx[1][1], board_mtx[2][2]]
    diagonal_b = [board_mtx[0][2], board_mtx[1][1], board_mtx[2][0]]
    eval_mtx.append(diagonal_a)
    eval_mtx.append(diagonal_b)
    return eval_mtx    
    

# Checkt the result of the game
# Count the different symbols and check the tie state
def check_result(mtx):
    
    counter_tie = 0
    #print "initial: ", counter_tie #for debugging
    for i in mtx:
        counter_tie += i.count(0)
        if i.count('X') == 3:
            print "The winner is Player X"
            print "Congrat!"
            return 1
        elif i.count('O') == 3:
            print "The winner is Player O"
            print "Congrat!"
            return 1
        else:
            pass    
    #print "The number of remain step(s): ", counter_tie # for debugging
    if counter_tie == 0:
            print "The tie is tie no tale!"
            print "No winner!"
            return 1

#Draw the board function with print statements

def board_print():
    print ('-------------')
    print  "| " +  str(game_mtx[0][0]) + " | " + str(game_mtx[0][1]) + " | " + str(game_mtx[0][2]) + " |"
    print ('-------------')
    print  "| " +  str(game_mtx[1][0]) + " | " + str(game_mtx[1][1]) + " | " + str(game_mtx[1][2]) + " |"
    print ('-------------')
    print  "| " +  str(game_mtx[2][0]) + " | " + str(game_mtx[2][1]) + " | " + str(game_mtx[2][2]) + " |"
    print ('-------------')




# initial the playboard mtx
game_mtx = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]


# Player 1
def player_x():

    print "Lets play!"

    
    n = (raw_input("X movement: "))

    coordinate_x = n.split(',')
    coordinate_x = [int(a) for a in coordinate_x]
    if game_mtx[coordinate_x[0]][coordinate_x[1]] == 0:
        game_mtx[coordinate_x[0]][coordinate_x[1]] = 'X'
        #print game_mtx
        board_print()
        if check_result(unzip_mtx(game_mtx)) != 1:
            player_o()
        else:
            print "Game Over"
    else:
        print "There is already used cell."
        print "Please give an another coordinate"
        #print game_mtx
        board_print()
        player_x()

#Player 2
def player_o():

    n = (raw_input("O movement: "))

    coordinate_o = n.split(',')
    coordinate_o = [int(a) for a in coordinate_o]
    if game_mtx[coordinate_o[0]][coordinate_o[1]] == 0:
        game_mtx[coordinate_o[0]][coordinate_o[1]] = 'O'
        #print game_mtx
        board_print()
        #check_result(unzip_mtx(game_mtx))
        if check_result(unzip_mtx(game_mtx)) != 1:
            player_x()
        else:
            print "Game Over"
            
    else:
        print "There is already used cell."
        print "Please give an another coordinate"
        #print game_mtx
        board_print()
        player_o()


player_x()

