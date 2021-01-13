player, opponent = "x", "o"


def is_moves_left(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == " ":
                return True
    return False


def evaluate(board):
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10
            elif board[row][0] == opponent:
                return -10

    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10

    return 0


def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == " ":
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = " "
        return best

    else:
        best = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == " ":
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = " "
        return best


def find_best_move(board):
    best_val = -1000
    best_move = (-1, 1)

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == " ":
                board[i][j] = player
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move, best_val


def display_board(board):
    print("Board : \n\t ", board[0][0], " | ", board[0][1], " | ", board[0][2], "\n\t-----------------"
                                                                                "\n\t ", board[1][0], " | ", board[1][1], " | ", board[1][2], "\n\t-----------------"
                                                                                "\n\t ", board[2][0], " | ", board[2][1], " | ", board[2][2])


if __name__ == "__main__":
    tic_toc_toe_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    my_turn = False
    move_val = 0

    while is_moves_left(tic_toc_toe_board):
        if my_turn:
            x = int(input("Enter X : "))
            y = int(input("Enter Y : "))
            tic_toc_toe_board[x][y] = "o"
        else:
            best_moves, move_val = find_best_move(tic_toc_toe_board)
            print("Move : [ Row: ", best_moves[0], ", Col: ", best_moves[1], " ]")
            x = best_moves[0]
            y = best_moves[1]
            tic_toc_toe_board[x][y] = "x"

        my_turn = not my_turn
        display_board(tic_toc_toe_board)
        if move_val == 10:
            print("Computer, wins the match ...!")
            break
        if move_val == -10:
            print("Player, Wins the match ...!")
            break

    if not is_moves_left(tic_toc_toe_board):
        print("Draw ...!")