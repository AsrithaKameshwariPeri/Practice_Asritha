import sqlite3
import pandas as pd

# creating file path
dbfile = 'c:/Users/14695/OneDrive/Desktop/Flask_practice/instance/site.db'
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# here is you table list
print(table_list)
df = pd.read_sql_query('SELECT * FROM profile', con)
print(df)
# Be sure to close the connection
con.close()