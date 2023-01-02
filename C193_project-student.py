#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Name : Ziyah Virani//Fierce Bird')
print('Plot a line graph to find the average cholestrol found in various age groups')
print('Plot a line graph to find the correlation between systolic and diastolic blood pressure found in various age groups')


# In[2]:


#Task 1 
#Import all the libraries and read cardiovascular.csv
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('cardiovascular.csv')
df


# # Average cholestrol found in various age groups

# In[3]:


#Task 2 
#Group by age and find the average cholesterol and make a dataframe out of it
group_by_age= df.groupby('age')['cholesterol'].mean().reset_index(name='cholesterol')
print(group_by_age)


# In[4]:


#Task 3 
#Plot a line graph for various age group and their cholesterol 
label = group_by_age['age']
value = group_by_age['cholesterol']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Average Cholesterol as per AGE" , linewidth=3.0)
plt.xlabel("AGE")
plt.xticks(rotation='vertical')

plt.ylabel('Cholesterol')

plt.title('Average Cholesterol as per AGE', fontsize=20)

plt.legend()

plt.show()


# Conclusion - 

# # Correlation between systolic and diastolic blood pressure

# In[7]:


# Diastolic blood pressure - is the pressure in the arteries when the heart rests between beats
# Systolic blood pressure - the pressure in your arteries when your heart beats

#predefine code for image
from IPython.display import Image
Image(filename='blood pressure readings chart.jpg') 
#predefine code end


# In[8]:


#Task 4
#Group by age and find maximum systolic blood pressure and create a dataframe project out of it
group_by_age2=df.groupby('age')['systolic_blood_pressure'].max().reset_index(name='systolic_blood_pressure')
print(group_by_age2)


# In[11]:


#Task 5
#Group by age and find maximum diastolic blood pressure and create a dataframe project out of it
group_by_age3 = df.groupby('age')['diastolic_blood_pressure'].max().reset_index(name='diastolic_blood_pressure')
print(group_by_age3)


# In[13]:


#Task 6
#Plot a line graph to show a Correlation between systolic and diastolic blood pressure
label = group_by_age2['age']
value = group_by_age2['systolic_blood_pressure']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Systolic Blood Pressure as per AGE" , linewidth=3.0)

#---------------------------------------------------------------

label = group_by_age3['age']
value = group_by_age3['diastolic_blood_pressure']
plt.plot(label, value, label = "Diastolic Blood Pressure as per AGE" , linewidth=3.0)

#----------------------------------------------------------------
plt.xlabel("AGE")
plt.xticks(rotation='vertical')

plt.ylabel('Blood Pressure ')

plt.title('Blood Pressure as per AGE', fontsize=20)

plt.legend()

plt.show()


# Conclusion - 

# In[ ]:




