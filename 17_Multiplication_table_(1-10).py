#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Write program that prints the <font color=red>multiplication table</font> from 1x1=1 to 10x10=100. <b></font></div> 

# In[10]:


# This program prints the multiplication table from 1x1=1 to 10x10=100.

print("\nMultiplication Table")

for i in range(1,11):
    print("~" * 20)
    print("For",i)
    
    print("~" * 20)
    for k in range(1,11):
        print(i,"x", k,"=",i*k)


# In[ ]:




