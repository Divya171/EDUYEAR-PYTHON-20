
# coding: utf-8

# In[16]:


#Day 6: Day 6 - List Comprehensions and Tuples


#1. Give all the index values of vowels.

#Eg. "abed" 
#>> 0 2

#2.
#Reverse the words of a string

#Input... hello world happy birthday
#Output... birthday happy world hello

#3. Remove duplicate elemnts without using set()
#Ex. 
#[1,2,3,3,2,4]
#>> [1,2,3,4]


# In[4]:


#1. Give all the index values of vowels.

#Eg. "abed" 
#>> 0 2
vowels = ['a','e','i','o','u']
word = input("Enter the word of your choice")

for letter in word:
    if letter in vowels:
        print("The vowel {} is at {} index".format(letter, word.index(letter)))
    #else:
        #print("{} is a consonant".format(letter))
        


# In[12]:


#que 1 using list comprehension

vowels = ['a','e','i','o','u']
word = input("Enter the word of your choice")

indices = [print(word.index(letter)) for letter in word if letter in vowels]
#print(indices)


# In[19]:


#2.
#Reverse the words of a string

s = input("enter a word")
print(s[::-1])

# without slice operator

st = input("Enter a word")
i = len(st)-1
output = ''
while i>=0:
    output = output+st[i]
    i=i-1
print(output)

# for input divya: this code gives output 'ayvid'


# In[31]:


#Input... hello world happy birthday
#Output... birthday happy world hello

s = input("Enter the string")
l = s.split()
#print(l)

l1=[]
i = len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
#print(l1)
print(' '.join(l1))


# In[41]:


#3. Remove duplicate elemnts without using set()
#Ex. 
#[1,2,3,3,2,4]
#>> [1,2,3,4]

s = [1,2,3,3,2,4]
l=[]

for x in s:
    if x not in l:
        l.append(x)
print(l)

