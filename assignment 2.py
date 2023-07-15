#!/usr/bin/env python
# coding: utf-8

# Q1. How do you comment code in Python? What are the different types of comments?
# Ans. we use # at the begining of line for single line comment and for multiline comment we use triple " at the begining and also end of text which we have to comment.
# 

# In[1]:


# This is single line comment.
""" we use triple (") at the begining a nd end of text which we have to comment.
just like this text"""


# Q2. What are variables in Python? How do you declare and assign values to variables?
# Ans. Variable are use to store values or we can say that it is a place in memory where we assign value
# we can assign the variable by using assignment operator in right side we assign the value in variable and in left side we put name of that variable as shown below

# In[2]:


A = 123
B = "string"
C = 23.42
D = 7+5j
E = True


# Q3. How do you convert one data type to another in Python?
# Ans. Python has two ways to change one data type to another data type.
# Implicit and Explicit type conversion
# In Implicit type conversioncSystem Automatically one data type converted to another data type.
# In Explicit Data type we have to type cast one data to another data type manually.

# In[5]:


X = 12234
Y = str(X)
type(Y)


# Q4. How do you write and execute a Python script from the command line?
# Ans. Open a command line and type "python" and the location of your script file then all that's left to do is press the ENTER key on the keyboard.
# 

# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[13]:


#Ans. 
my_list = [1, 2, 3, 4, 5]

sub_list = my_list[1:3]
sub_list


# Q6. What is a complex number in mathematics, and how is it represented in Python?
# Ans. A complex nuber is a number which is i the form of x+yi where x and y are real number and i is imaginary unit . In Python we define complex number in a + bj where a and b are real number and j is imaginary unit.

# In[15]:


Q = 3 + 9j
type(Q)


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
# Ans. there are certain  rules ti which we have to kept in mind for declaring value.
# 1.Underscore(_) , numbers and letters(both lower and upper case) are all acceptable character for variable names. They have to be preceded by a letter or an underscore.
# 2. Python is case sensitivite language. A and a are two distinct variable namber.
# 3. we cannot start name of variable by digit or special case(except _)
# 

# In[16]:


a = 25


# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable
# belong to?
# Ans. it is a float data

# In[18]:


price = 9.99
type(price)


# Q9. Create a variable named name and assign your full name to it as a string. How would you print the
# value of this variable?

# In[19]:


name = "Prashant Kumar Singh"
name


# Q10. Given the string "Hello, World!", extract the substring "World".
# 

# In[23]:


String = "Hello, world!"
sub_str = String[7:12:]
sub_str


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
# currently a student or not.

# In[24]:


is_student = True  
is_student = False 


# In[ ]:




