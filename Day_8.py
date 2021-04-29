
# coding: utf-8

# In[10]:


# 1. Take a number from user and check whether it is prime or not. Use paramters to send the number to the function
#eg. Enter a nnumber 3
# 3 is prime


def prime(num):
    found = False
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                found = True
                break
    if found:
        print(num, "is not a prime number")
    else:
        print(num,"is a prime number")

num = int(input("Enter a number of your choice"))       
prime(num)


# In[9]:


#2. Write a function to print n factorial
# Take n value as user input and pass as a parameter
#E.g Enter a number 5
# 120

def factorial(num):
    fact = 1
    while num>0:
        fact=fact*num
        num-=1
    print(fact)

num = int(input("Enter the number of your choice"))
factorial(num)
    

