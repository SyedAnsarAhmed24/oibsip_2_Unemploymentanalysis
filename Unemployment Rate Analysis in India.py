#!/usr/bin/env python
# coding: utf-8

# # OASIS INFOBYTE SIP August Data Science Internship TASK 2
# Unemployment Rate Analysis in India Using Python

# In[24]:


# import libraries


# In[25]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
print("Libraries are imported")


# In[5]:


#read datasets


# In[26]:


data=pd.read_csv("C:\\Users\SYED ANSAR AHMED\\OneDrive\\Desktop\\Unemployment in India.csv")
data=pd.read_csv("C:\\Users\SYED ANSAR AHMED\OneDrive\\Desktop\\Unemployment_Rate_upto_11_2020.csv")
print(data.head())


# In[27]:


data.info


# In[28]:


print(data.describe)


# In[9]:


#checking whether dataset contains null values


# In[29]:


print(data.isnull().sum())


# In[11]:


#rename the column names


# In[31]:


data.columns=["States","Date","Frequency","Estimated Unemployment Rate","Estimated Employed",
              "Estimated Labour Participation Rate","Region","longitude","latitude"]


# In[32]:


print(data)


# In[14]:


#checking the correlation between the features


# In[15]:


plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(12,10))
sns.heatmap(data.corr())
plt.show()


# In[16]:


#checking for estimated number of ynemployment rates in different regions of india


# In[17]:


data.columns=["States","Date","Frequency","Estimated Unemployment Rate","Estimated Employed",
              "Estimated Labour Participation Rate","Region","longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed",hue="Region",data=data)
plt.show()


# In[18]:


# to display the unemployment rate according to different regions of india


# In[19]:


plt.figure(figsize=(12,10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate",hue="Region",data=data)
plt.show()


# In[20]:


sns.pairplot(data,hue="Region")


# In[21]:


#create a dashboard to analyse the unemployment rate of each Indian State by region by region


# In[33]:


unemployment=data[["States","Region","Estimated Unemployment Rate"]]
figure=px.sunburst(unemployment,path=["Region","States"],values="Estimated Unemployment Rate",width=700,height=700,
                  color_continuous_scale="RDY1GN",title="Unemployment Rate in India")
figure.show() 


# In[ ]:





# In[ ]:




