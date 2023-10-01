#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Write a program that groups <font color=red>anagrams</font> of words given in a list. </font></div> 

# ### <div class="alert alert-danger"><font color=black> An <font color=red>anagram</font> is a word or phrase the letters of which can be rearranged into another word or phrase.</font></div> 

# ### <div class="alert alert-danger"><font color=black>Examples of anagram words :  triangle = integral, save = vase, bored = robed, arc = car, dusty = study, etc. </font></div> 

# In[6]:


# This program groups anagrams of words given in a list.

strs_list = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac",             "triangle", "save", "dusty", "car", "integral", "arc",              "silent", "study", "vase", "listen", "inch", "chin"  ]
anagram = {}
for i in strs_list:
    element = "".join(sorted(i))
    if element in anagram:
        anagram[element].append(i)
    else:
        anagram[element] = [i]
print(list(anagram.values()))


# In[7]:


# The detailed explanation of the above code block is given below. 

strs_list = strs_list = ["eat", "tea", "tan", "ate", "nat", "bat", "cat", "tac",             "triangle", "save", "dusty", "car", "integral", "arc",              "silent", "study", "vase", "listen", "inch", "chin"  ]
anagram = {}  # this is a dictionary.
for i in strs_list:
    element = "".join(sorted(i))  # sorted(i) gives us a list: ['a', 'e', 't']
    if element in anagram:
        anagram[element].append(i)
    else:
        anagram[element] = [i]  # anagram[element] is key, [i] is value/ we do this to insert pairs into dictionary.
        
print(sorted(i))  # when we use sorted() on a word from strs_list this is what we get.      
print()
print(element)  # we use "".join to turn the list into a string.
print()
print(anagram)  # what we actually created, but we dont want all of it.
print()
print(anagram.values())  # what we want, just not in the form we want it.
print()
print(list(anagram.values()))  # we want anagrams in list form, not in dict_values class


# In[8]:


# The version of the same program arranged to get the words from the user is given below.

strs_list = []
anagram = {}
counter = 0
list_size = int(input("How many words would you like to enter?\t"))

while counter < list_size:
    counter += 1
    word = input("\nAdd a word to your list: ").lower()
    strs_list.append(word)
for i in strs_list:
    element = "".join(sorted(i))
    if element in anagram:
        anagram[element].append(i)
    else:
        anagram[element] = [i]
print(list(anagram.values()))


# In[ ]:




