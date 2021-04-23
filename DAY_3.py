
# coding: utf-8

# In[1]:


#AGE CALCULATOR 
#1)  calculate Age of a person - User should enter the year of birth and the program should output the age.. eg : entered value is 1990, output age is 30


year = int(input("Enter your birth year"))
age = 2021 - year
print("Your age is {} years". format(age))



# In[10]:


#2) Simple Calculator:

#- get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, power of the input numbers


num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

S= num1 + num2

diff = num1 - num2
    
prod = num1 * num2

fd = num1//num2

quo = num1/num2

rem = num1%num2
 
P = num1**num2

print("The sum of the two numbers is {}".format(S))
print("The difference of the two numbers is {}".format(diff))
print("The product of the two numbers is {}".format(prod))
print("The floor division of the two numbers is {}".format(fd))
print("The quotient is {}".format(quo))
print("The remainder is {}".format(rem))
print("The power is {}".format(P))



# In[12]:


#3) use string functions to count the occurrence of 'y' in a word given by user.

word = input("Enter a word of your choice ")

print(word.count('y'))


# In[13]:


#4) take input of a string and print it's even indexed characters

word = input("Enter a word of your choice ")
print(word[::2])

