#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Find <b><font color=red>factorial</font> of a given number</font></div> 

# ### <div class="alert alert-danger"><font color=black>In mathematics, the factorial of a positive integer number n, denoted by n!, is the product of all positive integers less than or equal to n.</font></div> 

# #### Examples :  
# #### 5! = 5 * 4 * 3 * 2 * 1 = 120, 0! = 1, 3! = 3 * 2 * 1 = 6, ... etc  

# In[5]:


# This program finds factorial of a given number. (Method-I) (Without using any libraries)

number = int(input('Please enter a number : '))

factorial = 1

for i in range(1, number+1):
    factorial *= i

print(f"\n{number} ! = {factorial}")


# In[7]:


# This program finds factorial of a given number. (Method-II) (Using math library)

import math #  Importing math library.

number = int(input('Please enter a number : '))

factorial = math.factorial(number) #  Finding factorial.

print(f"\n{number} ! = {factorial}")


# In[ ]:




