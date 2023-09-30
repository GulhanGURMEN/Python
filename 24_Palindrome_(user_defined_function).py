#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Write a function/functions that checks whether the sentence you get from the user is a <font color=red>palindrome.</font>(Do not consider punctuation and special characters. Only consider "***alphanumeric***" characters.)</font></div> 

# ### <div class="alert alert-danger"><font color=black> A <font color=red>palindrome</font> is a word or phrase that is the same both backwards and forwards. This <font color=red>palindrome</font> definition means that if one were to read a <font color=red>palindrome</font> from right to left instead of from left to right, the resulting word would be the same in both directions. Etymologically, <font color=red>palindrome</font> comes from the Greek word palindromos, which means ''a recurrence'' or, more literally, ''running back.'' </font></div> 

# ### <div class="alert alert-danger"><font color=black>Examples of palindrome words : Mom, dad, radar, eye, madam, racecar etc. </font></div> 
# ### <div class="alert alert-danger"><font color=black>Examples of palindrome phrases : "Was it a car or a cat I saw?", "Murder for a jar of red rum", etc.</font></div> 

# In[5]:


# This program checks whether the sentence you get from the user is a palindrome.

# Function that enables a new string to be obtained by removing 
# non-alphanumeric characters from the entered sentence.

def palindrome_sentence(sentence):
  string=""
  for char in sentence:
    if char.isalnum():
      string+=char
  print(string)
  return palindrome(string)

# Function that checks whether the straight and reverse readings of the newly 
# obtained sentence are the same.

def palindrome(string):
  return string.casefold()==string[::-1].casefold()

# Reading a sentence from user 
text=input("\nPlease enter a sentence to check : ")
print()

# Deciding whether the sentence entered by the user is a palindrome or not 
# and printing the result to the screen. 

if palindrome_sentence(text):
  print("\n{} is a palindrome.".format(text))
else:
  print("\n{} is NOT palindrome.".format(text))


# In[ ]:





# In[ ]:




