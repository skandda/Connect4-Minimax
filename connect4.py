NUM_ROWS = 6
NUM_COLS = 7
WIN_LENGTH = 4
INF = float('inf')

PLAYER = 'X'
AI = 'O'
EMPTY = '_'

class Connect4:

    def __init__(self, board=[[EMPTY] * 7 for x in range(6)]):
        self.board = board
        self.turn = PLAYER

    def __str__(self):
        board = '\n 0 1 2 3 4 5 6\n'
        for i in range(NUM_ROWS-1, -1, -1):
            board += "|"
            for j in range(NUM_COLS):
                board += "{}|".format(self.board[i][j])
            board += "\n"
        return board
    
    def get_position_value(self, board_position):
        position_value = 0

        ai = board_position.count(AI)
        player = board_position.count(PLAYER)
        empty = board_position.count(EMPTY)

        if ai == 4:
            position_value += 100
        elif ai == 3 and empty == 1:
            position_value += 5
        elif ai == 2 and empty == 2:
            position_value += 2
        if player == 3 and empty == 1:
            position_value -= 4

        return position_value

    def get_board_value(self):
        board_value = 0

        #horizontal
        for row in range(NUM_ROWS):
            row_to_score = self.board[row]
            for col in range(NUM_COLS-3):
                board_to_score = row_to_score[col:col+WIN_LENGTH]
                board_value += self.get_position_value(board_to_score)

        #vertical
        for col in range(NUM_COLS):
            col_to_score = [self.board[r][col] for r in range(NUM_ROWS)]
            for row in range(NUM_ROWS-3):
                board_to_score = col_to_score[row:row+WIN_LENGTH]
                board_value += self.get_position_value(board_to_score)

        #diag_1
        for row in range(NUM_ROWS-3):
            for col in range(NUM_COLS-3):
                board_to_score = [self.board[row+i][col+i] for i in range(WIN_LENGTH)]
                board_value += self.get_position_value(board_to_score)

        #diag_2
        for row in range(NUM_ROWS-3):
            for col in range(NUM_COLS-3):
                board_to_score = [self.board[row+3-i][col+i] for i in range(WIN_LENGTH)]
                board_value += self.get_position_value(board_to_score)

        return board_value
                
    def place(self, row, column, turn):
        self.board[row][column] = turn
    
    def get_row(self, col):
        for row in range(NUM_ROWS):
            if self.board[row][col] == EMPTY:
                return row
            
    def valid_position(self, r, c):
        if r in range(NUM_ROWS) and c in range(NUM_COLS):
            return True
        return False
    
    def valid_column(self, c):
        return False if c not in range(NUM_COLS) or self.board[NUM_ROWS-1][c] != EMPTY else True

    def minimax_max(self, alpha, beta, depth):
        winner = self.check_win()
        max_value = -INF
        best_col = -1

        if winner != None or depth == 0:
            if winner == AI:
                return(INF, None)
            elif winner == PLAYER:
                return (-INF, None)
            elif winner == EMPTY:
                return (0, None)
            elif depth == 0:
                return(self.get_board_value(), None)
            
        for col in range(NUM_COLS):
            if self.valid_column(col):
                row = self.get_row(col)
                self.place(row, col, AI)
                value, column = self.minimax_min(alpha, beta, depth - 1)

                self.board[row][col] = EMPTY

                if value > max_value:
                    max_value = value
                    best_col = col
                if max_value > alpha:
                    alpha = max_value
                if alpha >= beta:
                    break
        return (max_value, best_col)

    def minimax_min(self, alpha, beta, depth):
        winner = self.check_win()
        min_value = INF
        best_col = -1

        if winner != None or depth == 0:
            if winner == AI:
                return(INF, None)
            elif winner == PLAYER:
                return (-INF, None)
            elif winner == EMPTY:
                return (0, None)
            elif depth == 0:
                return(self.get_board_value(), None)
            
        for col in range(NUM_COLS):
            if self.valid_column(col):
                row = self.get_row(col)
                self.place(row, col, PLAYER)
                value, column = self.minimax_max(alpha, beta, depth - 1)

                self.board[row][col] = EMPTY

                if value < min_value:
                    min_value = value
                    best_col = col
                if min_value < alpha:
                    alpha = min_value
                if alpha >= beta:
                    break
        return (min_value, best_col)

    def check_win(self):
        for piece in [AI, PLAYER]:
            for c in range(NUM_COLS-3):
                for r in range(NUM_ROWS):
                    if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                        return piece

            for c in range(NUM_COLS):
                for r in range(NUM_ROWS-3):
                    if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                        return piece

            for c in range(NUM_COLS-3):
                for r in range(NUM_ROWS-3):
                    if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                        return piece

            for c in range(NUM_COLS-3):
                for r in range(3, NUM_ROWS):
                    if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                        return piece
                    
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if self.board[r][c] == EMPTY:
                    return None
        
        return EMPTY
    
    def get_input(self):
        while(True):
            inp = input("Select a column (0 to 6): ")

            if inp in ['0', '1', '2', '3', '4', '5', '6'] and self.valid_column(int(inp)):
                return int(inp)
            else:
                print("Please select a valid column.")
    
    def play(self):
        winner = None
        while winner is None:

            if self.turn == PLAYER:
                print(self)
                col = self.get_input()
                row = self.get_row(col)
                self.place(row, col, PLAYER)
                winner = self.check_win()

            elif self.turn == AI:
                value, col = self.minimax_max(-INF, INF, 5)
                row = self.get_row(col)
                self.place(row, col, AI)
                winner = self.check_win()

            if winner == PLAYER:
                print(self)
                print("You have beaten the AI. Congratulations.")
            elif winner == AI:
                print(self)
                print("You lose! The AI is unbeatable.")
            elif winner == EMPTY:
                print(self)
                print("Tie game.")

            self.turn = PLAYER if self.turn == AI else AI