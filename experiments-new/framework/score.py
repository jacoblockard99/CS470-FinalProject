#!/usr/bin/env python3

import chess
import chess.engine
import sys
import time
import argparse

# Command-line arguments

parser = argparse.ArgumentParser(
    description="A simple Python program that launches two Stockfish servers with various options and plays them against each other to determine which plays chess better."
)

parser.add_argument("positions", help="Path to a file containing a newline-delimited list of FEN strings representing starting positions. Two games will be run for each position in the file, with each engine getting to go first.")

args = parser.parse_args()

# Launch the Stockfish servers.

engine = chess.engine.SimpleEngine.popen_uci("../../bin/stockfish-original")
engine.configure({"Threads": 4})

# Read the positions file.

with open(args.positions, 'r') as file:
    positions = file.readlines()

# Parse the limits given via the command-line.

limits = chess.engine.Limit()
limits.depth = 20

# Function to simulate a single game between two engines.

i = 0
for position in positions:
    if args.positions.endswith(".epd"):
        board = chess.Board()
        board.set_epd(position)
    else:
        board = chess.Board(position)
    info = engine.analyse(board, limits)
    print(f"{i+1}: ", end="")
    print(info["score"], flush=True)
    i += 1

# Kill the Stockfish servers.
engine.quit()