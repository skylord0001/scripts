
# Git Commit Shortcut with Emojis 🎉

A simple Python script to streamline the process of adding and committing files to Git with style! This script allows you to add files, enter a commit message, and automatically include three random emojis in the commit message for fun and expressiveness.

## Features
- **Quick File Adding**: Specify files to add to Git with a single input.
- **Emoji-enhanced Commit Messages**: Automatically adds three random emojis to your commit messages—one at the start, one in the middle, and one at the end.
- **User-friendly Cancellation**: Cancel the operation at any point by typing `cancel`.

## Requirements
- Python 3.x installed on your system.
- Git installed and configured on your system.
- Works on Windows, macOS, and Linux.

## Installation (Windows)
1. Clone the repository:
   ```bash
   git clone https://github.com/devfemibadmus/git_commit
   ```
2. Navigate to the script directory:
3. Copy the git_commit.py to dir ```C:\Scripts```
4. Copy the git_commit.bat to dir ```C:\Windows\System32\git_commit.bat```

## Usage
1. call in ur cmd:
   ```bash
   git_commit
   ```
2. Follow the prompts:
   - Enter the file(s) you want to add (space-separated). Type `cancel` to exit.
   - Enter the commit message. Type `cancel` to exit.
   - Enter the date offset (`0` for today, `-1` for yesterday, `1` for tomorrow, etc.). Type cancel to exit.

## Example
Input:
- Files to add: `main.py utils.py`
- Commit message: `Fixed a bug in the utility functions`

Generated commit message:
`🚀 Fixed a bug ✨ in the utility functions 🐛`

## Customization
You can modify the `emojis` list in the script to include your favorite emojis.

## Contributing
Feel free to fork the repository and submit pull requests with enhancements or fixes.

Enjoy committing with style! 🚀✨🎉