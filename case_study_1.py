# -*- coding: utf-8 -*-
"""Case Study 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19ZuRgIva314x-CPVkDvpzV9nsERR4l_m
"""

# Import Data Manipulation Library
import numpy as np
import pandas as pd

# Import Data Visualization Library
import seaborn as sns
import matplotlib.pyplot as plt

# Import FilterWarning library
import warnings
warnings.filterwarnings('ignore')

# Import Data Logging
import logging
logging.basicConfig(level = logging.INFO,
                    filename = 'app.log',
                    filemode = 'w',
                    format = '%(asctime)s - %(levelname)s - %(message)s') # 3F and 1 L

# Import Data using pandas Function

url = 'https://raw.githubusercontent.com/chandanc5525/Dataset/refs/heads/main/Data/titanic_train.csv'

data = pd.read_csv(url)
data.sample(frac = 1)

# Understanding Data Information
print(data.info())

# Identify passenger Class based on Category
data['Pclass'].value_counts()

# Distribution of passenger Class based on Category
data['Pclass'].value_counts().plot(kind = 'pie', autopct = '%.2f',explode = [0.02,0.02,0.02],figsize = (5,5))
plt.title('Passenger Class Distribution')
plt.legend(['First class','Second Class', 'Third Class'])
plt.show()

# Distribution of passenger Class based on Category
data['Parch'].value_counts().plot(kind = 'barh')
plt.title('Passenger Class Distribution')
plt.show()

# Distribution of Embarked based on Category
data['Embarked'].value_counts().plot(kind = 'pie', autopct = '%.2f',explode = [0.02,0.02,0.02],figsize = (5,5))
plt.title('Passenger Board their journey')
plt.show()

# Dataset belongs to Embarked = Southampton [S]
southampton = data[data['Embarked'] == 'S']
print(southampton)

southampton['Sex'].value_counts()

southampton[southampton['Sex'] == 'male']['Survived'].value_counts()

southampton[southampton['Sex'] == 'female']['Survived'].value_counts()

southampton['Age'].mean()

Queenstown = data[data['Embarked'] == 'Q']
print(Queenstown)

Queenstown[Queenstown['Sex'] == 'male']['Survived'].value_counts()

Queenstown[Queenstown['Sex'] == 'female']['Survived'].value_counts()

Queenstown['Age'].mean()

data[data['Pclass'] == 3 ]['Survived'].value_counts()

data[data['Pclass'] == 1 ]['Survived'].value_counts()

data[data['Pclass'] == 2 ]['Survived'].value_counts()

crosstab = pd.crosstab(southampton['Pclass'],southampton['Survived'])
print(crosstab)

crosstab = pd.crosstab(Queenstown['Pclass'],Queenstown['Survived'])
print(crosstab)

crosstab = pd.crosstab(['Pclass'],southampton['Survived'])
print(crosstab)

fig,ax = plt.subplots(2,2,figsize = (6,6))
sns.scatterplot(ax=ax[0][0],data=data,x = 'Parch',y = 'Pclass',hue= 'Survived')
sns.barplot(ax=ax[0][1],data=data,x = 'Embarked',y = 'Pclass')
sns.plot(ax=ax[1][0],data=data,x = 'Parch',y = 'Pclass')
sns.scatterplot(ax=ax[1][1],data=data,x = 'Parch',y = 'Pclass')

plt.show()

"""Data Insights :

The give dataset contains 12 columns and 891 rows out of which column name Age and Cabin found some missing values. The stratergies can be decided based on the above dataset are as follows

1: If the column contains more than 5% of missing values then the imputation can be done with the help on median.

2: For cabin column. we find more values are missing that is the reason we must drop this column for further analysis.

3: The dataset also shows 55.11% passengers belongs to Class 3 ,
20.65% belongs to class 2 and 24.24% belongs to class 1.

4: It was found that 72.44% Boarded their journey from 'Southampton'. 8.66% Boarded their journey from 'Queenstown'. and 18.90% boarded their journey from 'Cherbourg'

5 : Considering the southampton the Boarding rate is 33.69% out of which males are 441 and females are 203. and the surviving males are 77 out of 441 and surviving females are 140 out of 203.


"""