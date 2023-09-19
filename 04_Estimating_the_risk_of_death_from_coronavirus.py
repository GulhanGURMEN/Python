#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Estimating the risk of death from <font color=red>coronavirus.  </font></div> 

# ### <div class="alert alert-danger"><font color=black> Consider the following questions in terms of <font color=red>True / False</font>  regarding someone else.</font></div>

# ####  - Are you a cigarette addict older than 75 years old?
# ####  - Do you have a severe chronic disease? 
# ####  - Is your immune system too weak?
# ####  - Set a logical algorithm using boolean logic operators <font color=red>(and / or)</font>  and the given variables in order to give us <font color=red>True</font> (there is a risk of death) or <font color=red>False</font> (there is not a risk of death) as a result.

# In[4]:


# This program estimates the risk of death from coronavirus.

age = input("Are  you a cigarette  addict  older than 75 years old?\n(Please answer this question as Yes or No)\t\t : ").title().strip()

chronic = input("\nDo you have a severe chronic disease?\n(Please answer this question as Yes or No)\t\t : ").title().strip()

immune = input("\nIs your immune system too weak?\n(Please answer this question as Yes or No)\t\t : ").title().strip()

if age == 'Yes':
  age = True
else :
  age = False
if chronic == 'Yes':
  chronic = True
else :
  chronic = False
if immune == 'Yes':
  immune = True
else :
  immune = False

risk = age or chronic or immune 

if risk==True:
  message = "You are in risky group"
else:
  message = "You are not in risky group"
print("\n\t\t\t\t\t\t\t :", message)

