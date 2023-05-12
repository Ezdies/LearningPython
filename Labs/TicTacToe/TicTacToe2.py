

class Board(object):
    def __init__(self):
        self.board = [['_' for x in range(3)] for y in range(3)] # creates an empty 3x3 board
        
    def __str__(self):
        return self.get_state()
    
    def get_state(self):
        state = ""
        for row in self.board:
            state += "".join(row) + "\n"
        return state
    
    def get_field(self, x, y):
        return self.board[x][y]
        
    def set_field(self, move):
        if self.get_field(move.x, move.y) != "_":
            print("Pole zajęte")
            return False
        self.board[move.x][move.y] = move.sign
        return True

class Player(object):
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_move(self):
        print("Gracz", self.name)
        
        while True:
            x, y = map(int, input().split())
            try:
                x = int(x)
                y = int(y)
            except ValueError:
                print("Invalid input. Please enter integers between 0 and 2.")
                continue
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Invalid move. Please enter numbers between 0 and 2.")
                continue
            return Move(x, y, self.sign)


class Move(object):
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign

class Game(object):
    def __init__(self):
        self.board = Board()
        self.winning_sign = None
        
    def play(self, player_one, player_two):
        players = (player_one, player_two)
        current_player = 0
        
        
        while not self.game_over():
            while not self.board.set_field(
                players[current_player].get_move()):
                pass
            current_player = (current_player + 1) % 2
            print(self.board)
        
        if self.winning_sign == None:
            print("Remis")
        elif self.winning_sign == player_one.sign:
            print("Wygrał", player_one.name)
        else:
            print("Wygrał", player_two.name)
        
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
        
        for row in range(3):
            if self.board.get_field(row, 0) == \
                    self.board.get_field(row, 1) == \
                    self.board.get_field(row, 2) and \
                    self.board.get_field(row, 0) != '_':
                return True
        
        for col in range(3):
            if self.board.get_field(0, col) == \
                    self.board.get_field(1, col) == \
                    self.board.get_field(2, col) and \
                    self.board.get_field(0, col) != '_':
                return True
        
        if self.board.get_field(0, 0) == \
                    self.board.get_field(1, 1) == \
                    self.board.get_field(2, 2) and \
                    self.board.get_field(0, 0) != '_':
                self.winning_sign = self.board.get_field(0, 0)
                return True
        
        if self.board.get_field(2, 0) == \
                    self.board.get_field(1, 1) == \
                    self.board.get_field(0, 2) and \
                    self.board.get_field(2, 0) != '_':
                self.winning_sign = self.board.get_field(2, 0)
                return True
        if not self.is_next_move_possible():
            self.winning_sign = None
            return True
        return False

    
    def is_next_move_possible(self):
        return "_" in self.board.get_state()
    
def main():
    print("Welcome to Tic-Tac-Toe!")
    name1 = input("Enter player one's name: ")
    name2 = input("Enter player two's name: ")
    player_one = Player(name1, 'X')
    player_two = Player(name2, 'O')
    game = Game()

    game.play(player_one, player_two)
    print("Thanks for playing!")

if __name__ == '__main__':
    main()





