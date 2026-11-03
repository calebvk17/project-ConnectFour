# Connect Four

## The application

We are building a networked multiplayer Connect Four game that players can play through the terminal. It will allow players to take turns on a game board, with features like save/load, an AI opponent, win/draw detection, move history, and a leaderboard.

## Features (current):

-Connect Four board shown in the terminal, with pieces dropped into columns 1-7
-Save and load a game in progress (kept in memory, so it lasts for the current session only)
-Leaderboard that stores wins, losses and draws per player, ranked by wins
-Leaderboard saved to and loaded from a CSV file, so it survives a restart
-Leaderboard window built with tkinter
-Startup menu: play a game, view the leaderboard, or quit
---stats-file command-line option to choose where the leaderboard is saved

## Planned:
-Switching turns between players
-Win and draw detection
-Recording game results on the leaderboard automatically
-AI opponent, move history and player statistics
-Game rooms and multiplayer networking

## How to play:
-At the menu, enter 1 to play, 2 to view the leaderboard, or 3 to quit (this saves the leaderboard).
-During a game, enter a column number from 1 to 7 to drop a piece.
-Type save to save the current game, or load to restore the last saved game.

## The team

| Full name | GitHub username |
|-----------|-----------------|
| Alvin Joji John    | @Alvin1332     |
| Caleb Van Kampen    | @calebvk17     |
| Loaghan Vivares    | @LoaghanV     |

Note:  Be sure to [add all of the group members to as collaborators on this repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

<!-- Fill this in at Milestone 0. Teams of four: delete the fifth row.
     The GitHub username must be the one that authors your commits, so your work in the
     history can be matched to you - check yours with:  git log --format='%an <%ae>'
     Who owns which slice, and what each member contributed, go in CONTRIBUTIONS.md. -->

## Running it

```
python main.py
```

## Design

<Leave this until Milestone 3. Then add, in about a page: how the pieces fit together
(server, client, engine, storage), and a short **Big-O note** for the algorithm your team
implemented - what it does, its complexity, and why that is fast enough here.>

## Required Files

| File | What it is |
|------|------------|
| [`MILESTONES.md`](MILESTONES.md) | **the project requirements** - all four milestones, what's due when |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | who owns which slice, and which commit proves each member did each topic |
| [`AI-USAGE.md`](AI-USAGE.md) | the AI policy, and your team's disclosure |

> **This file is yours.** The sections above are part of your Milestone 0 write-up - fill
> them in together, and fill in the slices table in `CONTRIBUTIONS.md` at the same time.
> From Milestone 1 on, grow "The application" and "Running it" into a real README for your
> project, and keep the team table, the tech plan, and these pointers.

