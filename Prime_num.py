#!/usr/bin/env python
# coding: utf-8

# In[5]:


# write a python Program Fiboncce series

n = int(input("Enter the vale = :- "))
x = 0
y = 1
z = 0 
while n>z:
    print(z)
    x = y
    y = z
    z = x+y


# In[20]:


# write a python Program prime number 
i = int(input("Enter the number = :- "))
count = 0
n = 1
while i>=n:
    if i%n==0:
        count=count+1
    n=n+1
if count==2:
    print("This is Prime number ",i)
else:
    print("This not Prime numebr",i)


# In[ ]:




