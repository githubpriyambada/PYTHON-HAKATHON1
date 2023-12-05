#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd


# In[8]:


df_google_playstore_app=pd.read_csv("C:\PYTHON\googleplaystore.csv",nrows=1000)


# In[9]:


df_google_playstore_app.shape


# In[10]:


df_google_playstore_app


# In[13]:


x=df_google_playstore_app["Rating"]
y=df_google_playstore_app["Reviews"]


# In[18]:


plt.scatter(x,y)
plt.title=("google_playstore_app")
plt.ylabel("reviews")
plt.xlabel("rating")


# In[27]:


plt.figure(figsize=(16,9))
plt.scatter(x,y,color='r',marker='o',s=100,alpha=0.6,linewidth=10,edgecolor='g')
plt.title=("google_playstore_app")
plt.ylabel("reviews")
plt.xlabel("rating")


# In[ ]:




