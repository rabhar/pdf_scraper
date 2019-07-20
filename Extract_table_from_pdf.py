
# coding: utf-8

# In[237]:


import camelot
import pandas as pd


# In[238]:


tables = camelot.read_pdf('pdf_data.pdf', flavor = 'stream',pages='2,3,5,7,8')
tables


# In[239]:


#Storing raw tables
for table in range(tables.n):
    tables[table].to_csv("raw_table_" + str(table) + ".csv")


# ## cleansing tables using pandas

# In[240]:


#first table
df0 = tables[0].df

#set index 2 as columns and drop first 3 rows
df0.columns = df0.iloc[2]
df0.drop(df1.index[:3],inplace=True)
df0.to_csv("table_0.csv")


# In[241]:


#second Table is splitted into two tables so appending them 
df1 = tables[1].df
df2 = tables[2].df

#Removing index from table 2 and appending both tables
df2 = df2.drop(df2.index[0])
df2 = df1.append(df2)
df2.columns= df2.iloc[0]
df2.drop(df2.index[0])
df2.to_csv('table_1.csv')


# In[242]:


#remaining tables doesn't require any cleansing
tables[3].df.to_csv('table_2.csv')
tables[4].df.to_csv('table_3.csv')
tables[5].df.to_csv('table_4.csv')

