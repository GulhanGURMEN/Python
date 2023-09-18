#!/usr/bin/env python
# coding: utf-8

# In[8]:


# This program calculates the body mass index.

weight = float(input("Please enter your weight as kg.\t\t\t= "))
height = float(input("Please enter your height as meter (e.g. '1.76')\t= "))
body_mass_index = weight / height ** 2
print("Your body mass index \t\t\t\t= %.2f" % (body_mass_index))

