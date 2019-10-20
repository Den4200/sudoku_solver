# Sudoku Solver w/Backtracking Algorithm

class Sudoku:

    def __init__(self, board):
        self.board = board

    def solve(self):
        find = self.find_empty()

        if not find:
            self.print_board()
            return True
        else:
            y, x = find

        for i in range(1, 10):
            if self.is_valid(i, (y, x)):
                self.board[y][x] = i

                if self.solve():
                    return True

                self.board[y][x] = 0

        return False

    def is_valid(self, num, pos):
        
        # Validate row
        for x in range(len(self.board[0])):
            if self.board[pos[0]][x] == num and pos[1] != x:
                return False

        # Validate column
        for y in range(len(self.board)):
            if self.board[y][pos[1]] == num and pos[0] != y:
                return False 

        # Validate square
        sq_x = pos[1] // 3
        sq_y = pos[0] // 3

        for y in range(sq_y * 3, sq_y * 3 + 3):
            for x in range(sq_x * 3, sq_x * 3 + 3):
                if self.board[y][x] == num and (y, x) != pos:
                    return False

        # Everything checks out
        return True

    def print_board(self):
        for y in range(len(self.board)):
            if y % 3 == 0 and y != 0:
                print('-----------------------')

            for x in range(len(self.board[0])):
                if x % 3 == 0 and x != 0:
                    print(' | ', end='')

                if x == 8:
                    print(self.board[y][x])
                else:
                    print(str(self.board[y][x]) + ' ', end='')

    def find_empty(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == 0:
                    return (y, x)

        return None

def main(board):
    s = Sudoku(board)
    s.solve()

if __name__ == "__main__":

    b = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
    ]

    main(b)
