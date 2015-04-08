import pandas as pd 
from numpy import random 
import matplotlib.pyplot as plt 
import sys 
from sqlalchemy import create_engine, MetaData, Table, select

d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['Number'])
print df 
print df.dtypes 
print df.tail()

print sys.version 
print pd.__version__

ServerName = "RepSer2"
Database = "BizIntel"
TableName = "DimDate"

engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database)
conn = engine.connect()

metadata = MetaData(conn)

tbl = Table(TableName, metadata, autoload=True, schema='dbo')

sql = tbl.select()

result = conn.execute(sql)

df = pd.DataFrame(data=list(result), columns=result.keys())

print df 

conn.close()

print 'done'









