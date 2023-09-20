#!/usr/bin/env python
# coding: utf-8

# In[9]:


# This program guesses the number which user is thinking of.

print("Let's start play the guessing game!")

user = int(input("\nPlease enter a two digit number that you are thinking of : "))

while True :
    guess = int(input("\nWhat a two digit number am I thinking of? \t\t   "))
    
    if guess < user :
        print("\nLittle higher..")
    elif guess > user :
        print("\nLittle lower..")
    else :
        print("\nCongratulations. You guessed it right. Are you a MINDREADER?")
        break 


# In[ ]:




