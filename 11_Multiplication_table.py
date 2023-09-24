#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This program prints the multiplication table of a number entered by user.

# Taking input from the user
number = int(input("Please enter a number between 1-10 :"))

# Iterate 10 times from i = 1 to 10 
for i in range(1,11) :
    print(f"{number} x {i} = {number * i}")

