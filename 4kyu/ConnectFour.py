# Connect Four
# Take a look at wiki description of Connect Four game:

# Wiki Connect Four

# The grid is 6 row by 7 columns, those being named from A to G.

# You will receive a list of strings showing the order of the pieces which dropped in columns:

#   pieces_position_list = ["A_Red",
#                           "B_Yellow",
#                           "A_Red",
#                           "B_Yellow",
#                           "A_Red",
#                           "B_Yellow",
#                           "G_Red",
#                           "B_Yellow"]
# The list may contain up to 42 moves and shows the order the players are playing.

# The first player who connects four items of the same color is the winner.

# You should return "Yellow", "Red" or "Draw" accordingly.

#SOLUTION HERE
#The Code is lengthy but i wanted to make sure the 
#code is easy to read and solution is error proof :) :)

def positions(pieces_position_list):
    pos = [[] for _ in range(7)]
    column_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
    for piece in pieces_position_list:
        letter, colour = piece.split("_")
        index= column_map[letter]
        pos[index].append(colour)
    for i in range(7):
        while len(pos[i]) < 6: 
            pos[i].append("Empty")
    return pos

def check_vertical(pos, colour):
    for i in range(7):
        for j in range(3):
            if(pos[i][j]==pos[i][j+1]==pos[i][j+2]==pos[i][j+3]==colour):
                return True
    return False

def check_horizontal(pos, colour):
    for j in range(6):
        for i in range(4):
            if(pos[i][j]==pos[i+1][j]==pos[i+2][j]==pos[i+3][j]==colour):
                return True
    return False

def check_diagonal(pos,colour):
    for i in range(4):
        for j in range(3):
            if(pos[i][j]==pos[i+1][j+1]==pos[i+2][j+2]==pos[i+3][j+3]==colour):
                return True
    for i in range(6, 2, -1):
        for j in range(3):
            if(pos[i][j]==pos[i-1][j+1]==pos[i-2][j+2]==pos[i-3][j+3]==colour):
                return True
    return False

def who_is_winner(pieces_position_list):
    # Your code here!
    _, first = pieces_position_list[0].split("_")
    if (first=="Red"): second="Yellow"
    elif (first=="Yellow"): second="Red"
    
    temp_board=[]
    for piece in pieces_position_list:
        temp_board.append(piece)
        pos = positions(temp_board)
        
        if (check_vertical(pos, first)==True): return first
        elif (check_horizontal(pos, first)==True): return first
        elif (check_diagonal(pos, first)==True): return first
    
        elif (check_vertical(pos, second)==True): return second
        elif (check_horizontal(pos, second)==True): return second
        elif (check_diagonal(pos, second)==True): return second

    else: return "Draw"
        
    
    

    
    
    
    pass