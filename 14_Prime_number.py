#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Write a program that takes a number from the user and check if it is a<b/></font> <font color=red><b>prime number.</b></font></div> 

# ### <div class="alert alert-danger"> <font color=red><b>Prime numbers</b></font><font color=black> are the numbers that are only divisible by themselves and 1, in other words, if we try to divide them by another number, the result is not a whole number. So, if you divide the number by anything other than one or itself, you will get a remainder that is not zero.</font></div>

# In[4]:


# This program takes a number from the user and check if it is a prime number.

number = int(input("\nEnter a positive integer number to check if it is a Prime Number : "))
print()
counter = 0

for i in range(1, number+1) :
    if number % i == 0 :
        counter += 1   # counter = counter +1
        
if (number == 0) or (number == 1) or (counter >=3) :
    print(number, " is NOT a Prime Number.")

else :
    print(number, " is a Prime Number.")


# In[ ]:




