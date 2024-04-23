class Connect4():
    def __init__(self, grid=[['_'] * 7 for x in range(6)]):
        self.grid = grid
        self.turn = 'R'
        self.infinity = 100000000000000
        
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


    def minimax_max(self, alpha, beta, depth):



            winner = self.check_wins()

            if winner == 'B':
                return()


    
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
            
            if self.turn == "R":

                while(True):

                    col =self.get_input()

                    if self.valid_placement(col):
                        x, y = self.place(col)
                        break
                    else:
                        print("Select a valid column, please.\n")

            elif self.turn == 'B':

                while(True):
                    col = self.get_input()

                    if self.valid_placement(col):
                        x, y = self.place(col)
                        break
                    else:
                        print("Select a valid column, please.\n")
        