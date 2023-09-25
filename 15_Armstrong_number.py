#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Find out if a given number is an<b/></font> <font color=red><b>"Armstrong Number".</b></font></div> 

# ### <div class="alert alert-danger"> <font color=black><b>An n-digit number that is the sum of the nth powers of its digits is called an <font color=red>n-Armstrong number.</b><br>
# #### Examples :  
# #### 474 = pow(4,4) + pow(7,4) + pow(4,4);  
# #### 93084 = 9 ** 5 + 3 ** 5 + 0 ** 5 + 8 ** 5 + 4 ** 5;  

# In[14]:


# This program finds out if a given number is an "Armstrong Number".

while True :
    number = input("\nPlease enter a positive integer number : ")
    digit = len(number)
    summ = 0
    
    if not number.isdigit() :
        print(number, " is invalid. Please enter valid input ! ")
    
    elif int(number) >= 0 :
        for i in range(len(number)) :
            summ = summ + int(number[i]) ** digit
    
        if summ == int(number) :
            print(number, " is an Amstrong Number")
            break
        else :
            print(number, " is NOT an Amstrong Number")
            break


# In[ ]:




