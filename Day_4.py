
# coding: utf-8

# In[ ]:


#Assignment for For Loops

1. From range n to m,  

2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
Given:

number_of_terms = 5

So series will become 2 + 22 + 222 + 2222 + 22222

Expected output:

24690

Hint: 'a'*2 = 'aa'



Assignment for While Loops

3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)


4.  Write a loop to find the factorial of any number
The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
Expected output:

120


# In[1]:


#1. From range n to m, print all the numbers divisible by 5 and 7 both

n = int(input("Enter the first number"))
m = int(input("Enter the last number"))

for i in range(n,m+1):
    if i%5==0 and i%7==0:
        print(i)


# In[19]:


#2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
total = 0
for i in range(1,6):
    a = '2'*i
    total = total + int(a)
print(total)


# In[18]:


#3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)

total = 0
while True:
    n = input("Enter a number or press q to quit")
    if n == 'q':
        break
    else:
        n = int(n)
        total+=n
print("The sum is:",total)


# In[20]:


#4.  Write a loop to find the factorial of any number
#The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.

n = int(input("Enter the number of your choice"))

fact = 1
while n>0:
    fact=fact*n
    n-=1
print(fact)

