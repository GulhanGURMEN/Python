#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Checking whether a given year by user is <font color=red>leap year or not.</font></div> 

# ### <div class="alert alert-danger"><font color=black> Leap Year Rules : How to Calculate Leap Years</font></div>

# ####    In our modern-day Gregorian calendar, three criteria must be taken into account to identify leap years: 
# ####  - The year must be evenly divisible by 4;
# ####  - If the year can also be evenly divided by 100, it is not a leap year; unless
# ####  - The year is also evenly divisible by 400. Then it is a leap year.
# ####  - According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.

# In[10]:


# This program checks whether a given year by user is leap year or not.

year = int(input("Please enter a year\t:"))

if (year%4==0 and year%100!=0) or (year%400==0) :
    print(f"\n\t\t\t {year} is LEAP YEAR.")
else:
    print(f"\n\t\t\t {year} is not LEAP YEAR.")


# In[ ]:




