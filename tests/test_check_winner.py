import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def test_winner_in_row(self):
        board = Board()
        board.grid = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(board.check_winner(), "X")

    def test_winner_in_column(self):
        board = Board()
        board.grid = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
        self.assertEqual(board.check_winner(), "X")

    def test_winner_in_diagonal(self):
        board = Board()
        board.grid = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertEqual(board.check_winner(), "X")

    def test_no_winner(self):
        board = Board()
        board.grid = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.assertIsNone(board.check_winner())

    def test_empty_board(self):
        board = Board()
        board.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.assertIsNone(board.check_winner())

if __name__ == "__main__":
    unittest.main()
