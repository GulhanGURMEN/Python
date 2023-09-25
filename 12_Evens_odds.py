#!/usr/bin/env python
# coding: utf-8

# In[9]:


# This program first creates a list in increments from zero to 
# a number given by the user. Then it lists the numbers in this list 
# as odd and even.

my_list = []
evens = []
odds = []

number = int(input("Please enter a number :"))

for n in range(number) :
    
    my_list.append(n)
    
    if n % 2 == 0 :
        evens.append(n)
    else : 
        odds.append(n)
    
    
print("\nmy_list\t: ", my_list)     
print("\nevens\t: ", evens)
print("\nodds\t: ", odds)

