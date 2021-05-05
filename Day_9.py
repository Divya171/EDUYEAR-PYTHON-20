
# coding: utf-8

# In[1]:


#Day 9:

#Print following a pattern without using any loop. (Hint use recursive functions)

#Examples : 

#Input: n = 16
#Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

#Input: n = 10
#Output: 10, 5, 0, 5, 10


# In[14]:


def sequence(n):
    print(n)
    if n<=0:
        return 
    sequence(n-5)
    print(n)
    
sequence(16)


# In[15]:


def sequence(n):
    print(n)
    if n<=0:
        return 
    sequence(n-5)
    print(n)
    
sequence(10)

