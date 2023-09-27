#!/usr/bin/env python
# coding: utf-8

# In[12]:


# This function creates a simple calculator that can add, subtract, 
# multiply or divide depending upon the input from the user.

def calculator(x, y, sign) :
    if sign == "+" :  
        return (x + y)
    elif sign == "-" : 
        return (x - y)
    elif sign == "*" : 
        return (x * y)
    elif sign == "/" :  
        return (x / y)
    else :    
        return ("Enter a valid operator")


# In[13]:


calculator(5, 8, "+")


# In[14]:


calculator(51, 8, "-")


# In[15]:


calculator(5, 8, "*")


# In[16]:


calculator(100, 5, "/")


# In[ ]:




