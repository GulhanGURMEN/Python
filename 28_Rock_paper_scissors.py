#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This program creates a Rock-Paper-Scissor game in which the user plays against the computer. 
# The player will choose one of the actions, and the computer will choose its action randomly.

# Import the random library
import random

# Create a list containing the three actions of the game.
action_list = ["rock", "paper", "scissors"]

# Set the scores of players to 0
computer_score = 0
player_score = 0

# Ask the user how many rounds they want to play
total_rounds = input("\nHow many rounds do you want to play? Please enter a number here : ")

# Add a round_counter that is 0 at the beginning
round_counter = 0

# Write a while loop and put the game inside
while True:

    # Increase round_counter by and print it
    round_counter += 1
    print("\nRound number : ", round_counter)

    # Select a random action for computer
    computer_choice = random.choice(action_list)
  
    # Ask player to choose an action
    player_choice = input("Please choose your action :").lower().strip()
    
    while not player_choice in action_list:
        print("It is an invalid entry.")
        player_choice = input("Please choose 'rock', 'paper' or 'scissors' ! ").lower().strip()
    else:
    
    # Print the players choices
        print("Computer : ", computer_choice)
        print("Player : ", player_choice)
    
    # Tie condition
    if computer_choice == player_choice:
        print("Tie! Both players chose the same action.")

    # Remaining conditions
    elif computer_choice == "paper":
        if player_choice == "rock":
            print("Winner is : Computer")
            computer_score += 1
        else:
            print("Winner is : Player")
            player_score += 1
    
    elif computer_choice == "rock":
        if player_choice == "paper":
            print("Winner is : Player")
            player_score += 1
        else:
            print("Winner is : Computer")
            computer_score += 1
    
    elif computer_choice == "scissors":
        if player_choice == "paper":
            print("Winner is : Computer")
            computer_score += 1
        else:
            print("Winner is : Player")
            player_score += 1

    # Stop the while loop if the round_counter equals the number of total rounds
    if round_counter == int(total_rounds):
        break

# Print the outcome of the game by using conditional statements
if computer_score == player_score:
    print("\nThere is no winner, tie.", computer_score, ":", player_score)
elif computer_score > player_score:
    print("\nComputer won with score", computer_score, ":", player_score)
elif computer_score < player_score:
    print("\nPlayer won with score", computer_score, ":", player_score)


# In[ ]:





# In[ ]:




