import sqlite3 as db
from pyecharts.charts import Page,Pie
from pyecharts import options as opts

conn = db.connect('yanzhao.db')
cur =conn.cursor()
a = cur.execute('select shengfen,nizhaorenshu from xuejizy;')
s =a.fetchall()
print(s)
hh= []
for i in s:
    if(i[1][3]>='0'and i[1][3]<='9'):
        if(i[1][4]>='0'and i[1][4]<='9'):
            b=i[1][3:5]
        else:
            b=i[1][3]
    else:
        b=i[1][5]

print(hh)