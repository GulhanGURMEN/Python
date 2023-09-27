#!/usr/bin/env python
# coding: utf-8

# In[9]:


# This program prints even numbers of missing numbers that are
# between the smallest element and the largest element of the given list, 
# but not shown in the given list.

# A jumbled list is given whose elements are consecutive numbers.

# This program is written by using list comprehension and ternary expression.

jumbled_list = [48, 10, 11, 21, 36, 5, 6, 52, 28, 29, 53, 54, 45, 19, 20, 47, 55, 39,                 41, 7, 9, 17, 26, 27, 42, 22, 37, 51, 46, 18, 44, 30, 34, 13, 15, 35, 33,                 16, 50, 24]

missing_numbers = [i for i in range(min(jumbled_list), max(jumbled_list)+1) if i % 2 == 0 and not i in liste]
print(* missing_numbers)


# In[ ]:




