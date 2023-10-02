#!/usr/bin/env python
# coding: utf-8

# ### <div class="alert alert-danger"><font color=black><u>Task :</u> Write program an <font color=red>online shop</font> to sell different types  of items.</font></div> 

# In[39]:


# This program is about an online shop to sell different types  of items

# Create a dictionary for your inventory. For each item the key should be 
# the name and the value should be a list containing price, stock, and section
# The dictionary should follow this structure:

# inventory = {'item1':[price, stock quantity,'section'], 
#              'item2':[price, stock quantity,'section']}

inventory = {'Milk':[5,2000,'dairy'],
             
             'Apples':[3,100,'fruits'],

             'Onions':[2,100,'vegetables'],

             'Oranges':[2.5,2000,'fruits'],

             'Bread':[4,2,'bakery'],

             'Bananas':[6,400,'fruits']} 

# Create a shopping list that specifies how much of each item you want to purchase

shopping_list = [('Milk',6), ('Apples',4), ('Onions', 7), ('Oranges',3),                  ('Bread',3), ('Bananas',5)]
                                                                                     
# 1. check_stock 

# Define a function to check the stock quantity of the items in your shopping list. 
# The function should take your shopping list and inventory as an argument. 
# If there is not enough stock, the amount in your shopping list should be updated to 
# the highest amount possible.

# Define the check_stock function

def check_stock(shopping_list, inventory):
    
  # Create the empty shopping_list_updated
  updated_shopping_list = []
    
  # Write a for loop to iterate over each item in your shopping list
  for element in shopping_list:
    item, amount = element
    
    # Access the available stock in your inventory
    
    inventory_value = inventory[item]
    if amount > inventory_value[1]:
        amount = inventory_value[1]
        print("We dont have enough stock of", item,"you can buy a maximum amount of",inventory_value[1])
        
    # append item and amount to your updated shopping list
    updated_shopping_list.append((item,amount))
  return updated_shopping_list

# 2.compute_bill

# Next, we need to define a function to compute the bill and the price that has to be payed in the checkout. 
# The function should take your updated shopping list and inventory as an argument.

# Define the compute_bill function

def compute_bill(updated_shopping_list, inventory):
    
  # Create a bill variable that equals 0
  bill = 0
    
  # Write a for loop to iterate over each item in your updated shopping list
  for element in updated_shopping_list:
    item, amount = element
    
    # Access the price in your inventory
    inventory_value= inventory[item]
    
    # Compute the price and add it to the bill
    bill += inventory_value[0] * amount
  return bill

# 3. update_stock

# The last function should update your store inventory after items were purchased. The function should take your 
# updated shopping list and inventory as an argument.

# Define the update_stock function 
def update_stock(updated_shopping_list, inventory):
    
  # Write a for loop to iterate over each item in your updated shopping list
  for element in updated_shopping_list:
    item, amount = element
    
    # Access the stock in your inventory
    inventory_value = inventory[item]
    
    # Decrease the stock by the amount that was purchased
    inventory_value[1] = inventory_value[1] - amount
  
  return inventory


# ### <div class="alert alert-danger"><font color=black>Time to test if <font color=red>everything is working</font></font></div> 

# In[40]:


# Call check_stock function for your shopping list
updated_shopping_list = check_stock(shopping_list, inventory)
print("\nYour updated shopping list:", updated_shopping_list)


# In[41]:


#Call the compute_bill function for your updated shopping list
bill = compute_bill(updated_shopping_list, inventory)
print("Total price:",bill,"$")


# In[42]:


#Call the update_stock function for your updated shopping list
new_inventory = update_stock(updated_shopping_list, inventory)
print("The inventory was updated:", new_inventory)

