#!/usr/bin/env python
# coding: utf-8

# In[4]:


# This program prints the numbers from 1 to n. But for multiples of 3, 
# print 'Fizz' instead of the number, and for multiples of 5, print 'Buzz'. 
# For numbers that are multiples of both 3 and 5, print 'FizzBuzz'."

n = int(input("Please enter the last range of numbers for FizzBuzz Problem : "))
print()
for i in range(1,n+1):
  if i % 3 == 0 and i % 5 == 0 :
    print("FizzBuzz")
  elif i % 3 == 0 :
    print("Fizz")
  elif i % 5 == 0 :
    print("Buzz")
  else :
    print(i)


# In[ ]:




