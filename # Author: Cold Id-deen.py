# Author: Cold Id-deen
# Date: July 28, 2025
# Purpose: Practice on Python for Password Generator

# Using Python Library to start the loading bar as alive_bar. 
from alive_progress import alive_bar
import time 

# Using another Python Library to start different loading bar as tqdm.
from time import sleep
from tqdm import tqdm

# Importing Python modules to generate random characters for password
import random 
import string 

# Combine letters, digits, and punctuation into one pool of characters
characters = string.ascii_letters + string.digits + string.punctuation

# Setting the loading bar using alive_bar with 10 steps, a title, spinner style, and a smooth bar style
with alive_bar(10, title='LOADING: ', spinner='dots', bar='smooth') as bar:
    for i in range(10):         # Loop 10 times to simulate loading
        time.sleep(0.2)         # Wait for 0.2 seconds between each step
        bar()                   # Update the loading bar

# Ask the user's name. 
print("Hello, what is your name?")

# Store their name in a variable called 'name'
name = input()

# Greet the user using the name they entered
print(f"Nice to meet you, {name}!")

# Ask the user if they're ready to do the password generator. 
ready = input("Are you ready? (Y/N): ")

# If the user selects Y to confirm, the tqdm loading bar will appear
if ready == "Y":
    print("Wait a moment...")
    for i in tqdm(range(10), desc=" [OK] LOADING: "):  # Loading bar with title
        sleep(0.50)                                    # Wait half a second each step

# If the user selects N to deny, the program will end
elif ready == "N":
    print("Exiting the program... ")
    exit()  # Stop running the program immediately

# Start a loop that will keep asking until valid password length is entered
while True: 
    # Ask the user how long they want their password to be
    length_input = input("How long should your password be? (MIN 10 - 20 MAX!!): ")

    # Check if the input is not a number
    if not length_input.isdigit():
        print("Invalid. Please enter the properly a number, not letters or symbols. ")
        continue  # Skip the rest of the loop and ask again
    
    # Convert the string input to an integer
    password_input = int(length_input)

    # If the number is less than 10, it's too short
    if password_input < 10:
        print("⚠️ Too short. Minimum is 10 characters, try again.")
    # If the number is more than 20, it's too long
    elif password_input > 20:
        print("⚠️ Too long. Maximum is 20 characters, try again.")
    else:
        # If the input is valid, move forward with the password creation
        print(f"Perfect! Creating a {password_input}-character password...")

    # Ask the user again if they're ready to continue
    ready = input("Are you ready? (Y/N): ").upper()  # Ask for confirmation again and convert to uppercase

    if ready == "Y":
        # Show custom loading bar with 10 steps
        total = 10
        for i in range(1, total + 1):  # Loop from 1 to 10
            progress = i / total * 100  # Calculate the percentage progress
            bar_length = 10  # Total length of the visual bar
            filled_length = int(bar_length * progress / 100)  # Calculate how much of the bar is filled
            bar = '?' * filled_length + '-' * (bar_length - filled_length)  # Create the visual bar using ? and -
            print(f"Progress: [{bar}] {progress:.1f}%")  # Show the bar with percentage
            sleep(0.3)  # Add a small delay so the loading bar is visible

        # Generate the password after the progress bar is done
        password = ''.join(random.choices(characters, k=password_input))  # Randomly pick characters and join them
        print("\n Sucessfully! Your new password is:", password)  # Print the final password

    elif ready == "N":
        # If the user says no, cancel the generation
        print(f"ERROR! --> Cancelled by {name}!")  # Print who cancelled it

    # Always break after a valid input + process to exit the loop
    break
