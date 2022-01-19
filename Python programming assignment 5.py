#!/usr/bin/env python
# coding: utf-8

# PYTHON BASIC PROGRAMMING ASSIGNMENT 5

# FIND LCM

# In[2]:


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x >y:
    a = x
else :
    a = y
l = []    
for i in range(2,a):
    for j in range(i):
        if x * i ==  y * j:
            g=int(x*i)
            l.append(g)
print("The LCM of ",x ,"and ",y ,"is",min(l))
       


# FIND HCF

# In[3]:


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x >y:
    a = x
else :
    a = y
l=[]    
for i in range(2,a):
    if x % i == 0 and  y % i ==0 :
        g=int(i)
        l.append(g)
print("The HCF of ",x ,"and ",y ,"is",max(l))


# CONVERT DECIMAL TO BINARY

# In[4]:


a=int(input("Enter number:"))
b=[]
while a>0:
    c=a%2
    b.append(c)
    a=a//2    
b=b[::-1]

for i in b:
    print(i,end="")


# CONVERT DECIMAL TO OCTAL

# In[5]:


a=int(input("Enter number:"))
b=[]
while a>0:
    c=a%8
    b.append(c)
    a=a//8 
b=b[::-1]

for i in b:
    print(i,end="")


# CONVERT DECIMAL TO HEXADECIMAL

# In[6]:


a=int(input("Enter number:"))
b=[]
while a>0:
    c=a%16
    b.append(c)
    a=a//16
b=b[::-1]

for i in b:
    print(i,end="")


# ASCII VALUE TO CHARACTER

# In[7]:


Char = input("Enter Character: ")
print(ord(Char))


# MATHEMATICAL CALCULATOR

# In[8]:


Operations=input('choose:(+,-,*,/):')
a=int(input('Enter number:'))
b=int(input('Enter number:'))
if Operations=="+":
    print(a+b)
elif Operations=="-":
    print(a-b)
elif Operations=="*":
    print(a*b)
else:
    print(a/b)


# In[ ]:




