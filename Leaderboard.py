import csv
import tkinter as tk
    
class Leaderboard:
    def __init__(self, filename):
        self.stats: dict[str, dict[str, int]] = {}
        self.filename: str = filename

    def add_player(self, name):
        """Add the player with all counts at 0, if not already there."""
        if name not in self.stats:
            self.stats[name] = {"wins": 0, "losses": 0, "draws": 0}

    def record_result(self, winner, loser):
        """winner +1 win, loser +1 loss. Decide how you'll record a draw."""
        self.add_player(winner)
        self.add_player(loser) 

        self.stats[winner]["wins"] += 1
        self.stats[loser]["losses"] += 1

    def record_draw(self, player1, player2):
        """Both players +1 draw."""
        self.add_player(player1)
        self.add_player(player2)
        self.stats[player1]["draws"] += 1
        self.stats[player2]["draws"] += 1

    def get_sorted(self):
        """Turn self.stats into a list and return it sorted by wins,
        using your recursive sort."""

    def save(self):
        """Write every player to self.filename as CSV."""

    def load(self):
        """Read self.filename into self.stats. If the file doesn't exist
        yet, start with an empty dict (don't crash)."""

    def leaderboardGUI(self):
        '''Uses tkinter to make a GUI for the leaderboard.'''