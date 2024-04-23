class Connect4():
    def __init__(self, grid=[['_'] * 7 for x in range(6)]):
        self.grid = grid
        self.turn = 'R'
        self.infinity = 8
        
    def __str__(self):
        board = '\n 0 1 2 3 4 5 6\n'

        for i in range(6):
            board += "|"
            for j in range(7):
                board += "{}|".format(self.grid[i][j])
            board += "\n"
            
        return board
    
    def valid_placement(self, col):
        return False if (col < 0 or col > 6 or self.grid[0][col] != '_') else True

    def place(self, col):
        for slot in range(5, -1, -1):
            if self.grid[slot][col] == "_":
                self.grid[slot][col] = self.turn
                return (slot, col)
            
    def check_wins(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for sign in [-1, 1]:
                r, c = row, col
                while True:
                    r += sign * dr
                    c += sign * dc
                    if 0 <= r < 6 and 0 <= c < 7 and self.grid[r][c] == self.turn:
                        count += 1
                    else:
                        break
                if count >= 4:
                    return self.turn
        for r in range(6):
            for c in range(7):
                if self.grid[r][c] == "_":
                    return None
            
        return "_"
    
    def get_input(self):

        while(True):
            inp = input("Select a column (0 to 6): ")

            if inp in ['0', '1', '2', '3', '4', '5', '6']:
                return int(inp)
            else:
                print("Please select a valid input.")

    def minimax_max(self, alpha, beta, depth, coords):

        print(depth)

        max_value = -self.infinity

        coord_x, coord_y = coords

        best_col = -1

        if alpha >= beta:
            return (alpha, best_col)
        
        winner = self.check_wins(coord_x, coord_y)
        if winner != None or depth == 0:
            if winner != None:
                if winner == "B":
                    return (-self.infinity + depth, 0)
                elif winner == "R":
                    return (self.infinity - depth, 0)
                elif winner == "_":
                    return (0, 0)
            else:
                return (0, 0)

        
        for i in range(0, 7):
            if self.valid_placement(i):
                
                x, y = self.place(i)

                (value, min_col) = self.minimax_min(alpha, beta, depth - 1, (x, y))

                if value > max_value:
                    max_value = value
                    best_col = i

                self.grid[x][y] = "_"

                if max_value > alpha:
                    alpha = max_value
                
        return (alpha, best_col)
    
    def minimax_min(self, alpha, beta, depth, coords):

        min_value = self.infinity

        coord_x, coord_y = coords

        best_col = -1

        if alpha >= beta:
            return (alpha, best_col)
        
        winner = self.check_wins(coord_x, coord_y)

        if winner != None or depth == 0:
            if winner != None:
                if winner == "B":
                    return (-self.infinity + depth, 0)
                elif winner == "R":
                    return (self.infinity - depth, 0)
                elif winner == "_":
                    return (0, 0)
            else:
                return (0, 0)
        
        for i in range(0, 7):
            if self.valid_placement(i):
                x, y = self.place(i)

                (value, max_col) = self.minimax_max(alpha, beta, depth - 1, (x, y))

                if value < min_value:
                    max_value = value
                    best_col = i

                self.grid[x][y] = "_"

                if min_value < beta:
                    beta = min_value
                
        return (alpha, best_col)

    
    def play(self, x=0, y=0):

        while True:

            print(self)
            winner = self.check_wins(x, y)

            if winner != None:
                if winner == 'R':
                    print ("Red won.")
                elif winner == 'B':
                    print ("Blue won.")
                elif winner == '_':
                    print ("Tie game.")

                return
            
            if self.turn == 'R':
                self.turn = "B"
            else:
                self.turn = "R"
            
            #get turns

            if self.turn == "B":
                while(True):

                    col = self.get_input()

                    if self.valid_placement(col):
                        x, y = self.place(col)
                        break
                    else:
                        print("Select a valid column, please.\n")

            elif self.turn == 'R':

                while(True):

                    (value, max_col) = self.minimax_max(-self.infinity, self.infinity, 1, (0, 0))

                    if self.valid_placement(max_col):
                        x, y = self.place(max_col)
                        break
                    else:
                        print("Select a valid column, please.\n")
        