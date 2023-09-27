#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This program prints numbers that form a Pythagorean triangle (from 1 to 100).

# Method -I

for i in range(1, 101) :
  for j in range(i, 101) :
    for k in range(j, 101) :
      if i ** 2 + j ** 2 == k ** 2 :
        print(i, j, k)


# In[3]:


# This program prints numbers that form a Pythagorean triangle (from 1 to 100).

# Method -II (List comprehension and ternary expression)

[(i, j, k)  for i in range(1,101) for j in range(1,101) for k in range(1,101) if (i**2 + j**2 == k**2)]


# In[ ]:




