#!/usr/bin/env python
# coding: utf-8

# In[6]:


# This program prints the given list as sudoku looking format.

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

count=0
print("- - - - - - - - - - - - - - -")
for i in sudoku:
  for j in range(9):
    print(i[j], end="  ")
    if (j)==8 :
      print()
      count+=1
      if count % 3 == 0:
        print("- - - - - - - - - - - - - - -")
    if j==2 or j==5:
      print("| ", end="")


# In[ ]:




