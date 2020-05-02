import sqlite3 as db
from pyecharts.charts import Page,Pie
from pyecharts import options as opts
conn = db.connect('yanzhao.db')
cur =conn.cursor()
a = cur.execute('select city,count(*) from xuejiyx group by city;')
s =a.fetchall()
v1=[]
v2=[]
for each in s:
    v1.append(each[0])
    v2.append(each[1])
def pie_Base():
    p=(
        Pie()
        .add('',[list(z) for z in zip(v1,v2)],center=["30%", "70%"])
        .set_global_opts(title_opts=opts.TitleOpts('各省计算机学硕院校占比'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}%'),)

    )
    return p
pie_Base().render('饼状图.html')
