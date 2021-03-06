# -*- coding: utf-8 -*-
"""mushrooms knc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ul8bGzgnT8l-yEqSK7jizj4H8q4JWau1

# **import library**
"""

import pickle
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
np.random.seed(42)

"""# **load data**"""

#load data
load_data=pd.read_csv(r"/content/mushrooms.csv")

"""#view sample data"""

#print(load_data.head())

"""# **handel missing data**"""

#print(load_data.info())
#print(load_data.isna())

"""# ** map labled data **"""

X=load_data.drop('class',axis=1)
y=load_data['class']

"""# **convert letters to numbers**"""

Encoder_x=LabelEncoder()
for col in X.columns:
    X[col]=Encoder_x.fit_transform(X[col])
Encoder_y=LabelEncoder()
y=Encoder_y.fit_transform(y)

"""#**split data to train \ test**"""

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

"""#**choose model**"""

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)

"""#**train model**"""

model.fit(x_train,y_train)

"""# **validate modle**"""

print(model.score(x_train , y_train))
print(model.score(x_test , y_test))

"""#**save model**"""

pickle.dump(model , open(r"mushrooms.pkl","wb"))