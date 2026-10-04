# Ancient Treasure Quest — Python Adventure Game

A text-based, command-line adventure game built in Python, developed with **GitHub Copilot** as a pair-programming assistant. Players explore a forest or a cave, make choices, and try to find a hidden treasure — demonstrating core Python concepts like functions, conditionals, loops, and user input handling.

## How to Play

```bash
python adventure_game.py
```

- Enter your name to begin your quest
- Choose a path: `forest` or `cave`
- Make a decision at each stage to win, lose, or get stuck
- Choose to replay after each attempt

## Game Flow

1. **Start** — Player enters their name and receives the quest briefing
2. **Path Choice** — Explore the `forest` or the `cave`
3. **Forest Path** — `follow` the river (win) or `climb` a tree (lose)
4. **Cave Path** — `light` a torch (win) or `proceed` in the dark (lose)
5. **Replay** — Option to restart the adventure after each run

## Tech Stack

- **Python 3** (standard library only — `time`, `sys`)
- Built in **VS Code** with the **GitHub Copilot** extension

## Key Concepts Demonstrated

- Modular design — each location (`forest_path`, `cave_path`) is its own function
- Conditional logic (`if`/`elif`/`else`) to branch outcomes
- `while` loops for input validation and game replay
- Input sanitization (`.lower().strip()`) for robust user input handling
- The `if __name__ == "__main__":` guard, so functions can be imported/tested without auto-running the game
- ANSI escape codes for colored, typewriter-style terminal output

## GitHub Copilot's Role

Copilot was used throughout development to:
- Suggest `if-elif-else` structures for handling player decisions
- Recommend `.lower().strip()` for consistent input handling
- Help build the restart/error-handling loop so invalid input doesn't crash the game

Full write-up of the Copilot-assisted development process, challenges, and enhancements is in [`docs/project_report.pdf`](docs/project_report.pdf).

## Project Structure

```
├── adventure_game.py           # Main game script
├── docs/
│   ├── problem_statement.pdf   # Original course project brief
│   └── project_report.pdf      # Report on Copilot integration & development process
└── README.md
```

## Author

Sanjay Gosai
*Course-End Project — Building a Python Adventure Game with GitHub Copilot*
