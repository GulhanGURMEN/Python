#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Generate <b><font color=red>Fibonacci Series</font> up to given maximum number</font></div> 

# ### <div class="alert alert-danger"><font color=black>Fibonacci series or sequence starts with two numbers 0 and 1, and next number is obtained by adding two numbers before it. For example, third term 1 is found by adding 0 and 1, fourth term 2 is then obtained by third term 1 and second term 1.</font></div> 

# ### <div class="alert alert-danger"><font color=black>Fibonacci series is : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...</font></div> 

# In[6]:


# This program generates Fibonacci series up to given maximum number. 

n = input("Please enter a number\t: ")

while not n.isdigit() or int(n)<=1:
  print("\nIt is an invalid entry. Don't use non-numeric, float, zero, one or negative values!\n ")
  n = input("Please enter an another number! ")
else:
  n = int(n)  
  fibonacci=[]
  for i in range(n):
    if i == 0 :
        fibonacci.append(i)
    elif i == 1 :
        fibonacci.append(i)
    else :
        fibonacci.append(fibonacci[-1]+fibonacci[-2])  
  print("Fibonacci Series\t:", fibonacci)


# In[ ]:





# In[ ]:




