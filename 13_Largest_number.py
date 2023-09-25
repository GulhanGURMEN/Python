#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


# This program finds largest of two numbers given by user.

num_1 = float(input("Enter first number\t: "))
num_2 = float(input("\nEnter second number\t: "))

if num_1 > num_2 :
    largest = num_1
    
else :
    largest = num_2
    
print("\nThe larger number is ", largest)


# In[5]:


# This program finds largest of three numbers given by user.

num_1 = float(input("Enter first number\t: "))
num_2 = float(input("\nEnter second number\t: "))
num_3 = float(input("\nEnter third number\t: "))

if (num_1 >= num_2) and (num_1 >= num_3) :
    largest = num_1
elif (num_2 >= num_1) and (num_2 >= num_3) :
    largest = num_2
else :
    largest = num_3

print("\nThe largest number is ", largest)


# In[ ]:




