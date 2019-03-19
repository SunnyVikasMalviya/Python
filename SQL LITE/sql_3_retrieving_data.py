import sqlite3
import datetime
import time
import random


conn = sqlite3.connect('tutorial2.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1451255552.2834989, '2016-01-02', 'Python', 8)")
    c.execute("INSERT INTO stuffToPlot VALUES(1451255553.3573883, '2016-01-02', 'Python', 6)")
    c.execute("INSERT INTO stuffToPlot VALUES(1451255554.3503793, '2016-01-02', 'Python', 7)")
    c.execute("INSERT INTO stuffToPlot VALUES(1451255555.3537504, '2016-01-02', 'Python', 1)")
    conn.commit()
    #c.close()
    #conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    #data = c.fetchall()
    ##fetchone() can be used to retrieve a single row
    #for i in range(200):
    #    print(data[i])
    for row in c.fetchall():
        print(row)
    for row in c.fetchall() :
        print(row[3])

def delete_table() :
    c.execute("DROP TABLE stuffToPlot")
    print("Table deleted.")

    
create_table()
data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
read_from_db()


#delete_table()
c.close()
conn.close()
            


    
