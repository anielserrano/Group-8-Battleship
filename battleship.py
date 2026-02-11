"""
battleship.py
The classic board game battleship
Erin, Aniel, and Malik

"""
zeroes_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
                
                import random

SIZE = 10
LETTERS = ["A","B","C","D","E","F","G","H","I","J"]

WATER = "~"
SHIP = "S"
HIT = "X"
MISS = "M"

SHIP_LENGTHS = [5, 4, 3, 3, 2]


# make empty board
def make_board():
    board = []
    for r in range(SIZE):
        row = []
        for c in range(SIZE):
            row.append(WATER)
        board.append(row)
    return board


# print board
def print_board(board, title):
    print("\n" + title)
    print("    1 2 3 4 5 6 7 8 9 10")
    for r in range(SIZE):
        print(LETTERS[r], end="  ")
        for c in range(SIZE):
            print(board[r][c], end=" ")
        print()


# convert input like B7
def get_pos(text):
    text = text.upper()
    if len(text) < 2:
        return None
    if text[0] not in LETTERS:
        return None
    try:
        col = int(text[1:]) - 1
    except:
        return None
    if col < 0 or col >= SIZE:
        return None
    row = LETTERS.index(text[0])
    return row, col


# auto place ships
def place_ships(board):
    for length in SHIP_LENGTHS:
        placed = False
        while not placed:
            r = random.randint(0, SIZE - 1)
            c = random.randint(0, SIZE - length)
            ok = True
            for i in range(length):
                if board[r][c+i] != WATER:
                    ok = False
            if ok:
                for i in range(length):
                    board[r][c+i] = SHIP
                placed = True


# check win
def won(board):
    for row in board:
        if SHIP in row:
            return False
    return True


# one turn
def turn(name, shots, own, enemy):
    print("\n" + name + " turn")
    print_board(shots, "Shots")
    print_board(own, "Your ships")

    move = input("Enter shot: ")
    pos = get_pos(move)
    if pos is None:
        return

    r, c = pos
    if shots[r][c] != WATER:
        return

    if enemy[r][c] == SHIP:
        shots[r][c] = HIT
        enemy[r][c] = HIT
        print("Hit!")
    else:
        shots[r][c] = MISS
        print("Miss!")


# main game
p1_ships = make_board()
p1_shots = make_board()
p2_ships = make_board()
p2_shots = make_board()

place_ships(p1_ships)
place_ships(p2_ships)

player = 1
while True:
    if player == 1:
        turn("Player 1", p1_shots, p1_ships, p2_ships)
        if won(p2_ships):
            print("PLAYER 1 WINS")
            break
        player = 2
    else:
        turn("Player 2", p2_shots, p2_ships, p1_ships)
        if won(p1_ships):
            print("PLAYER 2 WINS")
            break
        player = 1
