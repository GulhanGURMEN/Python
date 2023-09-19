#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-success"><font color=black><u>Task :</u> Find out the <font color=red>most frequent number</font> and its <font color=red>frequency</font> in the given <font color=red>list.</font></div> 

# In[10]:


# This program finds out the most frequent number and its frequency in the given list.

numbers = [-1, 3, 4, 7, 3, 0, 3, 16, 3, 7, 0, 0, 1]

most_frequent_number = max(numbers, key = numbers.count)

frequency = numbers.count(max(numbers, key = numbers.count))

print(f"The most frequent number is {most_frequent_number} and it was {frequency} times repeated.")

