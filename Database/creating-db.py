# import pandas as pd
# import sqlite3
# import pathlib

# data=pd.read_csv('../data-collection/canadian_immegration_data.csv')

# #create database
# con=sqlite3.connect('../Database/immigration')
# cur=con.cursor()

# #create table
# create_table=  """CREATE TABLE canada(
#                         Country TEXT,
#                         Continent TEXT,
#                         Region TEXT,
#                         DevName TEXT,
#                         "1980" integer,
#                         "1981" integer,
#                         "1982" integer,
#                         "1983" integer,
#                         "1984" integer,
#                         "1985" integer,
#                         "1986" integer,
#                         "1987" integer,
#                         "1988" integer,
#                         "1989" integer,
#                         "1990" integer,
#                         "1991" integer,
#                         "1992" integer,
#                         "1993" integer,
#                         "1994" integer,
#                         "1995" integer,
#                         "1996" integer,
#                         "1997" integer,
#                         "1998" integer,
#                         "1999" integer,
#                         "2000" integer,
#                         "2001" integer,
#                         "2002" integer,
#                         "2003" integer,
#                         "2004" integer,
#                         "2005" integer,
#                         "2006" integer,
#                         "2007" integer,
#                         "2008" integer,
#                         "2009" integer,
#                         "2010" integer,
#                         "2011" integer,
#                         "2012" integer,
#                         "2013" integer
#                         );

#                 """

# cur.execute(create_table)

# path=pathlib.Path().cwd()  

# def create_db (db_name,filename,table_name): 
#     folder_data = 'data-collection'
#     file_path = Path(folder_data) / filename
#     # file_path=path/filename  
#     con=sqlite3.connect(db_name)
#     cursor=con.cursor()
#     cur.execute(f'drop table {table_name}')
#     data=pd.read_csv(file_path) 
#     data.to_sql(table_name,con,index=False,if_exists='replace') 
#     results=cursor.execute(f'select*from {table_name}').fetchall()
#     print(results)
#     con.commit() 
#     con.close()
    
# if __name__=="__main__":
#     db_name="immigration.db"
#     filename="canadian_immegration_data.csv"
#     tablename="canada"
#     create_db(db_name,filename,tablename)



from pathlib import Path
import sqlite3
import pandas as pd

def create_db(db_name, filename, table_name):
    folder_data = 'data-collection'
    file_path = Path(folder_data) / filename
    print(file_path) # create a path to the data file

    # folder_db = '../Database'
    folder_db = 'Database'
    db_path = Path(folder_db) / db_name
    con = sqlite3.connect(db_path) # create a connection to the database
    cursor = con.cursor() # create a cursor

    data_titanic = pd.read_csv(file_path) # read in the data 
    # insert the data into the specified table 
    data_titanic.to_sql(table_name,con, index = False, if_exists='replace')

    # execute a select statement as f-string and print results to verify insertion
    executing_db = f"SELECT * FROM {table_name}"
    result = cursor.execute(executing_db).fetchall()
    print(result)
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()

if __name__=="__main__":
    db_name = "immigration.db"
    filename = "canadian_immegration_data.csv"
    table_name = "canada"
    create_db(db_name, filename, table_name)