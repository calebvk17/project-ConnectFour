# Connect Four

## The Application

We are building a networked multiplayer Connect Four game that players can play through the terminal. It allows players to take turns on a game board and includes features such as save/load, an AI opponent, win/draw detection, move history, and a leaderboard.

## Features (Current)

- Connect Four board displayed in the terminal, with pieces dropped into columns 1–7.
- Save and load a game in progress (kept in memory, so it lasts for the current session only).
- Leaderboard that stores wins, losses, and draws per player, ranked by wins.
- Leaderboard saved to and loaded from a CSV file, so it survives a restart.
- Leaderboard window built with Tkinter.
- Startup menu with options to play a game, view the leaderboard, or quit.
- `--stats-file` command-line option to choose where the leaderboard is saved.

## Planned Features

- Switching turns between players.
- Win and draw detection.
- Automatically recording game results on the leaderboard.
- AI opponent.
- Move history and player statistics.
- Game rooms and multiplayer networking.

## How to Play

1. Run the application using `python main.py`.
2. At the startup menu, enter:
   - `1` to play a game.
   - `2` to view the leaderboard.
   - `3` to quit (this saves the leaderboard).
3. During a game, enter a column number from 1 to 7 to drop a piece.
4. Type `save` to save the current game.
5. Type `load` to restore the last saved game.

## The Team

| Full Name | GitHub Username |
|---|---|
| Alvin Joji John | [@Alvin1332](https://github.com/Alvin1332) |
| Caleb Van Kampen | [@calebvk17](https://github.com/calebvk17) |
| Loaghan Vivares | [@LoaghanV](https://github.com/LoaghanV) |

**Note:** Be sure to [add all group members as collaborators to this repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

## Running It

To start the application, run:

```bash
python main.py
```

## Design

*To be completed by Milestone 3.*

Add approximately one page explaining how the different components fit together (server, client, engine, and storage). Include a short **Big-O analysis** of the algorithm your team implemented, explaining what it does, its time complexity, and why it is efficient enough for this project.

## Required Files

| File | Description |
|---|---|
| [MILESTONES.md](MILESTONES.md) | **Project requirements** – all four milestones and their deadlines. |
| [CONTRIBUTIONS.md](CONTRIBUTIONS.md) | Who owns each part of the project and which commits demonstrate each member's contributions. |
| [AI-USAGE.md](AI-USAGE.md) | The AI policy and your team's disclosure. |

---

> **This file is yours.** The sections above are part of your Milestone 0 write-up. Fill them in together and complete the contributions table in `CONTRIBUTIONS.md` at the same time.
>
> From Milestone 1 onward, expand the "The Application" and "Running It" sections into a complete README for your project. Keep the team table, technical plan, and required file references updated.