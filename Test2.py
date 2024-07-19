#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TASK 1
##1.Write a function `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence and returns them as a list. (10 Marks)


# In[45]:


def fibonacci(num):  ## function fibonacci is defined here with the arguement num
    if num < 0:
        print("Invalid input. Please enter a non-negative number.")
    else:
        a, b = 0, 1
    if num >= 1:
        print(a)
        if num >= 2:
            print(b)
            for i in range(2, num):
                c = a + b
                print(c)
                a, b = b, c 
                
    return
num = int(input("Enter the number of terms for the Fibonacci sequence: ")) ## the input() receives the data and int() converts it into integer and stored the variable num
fibonacci(num)


# In[ ]:


# 2. Write a function `is_prime(num)` that checks if a given number is a prime number. Return `True` if the number is prime, otherwise return `False`. (10 Marks)


# In[19]:


def prime(num):
    if num <= 1:
        return False  # 1 and less are not prime
    if num <= 3:
        return True  # 2 and 3 are prime
    if num % 2 == 0 or num % 3 == 0:
        return False

  # Only check for divisibility by odd numbers from 5 to sqrt(num)
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
    i += 6

    return True
num = int(input("Enter the number : "))
prime(num)


# In[ ]:


# TASK 2 - PANDAS


# In[20]:


##Task 2: Data Manipulation with Pandas (30 Marks)
##Using the dataset provided below, perform the following tasks. The dataset contains information about a company's sales.
 


# In[ ]:


# 1. Load the dataset into a pandas DataFrame and display its first 5 rows. (5 Marks


# In[24]:


import pandas as pd
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Sales': [200, 220, 210, 215, 225],
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Manager': ['John', 'Jane', 'Joe', 'Jake', 'John']}
df = pd.DataFrame(data)
df


# In[25]:


df.head()


# In[26]:


## 2. Add a new column `Profit` which is 10% of the `Sales` column. (5 Marks)


# In[27]:


df["Profit"] = df['Sales'] * 10/100


# In[28]:


df


# In[29]:


##3.Group the data by `Region` and calculate the total sales for each region.


# In[30]:


total_sales_by_region = df.groupby('Region')['Sales'].sum()

print(total_sales_by_region)


# In[32]:


## 4. 4. Find the region with the highest average sales. (10 Marks


# In[43]:


avg_sales = df.groupby('Region')['Sales'].mean()
avg_sales
highest = avg_sales.idxmax()
print(highest,avg_sales)


# In[44]:


##Task 3: Data Loading and Manipulation from GitHub (10 Marks


# In[46]:


import pandas as pd


# In[47]:


## Load a CSV file from a GitHub repository into a pandas DataFrame. Use the following URL for the dataset:


# In[48]:


titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")


# In[49]:


titanic


# In[50]:


titanic.head()


# In[51]:


## Display summary statistics of the DataFrame.


# In[53]:


titanic.shape


# In[54]:


##Check for null values in the DataFrame and display the count of null values in each column. 


# In[55]:


titanic.isnull().sum()


# In[56]:


##Fill the null values in the 'Age' column with the mean age.


# In[57]:


titanic['Age'].fillna(titanic['Age'].mean(),inplace=True)


# In[58]:


titanic


# In[59]:


titanic.isnull().sum()


# In[60]:


## Drop the rows where 'Embarked' is null.


# In[61]:


titanic = titanic["Embarked"].dropna(axis = 0)


# In[63]:


titanic


# In[64]:


##Create a new column 'FamilySize' which is the sum of 'SibSp' and 'Parch'. (1 Mark)


# In[68]:


titanic['FamilySize'] = titanic['SibSp'] + titanic['Parch']
titanic


# In[ ]:


# Convert the 'Sex' column to numerical values (male: 0, female: 1)


# In[77]:


nsex = {"male": 0, "female": 1}
titanic['Sex'] = titanic['Sex'].replace(nsex)
del titanic['Sexnum']
titanic


# In[69]:


#Group the data by 'Pclass' and calculate the average fare for each class.


# In[73]:


titanic.groupby('Pclass')['Pclass'].mean()


# In[75]:


## Find the most common port of embarkation ('Embarked' column).


# In[82]:


titanic['Embarked'].mode()[0]


# In[83]:


## Create a pivot table that shows the survival rate ('Survived') for each combination of 'Sex' and 'Pclass'. (1 Mark)End of Assessmen


# In[84]:


titanic['Survived'].unique()


# In[ ]:




