
# coding: utf-8

# In[2]:


import numpy as np

import pandas as pd


# In[3]:


from pandasql import sqldf


# In[ ]:


import sqlite3
import pandas as pd
from pandas import DataFrame, Series

from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

sqladb = pd.read_csv("https://archive.ics.uci.edu//ml//machine-learning-databases//adult//")

#sqladb = pd.read_csv('adult.csv')

pysqldf("""sqlite3.connect('sqladb')""")

pysqldf("""CREATE TABLE adult (
            age   int,
            workclass   varchar(40),
            fnlwgt   int,
            education   varchar(40),
            education_num   int,
            marital_status   varchar(40),
            occupation   varchar(20),
            relationship   varchar(40),
            race   varchar(20),
            sex   varchar(10),
            capital_gain   int,
            capital_loss   int,
            hours_per_week   int,
            native_country   varchar(50),
            label    varchar(10))""")
#question 1
pysqldf("SELECT * FROM adult LIMIT 10;")

