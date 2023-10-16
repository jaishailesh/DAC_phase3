# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SJsfCWAb1NbqABbYdMqPqENEHkbzsrUC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
product=pd.read_csv("statsfinal.csv")
product

product.describe()

product.info()

x=product.drop("S-P2",axis=1)
y=product['S-P2']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=0)
x_train

x_train.shape

x_test.shape

y_train.shape

y_test.shape

y_test

x_test

display(product.drop_duplicates())