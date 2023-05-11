class Board(object):
    def __init__(self):
        self.board = [[' ' for x in range(3)] for y in range(3)] # creates an empty 3x3 board
        
    def __str__(self):
        result = ''
        for row in self.board:
            result += '|'.join(row) + '\n'
        return result
    
    def get_state(self):
        return self.board
    
    def get_field(self, x, y):
        return self.board[x][y]
        
    def set_field(self, move):
        if self.board[move[0]][move[1]] == ' ':
            self.board[move[0]][move[1]] = move[2]
            return True
        else:
            return False

class Player(object):
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_move(self):
        while True:
            x = input(f"{self.name}, please enter the x coordinate of your move (0-2): ")
            y = input(f"{self.name}, please enter the y coordinate of your move (0-2): ")
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                print("Invalid input. Please enter integers between 0 and 2.")
                continue
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Invalid move. Please enter numbers between 0 and 2.")
                continue
            return (x, y, self.sign)


class Move(object):
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign

class Game(object):
    def __init__(self):
        self.board = Board()
        self.current_player = None
        self.winner = None
        
    def play(self, player_one, player_two):
        self.current_player = player_one
        while not self.game_over():
            move = self.current_player.get_move()
            if self.board.set_field(move):
                print(self.board)
                if self.game_over():
                    break
                if self.current_player == player_one:
                    self.current_player = player_two
                else:
                    self.current_player = player_one
            else:
                print("That space is already occupied. Please try again.")
        if self.winner is None:
            print("It's a tie!")
        else:
            print(f"{self.winner.name} wins!")
    
    def game_over(self):
        board = self.board.get_state()
        for i in range(3):
            # check rows
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                self.winner = self.current_player
                return True
            # check columns
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                self.winner = self.current_player
                return True
        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            self.winner = self.current_player
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            self.winner = self.current_player
            return True
        # check for tie
        if self.is_next_move_possible() == False:
            return True
        return False
    
    def is_next_move_possible(self):
        board = self.board.get_state()
        for row in board:
            if ' ' in row:
                return True
        return False
    
def main():
    print("Welcome to Tic-Tac-Toe!")
    name1 = input("Enter player one's name: ")
    name2 = input("Enter player two's name: ")
    player_one = Player(name1, 'X')
    player_two = Player(name2, 'O')
    game = Game()
    print(game.board)
    game.play(player_one, player_two)
    print("Thanks for playing!")

if __name__ == '__main__':
    main()





