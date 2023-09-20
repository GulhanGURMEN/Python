#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Method - I (with set)
# This program finds the number of occurrences of each letter 
# in a sentence entered by the user.

sentence = input("Please write a sentence : ").lower()
unique = set(sentence)
letter = {}
for i in unique:
  letter.update({i:sentence.count(i)})
print("\nnumber of letter = ",letter)


# In[ ]:





# In[12]:


# Method - II (with if) 
# This program finds the number of occurrences of each letter 
# in a sentence entered by the user.

sentence = input("Please write a sentence : ").lower()
letter = {}
for i in sentence:
    if i not in letter:
        letter.update({i:sentence.count(i)})
print("\nnumber of letter = ",letter)


# In[ ]:




