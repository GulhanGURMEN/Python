#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u>  Write a program to convert the given decimal number into an equivalent binary number. <font color=red></font> <b></font></div> 

# In[36]:


# This program converts the given decimal number into an equivalent 
# binary number. (Method - 1)

number= int(input('\nPlease enter a decimal number\t\t\t: '))

binary=''

while number>0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2

print(f"\nThe binary equivalent of entered decimal number :", binary)


# In[38]:


# This program converts the given decimal number into an equivalent 
# binary number. (Method - 2)

number= int(input('\nPlease enter a decimal number\t: '))

binary = bin(number)

print(f'\nThe binary equivalent of {number} \t:',binary)


# In[ ]:




