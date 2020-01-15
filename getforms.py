import pandas as pds
import pymysql
import pyodbc
import psycopg2
#miscellaneous extra goodies for psycopg2
import psycopg2.extras
import os
import sqlalchemy as np
import numpy
from datetime import datetime
#x = datetime.today().strftime('%Y%m%d%H%M%S')
x = datetime.today().strftime('%Y%m%d')
# Uses Windows authentication on your laptops
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=sql2014;'
                      'Database=gogdbm_dev;'
                      'Trusted_Connection=yes;')

cursor = connection.cursor()
#Uses Windows authentication on your laptops. connection string (import psycopg2)
connection2 = psycopg2.connect(
    user="postgres",
    password="Ti16tans",
    host="127.0.0.1",
    port="5432",
    database="postgres")
cursor2 = connection2.cursor()

csvDF1 = {'column_name': [],
         'question_text': [],
         'question_description': [],        
         'valid_value': [], 
         'export_value': [],       
         'data_type': [],
         'format_type': [],         
         'field_size': [],
         'logic': [],
         'min_value': [],
         'max_value': [],
         'max_length': []}
csvDF2 = {'form_type': [],
         'form_id': [],
         'version':[],
         'web_label': [],
         'export_table': []
         }

#created tableName variable which gets filled in by the input
tableName = input("Please enter the name of the table you want information on: ")
version = input("Please enter the form version number: ")
#select statement from table that was choosen by the input statement 
query = ("""
SELECT  
    column_name,    
    data_type,   
    CASE DATA_TYPE WHEN  'date'     THEN 10
                   WHEN  'varchar'  THEN CHARACTER_MAXIMUM_LENGTH
                   WHEN  'char'     THEN CHARACTER_MAXIMUM_LENGTH
                   WHEN  'decimal'  THEN 10
                   WHEN  'real'     THEN 24
   END   
FROM 
  INFORMATION_SCHEMA.COLUMNS
WHERE    
   table_name = '%s';""" % tableName)
#runs the select statement
cursor.execute(query)
#fetches the data from the table
tables = cursor.fetchall()
#adding relatable column headers to our csvDF1
#loop to get all the data requested in the select and adds it to dataframe we call csvDF
for column in tables:
    csvDF1['column_name'].append(column[0]) 
    csvDF1['data_type'].append(column[1]) 
    csvDF1['field_size'].append(column[2])
    max_query = ("""select max(%s) from %s""") % (column[0], tableName) 
    
    #sql to get footer fields prefilled    
headerQuery = ("""
SELECT 
    question_text,    
    question_description,    
    valid_value,
    export_value,
    format_type,
    logic 
FROM 
    header""")
#runs the select statement
cursor2.execute(headerQuery)
#fetches the data from the table
header = cursor2.fetchall()
for data in header:
    csvDF1['question_text'].append(data[0])    
    csvDF1['question_description'].append(data[1])    
    csvDF1['valid_value'].append(data[2])
    csvDF1['export_value'].append(data[3])
    csvDF1['format_type'].append(data[4])
    csvDF1['logic'].append(data[5])     
    #sql to get minimum value from each column and formatted to get only what we need
    min_query = ("""select min(%s) from %s""") % (column[0], tableName)
    cursor.execute(min_query)
    mins = cursor.fetchall()
    #adding it to csvDF1 and formatted  ([0][0] given a list of lists value in the list at the 0 index and 0 value of 2nd list)
    csvDF1['min_value'].append(mins[0][0])
    #sql to get maximum value from each field and formatted to only get what we need
   
    cursor.execute(max_query)  
    maxes = cursor.fetchall()
    csvDF1['max_value'].append(maxes[0][0])
#sql to get the maximum number of characters in the field and formated
    maxlength_query = ("""
    select 
        len(cast(max(%s) AS VARCHAR)) 
    from 
         %s""") % (column[0], 
        tableName)
    cursor.execute(maxlength_query)
    maxlengths = cursor.fetchall()
    csvDF1['max_length'].append(maxlengths[0][0])
joinQuery = (""" 
SELECT 
    teleforms.formlabel,
    teleforms.form_id,    
    teleforms.web_label, 
    teleforms.datatable1
FROM 
    teleforms 
INNER JOIN %s ON CAST(teleforms.form_id AS CHAR) = CAST(%s.form_id AS CHAR);
""" % (tableName, tableName))
cursor.execute(joinQuery)
joinResults = cursor.fetchmany() 
for data in joinResults:
    csvDF2['form_type'].append(data[0])    
    csvDF2['form_id'].append(data[1])    
    csvDF2['web_label'].append(data[2])
    csvDF2['export_table'].append(data[3])
    csvDF2['version'].append(version)

max_length = 1
for k, v in csvDF1.items():
  if len(v) > max_length:
    max_length = len(v)
for k, v in csvDF1.items():
  if len(v) == 0:
    csvDF1[k] = ["" for i in range(max_length)]
  elif len(v) != max_length:
    v += ["" for i in range(max_length, max_length - len(v), 1)] 
print(max_length)
#renaming dataframe
df1 = pds.DataFrame(csvDF1)
df2 = pds.DataFrame(csvDF2)
print(max_length)
print(__________________________________________)
print(df1)
#create a helper row to connect the two dataframes to start on the same
id=0
for i in df1.index:
    df1.loc[i,'id']=id
    id=id
for i in df2.index:
    df2.loc[i,'id']=id
    id=id

df3 = df2.merge(df1,on='id',how='outer', sort=False)
#getting the filename with the tablename from the input 
fileName = tableName
#variable to hold the path to where the csv file will go 
path ='DataTables'
#if not os.path.exists(tableName):
try:
    dirName =  path + '/' + fileName   
    os.makedirs(dirName)
    export_csv = df5.to_csv(dirName  + '/' + fileName + '_' + x + '.csv', index=None, header=True)
except FileExistsError:
    path =  path + '/' + fileName
    export_csv = df3.to_csv(path  + '/' + fileName + '_' + x + '.csv', index=None, header=True)

'''
# Pulling out individual elements from each row 
# This makes all of the columns strings. This MIGHT cause an issue when
# inserting into the DB if the data type of the column isn't a char/varchar
#the columns will need to cast to the correct type
for column in df3.columns:
        df3[column] = df3[column].astype(str)   
sql= """insert into forminfo(
            id, 
            form_type, 
            form_id,
            form_ver,
            web_label, 
            export_table, 
            column_name, 
            question_text,
            question_description,
            validvalue,
            export_value
            data_type,
            format_type
            field_size,
            logic,              
            min_value, 
            max_value, 
            max_length)
		values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

for index, row in df3.iterrows():
    data = (id, 
            row.form_type,
            row.form_id,
            version,
            row.web_label,
            row.export_table,
            row.column_name,            
            row.data_type,
            row.field_size,             
            row.min_value,
            row.max_value,
            row.max_length)
    cursor2.execute(sql,data)
connection2.commit()
'''
#close connections
cursor.close()
connection.close()
cursor2.close()