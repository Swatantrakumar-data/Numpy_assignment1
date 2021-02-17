#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# ### 1. Create a null vector of size 10 but the fifth value which is 1.

# In[7]:


x=np.zeros((1,10),int)
x[0][4]=1
x


# ### 2. Create a vector with values ranging from 10 to 49.

# In[33]:


np.arange(10,50)


# ###  3. Create a 3x3 matrix with values ranging from 0 to 8

# In[12]:


x = np.arange(9)
x.reshape((3,3))


# ###  4. Find indices of non-zero elements from [1,2,0,0,4,0]

# In[14]:


x = [1,2,0,0,4,0]
arr = np.array(x)
np.where(arr>0)


# In[19]:


# OR
  
x = [1,2,0,0,4,0]
for i in x:
  if i > 0 :
      print(x.index(i))


# ###  5. Create a 10x10 array with random values and find the minimum and maximum values.

# In[26]:


x = np.random.randint(0,100,size=(10,10))
print(x.min())
print(x.max())


# ###  6. Create a random vector of size 30 and find the mean value.

# In[32]:


x = np.random.randint(0,100,size=30)
x.mean()


# In[ ]:




