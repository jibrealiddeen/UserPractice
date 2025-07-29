# Username Creator System

A simple Python program for creating and managing usernames with interactive progress bars and animations.

## 📋 Description

This program allows users to create, delete, and manage usernames through an easy-to-use menu system. It includes input validation, progress bar animations, and a clean command-line interface perfect for learning Python programming concepts.

## ✨ Features

- **Username Creation**: Create usernames with validation rules
- **Interactive Menu**: Simple 4-option menu system
- **Progress Animations**: Cool loading bars and spinners
- **Username Management**: View, create, and delete usernames
- **Input Validation**: Ensures usernames meet specific criteria

## 🔧 Requirements

```bash
pip install tqdm
pip install alive-progress
```

## ⚡ Quick Start

1. Clone this repository:
```bash
git clone https://github.com/yourusername/username-creator.git
cd username-creator
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the program:
```bash
python username_creator.py
```

## 🎮 How to Use

1. **Start the program** - You'll see a welcome message and main menu
2. **Choose an option**:
   - `[1]` Create a new username
   - `[2]` Delete an existing username
   - `[3]` Show all saved usernames
   - `[4]` Exit the program

### Username Rules
- Must be at least 4 characters long
- Only letters and numbers allowed (no spaces or symbols)
- Cannot be empty
- Must be unique (not already taken)

## 📸 Screenshots

```
Hello! Welcome to Username System!

       ============== MAIN MENU ==============        
               [1] Create a username
               [2] Delete a username
               [3] Show all usernames
                       [4] Exit
What would you like to do? 1

Enter the desired username: john123
Username 'john123' is valid!
     Wait a moment... 
Progress: [→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→] 100.0%

Sucessfully 'john123' created!
Are you sure? (Y/N): Y
OK!
LOADING: ████████████████████████████████████████ 100% 0:00:10
```

## 🏗️ Code Structure

```
username_creator.py
├── loading_bar()          # Shows initial loading animation
├── create_username()      # Handles username creation and validation
├── remove_username()      # Manages username deletion/keeping
└── Main Loop             # Menu system and program flow
```

## 🔍 Functions Overview

### `loading_bar()`
- Displays a 10-step loading animation
- Starts the username creation process

### `create_username()`
- Prompts user for username input
- Validates username according to rules
- Shows creation progress with animated spinner
- Returns the valid username

### `remove_username(username)`
- Asks if user wants to keep the username
- Y = Keep username + show loading animation
- N = Delete username from list

## 📚 Learning Concepts

This project demonstrates several Python programming concepts:

- **Lists**: Storing usernames in a list
- **Loops**: `while` and `for` loops for menu and animations
- **Functions**: Breaking code into reusable functions
- **Input Validation**: Checking user input with `if` statements
- **String Methods**: Using `.strip()`, `.upper()`, `.isalnum()`
- **Libraries**: Working with external packages like `tqdm` and `alive-progress`

## 🎯 Perfect For

- Python beginners learning basic programming
- Students in intro programming classes
- Anyone wanting to understand input validation
- Learning about progress bars and user interfaces

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Some ideas for improvements:

- Add password creation functionality
- Save usernames to a file
- Add username search feature
- Implement username categories

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Cold Id-deen**  
*Created: July 28, 2025*  
*Purpose: Practice Python for User Creation*

---

⭐ If you found this helpful, please give it a star on GitHub!
