#!/usr/bin/env python
# coding: utf-8

# # Practical exercise :  Become a teacher assistant
# 
# For this practical exercise, imagine you are a student in a chemistry class.
# 
# Your teacher assigned you a task to create a report card on your classmates' chemistry exams. 
# 
# 📌 The exam scores are given as points between 0 and 100, but in the report card the grade have to be given as letters. 
# 
# 📌 He has provided you with the conversion table so that you can convert points to letters.
# 

# ## Warm up
# 
# Before you start working on the report card and practicing file operations and exceptions handling, let's warm up by defining the functions we will need. 
# 
# 📌Define a function *compute_grade* that converts points to letter grades.
# 
# 📌This function should take points as an argument and return the grade as a letter. 
# 
# The conversion table is as follows:
# 
# Points | Grade
# --- | ---
# 70 - 100 | A
# 50 - 69 | B
# 30 - 49 | C
# 0 - 29 | F
# 
# 📌 You can use if, elif and else statements. 
# 

# In[2]:


#Define a function compute_grade that takes points as an argument and returns the grade as a letter
def compute_grade(points):
  if points >= 70:
    return 'A'
  elif points >=50:
    return 'B'
  elif points >=30:
    return 'C'
  else:
    return 'F'


# Let's check if your function is working.
# 
# One of your classmates got 39 points in the exam. Use the function *compute_grade* to check his grade.

# In[6]:


#Call the function to convert 39 points to a letter grade
compute_grade(39)


# ## Prepare the report card message
# 
# Now, you have a function to convert the points to letter grades. But to make a report card, we need more information. 
# 
# The report card should also include the name of the student, their points, and the resulting grade. All of this can be written in a sentence like this: "[Student name] scored [points]/100 points in Chemistry and got the grade [letter grade]"
# 
# Here are the steps to do this:
# 
# 📌 Define a function (e.g. *report_message*) that takes the student name and the points as an argument.
# 
# 📌 Inside the function, use the *compute_grade* function to convert the points to a letter grade.
# 
# 🧨 You can use the '+' sign to concatenate strings. 
# 
# 💣 You might need to convert variables to string data type to be able to include them in the message.
# 
# 

# In[7]:


#Define a function that takes the student name and the points as an argument and returns the message for the report card
def report_message(name, points):
  return name + " scored " + str(points) + "/100 points in Chemistry and got the letter " + compute_grade(points)


# Let's try the function for your classmate Zach, who scored 51 points.

# In[8]:


#Call the function for you friend Zach
report_message("Zach", 51)


# ## Help your teacher send Zach his report card
# Great! Your teacher wants you to create a report card for Zach that he can send to him. 
# 
# You decide that the easiest way to do this is to save the report card message inside a text file.
# 
# 📌 Create a text file *zach_report.txt* in which the message can be saved.
# 
# 💣 Remember that you can simply create a file by opening it in the write mode. 
# 
# 📌 Use the .write() method to write the message inside the file.
# 
# 🧨🧨🧨 Make sure to close all the files that you open during this exercise once you are done using them!

# In[9]:


#Creat a text file for Zach's report card and write the message inside
result_file = open("zach_report.txt", 'w')
result_file.write(report_message("Zach", 51))
result_file.close()


# ## Check if report cards are already prepared
# 
# Sophie got 78 points in the exam and your teacher wants to send her a report card as well. However, he doesn't remember if there is already a report card for her. Let's find out!
# 
# 
# 📌 Check if there is already an existing report card *sophie_report.txt* by trying to open it in the read mode. If there is, print a message: 'There is an existing report card for Sophie.'
# 
# 📌 However, if there is none, you need to create one and write the message inside.
# 
# 💣 If the file does not exist, you will get an error! Make sure to apply the exception handling techniques that we covered in this module to prevent errors.
# 
# 📌📌📌 Use the *try* keyword to open the file sophie_report.txt in the read mode. If the file does not exist, it will throw an exception. In the *except* block, open the same file in the write mode to create the file.

# In[10]:


#Check if there is already a report card for Sophie and print a message in case there is
try:
  result_file = open("sophie_report.txt", 'r')
  print('There is an existing report card for Sophie')
#If there is none, create one and write the message inside
except:
  result_file = open("sophie_report.txt", 'w')
  result_file.write(report_message("Sophie", 78))

result_file.close()


# ## Good job, your teacher is impressed!
# 
# You have done a great job helping him. That's why he wants you to take it a step further and enter the grades of the whole class in a single file.
# 
# Instead of a message for each student, the file should contain the names and the grades as letters in this form: 
# 
# *Name:Grade*
# 
# 
# 📌 For this task you will implement a function *student_grade* which takes the student name and points as arguments. This function should use the previously defined *compute_grade* function to convert points to a letter grade. 
# 
# 🧨🧨 There might be some missing students during the exam. Instead of the points, 'missing' will be entered for them. The function should consider the exception case when the points are not a number.

# In[11]:


#Define a function that takes the student name and the points as an argument and returns them as specified in the instructions
def student_grade(name, points):
  #return name:grade
  try:
    return (name + ':' + compute_grade(points))
  #or return a message if the student was missing
  except:
    return (name + ' was missing during the exam.')


# Your teacher provided you a list with the students and their points in the exam. If a student is missing, the string 'missing' is entered instead.

# In[12]:


#Run the list of all students and their points
student_list = [('Zach', 51), ('Sophie', 78), ('Fred', 29), ('Belina','missing'), ('Markus','missing')]


# ### (1) Use a for loop to access each student one at a time
# 
# 📌 You can loop over the list that you teacher provided you by using a for loop.
# 
# 📌 Unpack the tuples containing the student name and points, then use the *student_grade* function you defined earlier to convert the points into a letter grade.
# 
# 📌 Print the message that the *student_grade* function returns
# 
# 

# In[13]:


#Write a for loop to access each student one at a time and unpack the tuple
for name, points in student_list:
  grade = student_grade(name, points)
  #print the message returned by student_grade
  print(grade)


# ### (2) Store the names and the grades in a text file
# 
# As a last step, you need to save the grades inside a file. 
# 
# 📌 Create a file *grades.txt* by opening it in the write mode.
# 
# 📌 Instead of printing the grade, use the .write() method and the for loop you just created to write the grades into the file.
# 
# 💣 Make sure to add the escape statement '\n' to each line you write to the file to indicate that each student should be written in it's own line.
# 
# 

# In[15]:


#Create the grades.txt file
grades_file = open("grades.txt", 'w')

#Use the for loop to write the name and grade of each student in the file 
for name, points in student_list:
  grade = student_grade(name, points)
  #Write the message returned by student_grade into the file
  grades_file.write(grade + '\n')


# Well done! 
# You have completed all the tasks that your teacher had assigned you. Don't forget to close the grades.txt file.

# In[16]:


#Close the file
grades_file.close()


# In[ ]:




