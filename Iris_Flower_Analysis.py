
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


iris_data = pd.read_csv('iris.csv', index_col="Id")


# In[3]:


iris_data.head()


# In[4]:


sns.distplot(a=iris_data['Petal Length (cm)'], kde=False) #histogram data


# In[5]:


# KDE plot 
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)


# In[6]:


# 2D KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")


# In[7]:


iris_set_data = pd.read_csv('iris_setosa.csv', index_col="Id")
iris_ver_data = pd.read_csv('iris_versicolor.csv', index_col="Id")
iris_vir_data = pd.read_csv('iris_virginica.csv', index_col="Id")


# In[8]:


iris_set_data.head()


# In[9]:


iris_ver_data.tail()
iris_vir_data.tail()


# In[10]:


sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)
import matplotlib.pyplot as plt
plt.title("Histogram of Petal Lengths, by Species")
plt.legend()

