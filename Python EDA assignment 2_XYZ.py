#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string


# # 1. All Red
# 
# Description
# 
# Build a function AllRed that takes a list of strings as input, returns a boolean indicating whether all the strings containing word "red".

# In[6]:


def Allred(list):
    n = 0
    for i in list: # if number of 'red' element equal to full length of list, return true
        if i.str.contain('red'):
            n = n+1
        else: 
            break
    return(lambda n,len(list):n==len(list)) # no idea why this doesnt work, w/wo return


# ## solution #2

# In[2]:


# if any member of list dont have 'red', return false
def Allred2(list):
    for item in list:
        if str(item).find('red') == -1:
            res = 'false'
            break
        else:
            res = 'true'
    print(res)


# In[ ]:


Allred2(["red hat"
         , "a pair of red shoes"
         , "three red apples"
        ])


# # 2. Reverse String
# 
# Description
# 
# Build a function RevStr to reverse a string.

# In[40]:


def RevStr(string):
    print(string[::-1])


# In[ ]:


RevStr('waishizaohuazhongdexinyuan')


# # 3. Reverse Sentence
# 
# Description
# 
# Build a function RevSen to reverse a sentence.

# In[82]:


def revsen(sent):
    sent = sent.replace(',',' ,')
    words = sent.split()
    rev_words = words[::-1]
    rev_sent = ' '.join(rev_words)
    rev_sent = rev_sent.replace(' ,',',') #might need to write a spearate function just  to list all other punctuations
    print(rev_sent)


# In[83]:


revsen('wai shi zao hua, zhong de xin yuan')


# # 4. Reverse Words
# 
# Description
# 
# Build a function RevWords to reverse each word of a sentence.

# In[84]:


def revword(sent):
    sent = sent.replace(',',' ,')
    words = sent.split()
    rev_words = [i[::-1] for i in words]
    rev_sent = ' '.join(rev_words)
    rev_sent = rev_sent.replace(' ,',',')
    print(rev_sent)
    


# In[85]:


revword('wai shi zao hua, zhong de xin yuan')


# # 5. Capitalize First Letters
# 
# Description
# 
# Build a function CapLett to capitalize the first letter of each word in a sentence.

# In[86]:


def caplett(sent):
    words = sent.split()
    cap_words = [i.capitalize() for i in words]
    cap_sent = ' '.join(cap_words)
    print(cap_sent)


# In[87]:


caplett('wai shi zao hua, zhong de xin yuan')


# # 6. Remove Punctuations
# 
# Description
# 
# Build a function RmPunct to remove punctuations from a string.

# In[124]:


def rmpunct(sent):
#     import string
    punct = string.punctuation # this makes no sense, shouldn't this be punct  = sent.punctuation  ?
    nopunct_sent = ''.join(i for i in sent if i not in punct)
    print(nopunct_sent)


# In[125]:


rmpunct('wai shi zao hua, zhong de xin yuan')


# # 7. N Grams
# 
# Description
# 
# Build a function NGram which takes a string s and an integer n as inputs, returns a list of n grams of s.# 7. N Grams
# 
# Description
# 
# Build a function NGram which takes a string s and an integer n as inputs, returns a list of n grams of s.

# In[138]:


def ngram(sent,n):
    punct = string.punctuation # this makes no sense, shouldn't this be punct  = sent.punctuation  ?
    nopunct_sent = ''.join(i for i in sent if i not in punct)
    words = nopunct_sent.split() #words is a list
    ngram = [] #ngram is a list, good
    for i in range(len(words)-n+1):
        gram = words[i:i+n] # now gram is one element(string) 
        gram = ''.join(gram) #gram is still one element(string)
        ngram.append(gram)
    return ngram


# In[139]:


ngram('wai shi zao hua, zhong de xin yuan', 3)


# # 8. Palindrome
# 
# Description
# 
# Build a function isPalindrome which takes a string as an input and returns boolin value telling whether the string is a palindrome.# 

# In[6]:


# def ispalindrome(string): #something off, code cant be reached
#     n=1
#     res = 'true'
#     while n <= len(string)/2:
#         if string[n-1] == string[-n]:
#             continue
#         else:
#             res = 'false'
#             break
#         n = n+1    
#     print(res)


# In[8]:


# ispalindrome('aba') # no idea why this doesbnt return anything and takes a loooooooong time to run


# # 9. Valid Parenthesis
# 
# Description
# 
# Build a function isValid to determine the parenthesis in a string are valid.

# In[ ]:


def isValid(s): # something wrog with the loop, it  takes for ever to run  therefore hard to debug
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack:
                return False
            else:
                last_char = stack.pop()
                if (char == ")" and last_char != "(") or /
                (char == "]" and last_char != "[") or /
                (char == "}" and last_char != "{"):
                    return False
    return not stack

