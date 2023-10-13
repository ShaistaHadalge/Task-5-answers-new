#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Create a pyramid of numbers from 1 to 20 using for loop##


# In[11]:


for i in range(1 , 21):
    for j in range (21 - i):
         print(" ", end = " ")
    for j in range(1, i ):
        print(j, end = " ")
    for i in range(i , 0, -1):
        print(i, end = " ")
        
    print("\n") 
            
    


# In[19]:


##Write a python programme to calculate the total number of vowels and count of each individual vowel A,E,I,O,U in 
##Guvi Geeks Network India Private Limited##


# In[7]:


str=input("Enter String")
str=str.lower()
vowels="aeiouAEIOU"
d=dict()
d=d.fromkeys(vowel,0)
for char in str:
    if char in vowels:
        d[char]+=1
        print(d)


# In[ ]:


##Write a function that takes a string and returns a new string with all the vowels removed##


# In[3]:


str =input("Enter the string")
vowel_string= "aeiouAEIOU"

print("input string",str)
for char in str:
    if char in vowel_string:
        str=str.replace(char,"")

print("Output string without vowels",str)


# In[ ]:


##Write a function that takes a string and returns the number of unique characters in it##


# In[4]:


str=input("Enter String")
#print(str)
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d=dict(zip(l,freq))
print(d)


# In[ ]:


##Write a function that takes a string and returns true if it is Palindrome,False otherwise##


# In[5]:


str=input("Enter String")
rev_str=""
for char in str:
     rev_str=char+rev_str
print("Reverse of given string",str,"is",rev_str)
if str==rev_str:
    print("True")
else:
    print("False")


# In[1]:


str=input("Enter String")
rev_str=""
for char in str:
     rev_str=char+rev_str
print("Reverse of given string",str,"is",rev_str)
if str==rev_str:
    print("True")
else:
    print("False")


# In[6]:


##Write a function that takes a string and returns true if it is an anagram of another string,false otherwise##


# In[11]:


str1 =input("Enter string1")
str2 =input("Enter string2")

if len(str1)!=len(str2):
    print("Not Anagram")
else: 
    if sorted(str1)==sorted(str2):
        print("Strings are anagram")
    else: 
        print("Not Anagram")


# In[12]:


str1 =input("Enter string1")
str2 =input("Enter string2")

if len(str1)!=len(str2):
    print("Not Anagram")
else: 
    if sorted(str1)==sorted(str2):
        print("Strings are anagram")
    else: 
        print("Not Anagram")
    


# In[13]:


##Write a function that takes a string and rerurns the number of words in it##


# In[14]:


s=len(input("Enter a string:").split())
print(s)


# In[1]:


##Write a function that takes two strings and returns the longest common substring between them###


# In[5]:


str1=("Guvi Geeks")
str2=("India Private Limited")
print(str1+" "+str2)


# In[ ]:




