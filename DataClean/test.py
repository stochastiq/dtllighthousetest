# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:15:29 2018

@author: abiga
"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine


user = 'dtllighthouse'
password = 'dealsanalytics2018'
host = 'localhost'
db = 'abs'

connectionstring = user + ":" + password + "@" + host + "/" + db

engine = create_engine("mysql+pymysql://dtllighthouse:dealsanalytics2018@localhost/abs")
df=pd.DataFrame(['A','B'],columns=['new_tablecol'])
df.to_sql(name='new_table',con=engine,if_exists='append')




#import pymysql
#connection = pymysql.connect(host='127.0.0.1',
#                             user='dtllighthouse',
#                             password='dealsanalytics2018',
#                             db='abs')
