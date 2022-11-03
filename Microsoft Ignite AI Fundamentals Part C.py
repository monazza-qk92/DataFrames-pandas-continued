#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)


# In[2]:


import numpy as np

grades = np.array(data)
print(grades)


# In[3]:


# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
student_data


# In[4]:


import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

df_students 


# In[5]:


get_ipython().system('wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv')
df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
df_students.head()


# In[6]:


df_students.isnull()


# In[7]:


df_students.isnull().sum()


# In[8]:


df_students[df_students.isnull().any(axis=1)]


# In[9]:


df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
df_students


# In[10]:


df_students = df_students.dropna(axis=0, how='any')
df_students


# In[11]:


# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))


# In[12]:


# Get students who studied for the mean or more hours
df_students[df_students.StudyHours > mean_study]


# In[13]:


# What was their mean grade?
df_students[df_students.StudyHours > mean_study].Grade.mean()


# In[14]:


passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

df_students


# In[15]:


print(df_students.groupby(df_students.Pass).Name.count())


# In[16]:


print(df_students.groupby(df_students.Pass)['StudyHours', 'Grade'].mean())


# In[17]:


# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)

# Show the DataFrame
df_students


# In[ ]:




