import pandas as pd
from utils.game_logic import play_tic_tac_toe

def play_tic_tac_toe():
    board = Board()
    board.draw_board()

if __name__ == "__main__":
    play_tic_tac_toe()