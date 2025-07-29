# Author: Cold Id-deen 
# Date: July 28, 2025 
# Purpose: Practice on Python for User Creation   

# These are libraries that help us do special things in our program
from time import sleep 
from tqdm import tqdm  
from alive_progress import alive_bar 
import time   

# This is a list that will store all the usernames we create
usernames = []  

def loading_bar():
    '''
    This function shows a loading bar on the screen.
    It counts from 1 to 10 and shows progress.
    Then it starts the username creation process.
    '''     
    total = 10  # Set total steps for the loading bar
    # Loop through each step from 1 to 10
    for i in range(1, total + 1):                
        progress = i / total * 100  # Calculate the percentage progress                 
        bar_length = 10  # Total length of the visual bar                 
        filled_length = int(bar_length * progress / 100)  # Calculate how much of the bar is filled                 
        bar = '!' * filled_length + '-' * (bar_length - filled_length)  # Create the visual bar using ! and -                 
        print(f"Progress: [{bar}] {progress:.1f}%")  # Show the bar with percentage                 
        sleep(1)  # Add a small delay so the loading bar is visible
    
    # Create a new username
    new_user = create_username()     
    # Add the new username to the global list
    usernames.append(new_user)     
    # Ask if user wants to remove the username
    remove_username(new_user)  

def create_username():
    '''
    This function asks the user to make a username.
    It checks if the username is good by making sure:
    - It's not empty (has something in it)
    - It has at least 4 letters or numbers
    - It only has letters and numbers (no spaces or symbols)
    - Nobody else is using it already
    
    If the username is good, it returns the username.
    '''     
    while True:  # Keep looping until a valid username is entered
        # Get username input from user and remove whitespace
        username = input("Enter the desired username: ").strip()         
        
        # Check if username is empty
        if not username:             
            print("Username can't be empty! ")             
            continue  # Go back to start of loop
        
        # Check if username is too short (less than 4 characters)
        if len(username) < 4:             
            print("Too short. Must be at least 4 characters.")             
            continue  # Go back to start of loop
        
        # Check if username contains only letters and numbers
        if not username.isalnum():             
            print("Invalid. Only letters and numbers allowed.")             
            continue  # Go back to start of loop
        
        # Check if username already exists in the list
        if username in usernames:              
            print("ERROR! That username is already taken! Try something else. ")              
            continue  # Go back to start of loop
        else:             
            # Username is valid, show confirmation message
            print(f"Username '{username}' is valid!\n     Wait a moment... ")             
            total = 30  # Set total steps for creation progress bar
            spinner = ['→', '↻', '↪', '⇨']  # Arrow-like symbols for animation

            # Display progress bar for username creation
            for i in range(1, total + 1):
                progress = i / total * 100  # Calculate progress percentage
                bar_length = 30  # Length of progress bar
                filled_length = int(bar_length * progress / 100)  # How much is filled

                # Get rotating symbol (loop through spinner list)
                current_arrow = spinner[i % len(spinner)]

                # Build visual bar with rotating arrows
                bar = current_arrow * filled_length + '-' * (bar_length - filled_length)

                print(f"\rProgress: [{bar}] {progress:.1f}%", end="")  # Overwrite the line
                time.sleep(0.70)  # Small delay for animation
            
            # Show success message
            print(f"\nSucessfully '{username}' created!")              
            return username  # Return the valid username
               
def remove_username(username):
    '''
    This function asks if you want to keep the username.
    
    If you say yes, it shows a cool loading animation and keeps it.
    If you say no, it deletes the username.
    
    username: This is the username we might delete
    '''     
    # Ask user if they want to keep the username
    keep_choice = input("Are you sure? (Y/N): ").strip().upper()      

    # If user chooses to keep it
    if keep_choice == "Y":               
        # Show a fancy loading bar using alive_progress library
        with alive_bar(10, title='LOADING: ', spinner='arrows', bar='smooth') as bar:             
            for i in range(10):  # Loop 10 times to simulate loading                
                time.sleep(1)  # Wait for 1 second between each step                
                bar()  # Update the progress bar
    else:         
        # If user chooses to delete
        # Check if username exists in the list
        if username in usernames:             
            print(f"'{username}' has been deleted! ")         
        else:             
            print(f"'{username}' was not found in the list! ")

# Menu options for the main program
menu_options = [
    "               [1] Create a username",
    "               [2] Delete a username", 
    "               [3] Show all usernames",
    "                       [4] Exit"
]

# Display welcome message
print("Hello! Welcome to Username System!")  

# Main program loop
while True:
    # Show the main menu
    print("\n       ============== MAIN MENU ==============        ")
    for option in menu_options:  # Print each menu option
        print(option)
    ask = input("What would you like to do? ")  # Get user's choice

    # Option 1: Create a new username
    if ask == "1":
        new_user = create_username()  # Create username
        usernames.append(new_user)    # Add to list
        remove_username(new_user)     # Ask if they want to delete it

    # Option 2: Delete an existing username
    elif ask == "2":
        to_delete = input("Enter the username you want to delete: ")
        if to_delete in usernames:  # Check if username exists
            usernames.remove(to_delete)  # Remove it from list
            print(f"Sucessfully '{to_delete}' removed! ")
        else:
            print("ERROR! Username not found! Try again. ")

    # Option 3: Show all saved usernames
    elif ask == "3":
        if not usernames:  # Check if list is empty
            print("No usernames saved. ")
        else:
            print("OK! All saved usernames: ")
            # Print each username with a number
            for i, name in enumerate(usernames, 1):
                print(f"{i}. {name} ")

    # Option 4: Exit the program
    elif ask == "4":
        break  # Exit the main loop