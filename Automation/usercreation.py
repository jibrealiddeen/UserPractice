# Author: Cold Id-deen
# Date: July 28, 2025
# Purpose: Practice on Python for User Creation 

from time import sleep
from tqdm import tqdm

print("Hello! Welcome to Username Creator!")

while True:
    choice = input("Enter the desired username: ")
    if choice == "Y":
        print("Please wait. ")
       # Show custom loading bar with 10 steps
        total = 10
        for i in range(1, total + 1):  # Loop from 1 to 10
            progress = i / total * 100  # Calculate the percentage progress
            bar_length = 10  # Total length of the visual bar
            filled_length = int(bar_length * progress / 100)  # Calculate how much of the bar is filled
            bar = '?' * filled_length + '-' * (bar_length - filled_length)  # Create the visual bar using ? and -
            print(f"Progress: [{bar}] {progress:.1f}%")  # Show the bar with percentage
            sleep(0.3)  # Add a small delay so the loading bar is visible

    elif choice == "N":
        print("Shame. Exiting the program...")
        exit() 
    else: 
        print("Invalid input. Please type Y or N. ")