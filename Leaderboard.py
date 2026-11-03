import csv
import tkinter as tk

def stats_sort(stats: list):
    """Sort the list of stats by wins, using recursion."""

    if len(stats) == 0:
        return []

    winner: str = stats[0]

    for stat in stats:
        if stat[1] > winner[1]:
            winner = stat

    stats_temp: list = stats.copy()
    stats_temp.remove(winner)

    return [winner] + stats_sort(stats_temp)
    
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
        player_stats_list: list = []
        for player, stats in self.stats.items():
            player_stats_list.append((player, stats["wins"], stats["losses"], stats["draws"]))
        return stats_sort(player_stats_list)

    def save(self):
        """Write every player to self.filename as CSV."""
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            for player, stats in self.stats.items():
                writer.writerow([player, stats["wins"], stats["losses"], stats["draws"]])

    def load(self):
        """Read self.filename into self.stats. If the file doesn't exist
        yet, start with an empty dict (don't crash)."""
        try:
            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    player, wins, losses, draws = row
                    self.stats[player] = {"wins": int(wins), "losses": int(losses), "draws": int(draws)}
        except FileNotFoundError:
            pass


