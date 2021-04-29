
# coding: utf-8

# In[ ]:


common part ->  Create a list of n numbers


Q1. Count even numbers and odd numbers

Q2. Tell max and min of the list ( without using any inbuilt function like max(),min())

Q3. Check whether the whole list is palindrome or not( eg. [1,2,1] gives yes for palindrome while [1,2,2] doesn't

Q4. Print the numbers which are palindrome inside the list



    if i%2 == 0:
        even+=1
    else:
        odd+=1
print("odd:{},even:{}".format(odd,even))

high = 0 
low = num[0]

for n in num:
    if n>high:
        high=n
print("max:",high)

for k in num:
    if low>k:
        low=k
print("min:",low)

palindromes = []
for t in num:
    t = str(t)
    print(t[::-1])
    if t == t[::-1]:
        print("It is a palindrome")
        palindromes.append(t)
    else:
        print("It is not a palindrome")
print("the numbers which are palindrome are:{}".format(palindromes))    
                                                      
