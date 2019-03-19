import sqlite3
import datetime
import time
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial3.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def display_table() :
    c.execute('SELECT * FROM stuffToPlot')
    for row in c.fetchall():
        print(row)


def graph_data() :
    c.execute('SELECT unix, value FROM stuffToPlot')
    data = c.fetchall()
    dates = []
    values = []
    for row in data :
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('UPDATE stuffToPlot SET keyword="C++" WHERE value=8.0')
    conn.commit()
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]
    #The above line is called one liner or one line for loop
    #Also referred to as list comprehension
    print(50*'#')
    c.execute('DELETE FROM stuffToPlot WHERE keyword="C++"')
    conn.commit()
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]
    
    
##create_table()
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)
#display_table()
##graph_data()
del_and_update()
c.close()
conn.close()




"""
OUTPUT
_________________________________________________________

(1552638100.702875, '2019-03-15 13:51:40', 'C++', 8.0)
(1552638101.7874396, '2019-03-15 13:51:41', 'Python', 9.0)
(1552638102.8790672, '2019-03-15 13:51:42', 'Python', 3.0)
(1552638103.9998434, '2019-03-15 13:51:43', 'C++', 8.0)
(1552638105.150459, '2019-03-15 13:51:45', 'Python', 6.0)
(1552638106.27699, '2019-03-15 13:51:46', 'C++', 8.0)
(1552638107.3891416, '2019-03-15 13:51:47', 'Python', 0.0)
(1552638108.4538522, '2019-03-15 13:51:48', 'Python', 0.0)
(1552638109.570014, '2019-03-15 13:51:49', 'Python', 1.0)
(1552638110.6691718, '2019-03-15 13:51:50', 'Python', 6.0)
(1552638251.3835404, '2019-03-15 13:54:11', 'Python', 0.0)
(1552638252.4890552, '2019-03-15 13:54:12', 'Python', 6.0)
(1552638253.6715872, '2019-03-15 13:54:13', 'Python', 6.0)
(1552638254.828853, '2019-03-15 13:54:14', 'Python', 4.0)
(1552638255.900229, '2019-03-15 13:54:15', 'Python', 0.0)
(1552638256.9698079, '2019-03-15 13:54:16', 'Python', 9.0)
(1552638258.0534103, '2019-03-15 13:54:18', 'Python', 2.0)
(1552638259.1291347, '2019-03-15 13:54:19', 'C++', 8.0)
(1552638260.226016, '2019-03-15 13:54:20', 'Python', 1.0)
(1552638262.2271311, '2019-03-15 13:54:22', 'C++', 8.0)
(1552638360.1627703, '2019-03-15 13:56:00', 'Python', 7.0)
(1552638361.2624288, '2019-03-15 13:56:01', 'Python', 9.0)
(1552638362.3477745, '2019-03-15 13:56:02', 'Python', 7.0)
(1552638363.4346094, '2019-03-15 13:56:03', 'Python', 5.0)
(1552638364.5564897, '2019-03-15 13:56:04', 'Python', 1.0)
(1552638365.6801066, '2019-03-15 13:56:05', 'Python', 0.0)
(1552638366.8049898, '2019-03-15 13:56:06', 'Python', 4.0)
(1552638367.9035609, '2019-03-15 13:56:07', 'Python', 6.0)
(1552638369.117085, '2019-03-15 13:56:09', 'Python', 0.0)
(1552638370.4665222, '2019-03-15 13:56:10', 'Python', 3.0)
##################################################
(1552638101.7874396, '2019-03-15 13:51:41', 'Python', 9.0)
(1552638102.8790672, '2019-03-15 13:51:42', 'Python', 3.0)
(1552638105.150459, '2019-03-15 13:51:45', 'Python', 6.0)
(1552638107.3891416, '2019-03-15 13:51:47', 'Python', 0.0)
(1552638108.4538522, '2019-03-15 13:51:48', 'Python', 0.0)
(1552638109.570014, '2019-03-15 13:51:49', 'Python', 1.0)
(1552638110.6691718, '2019-03-15 13:51:50', 'Python', 6.0)
(1552638251.3835404, '2019-03-15 13:54:11', 'Python', 0.0)
(1552638252.4890552, '2019-03-15 13:54:12', 'Python', 6.0)
(1552638253.6715872, '2019-03-15 13:54:13', 'Python', 6.0)
(1552638254.828853, '2019-03-15 13:54:14', 'Python', 4.0)
(1552638255.900229, '2019-03-15 13:54:15', 'Python', 0.0)
(1552638256.9698079, '2019-03-15 13:54:16', 'Python', 9.0)
(1552638258.0534103, '2019-03-15 13:54:18', 'Python', 2.0)
(1552638260.226016, '2019-03-15 13:54:20', 'Python', 1.0)
(1552638360.1627703, '2019-03-15 13:56:00', 'Python', 7.0)
(1552638361.2624288, '2019-03-15 13:56:01', 'Python', 9.0)
(1552638362.3477745, '2019-03-15 13:56:02', 'Python', 7.0)
(1552638363.4346094, '2019-03-15 13:56:03', 'Python', 5.0)
(1552638364.5564897, '2019-03-15 13:56:04', 'Python', 1.0)
(1552638365.6801066, '2019-03-15 13:56:05', 'Python', 0.0)
(1552638366.8049898, '2019-03-15 13:56:06', 'Python', 4.0)
(1552638367.9035609, '2019-03-15 13:56:07', 'Python', 6.0)
(1552638369.117085, '2019-03-15 13:56:09', 'Python', 0.0)
(1552638370.4665222, '2019-03-15 13:56:10', 'Python', 3.0)
"""
            


    
