# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self) -> None:
        self.board = ["*"] * 9

    def __str__(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n---------\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n---------\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def make_move(self, char, index):
        if self.board[index] == "*":
            self.board[index] = char
        else:
            return None
        
    def clear(self):
        self.board = ["*"] * 9

    def has_won(self, char):

        # check horizontal
        for i in range(0,3):
            if self.board[0 + i * 3] == self.board[1 + i * 3] == self.board[2 + i * 3] and self.board[0 + i * 3] == char:
                return True
        
        # check vertical
        for i in range(0,3):
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i] and self.board[0 + i] == char:
                return True
            
        # check diagonal
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] == char:
                return True
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] == char:
                return True
        
        return False

    def game_over(self):
        
        if self.has_won("X") or self.has_won("O") or "*" not in self.board:
            return True

        
        return False




def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)

        while True:
            try:
                move: str = input(f"Player {players[turn]} what is your move? ")
                #assert int(move) == int

                if int(move) not in (0,1,2,3,4,5,6,7,8):
                    raise ValueError

                if brd.board[int(move)] != "*":
                    raise ValueError
                    
            except ValueError:
                print("Enter a valid index.")
                continue
            else:
                break
        
        brd.make_move(players[turn], int(move))

        if turn == 0:
            turn = 1
        elif turn == 1:
            turn = 0

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    #print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()
