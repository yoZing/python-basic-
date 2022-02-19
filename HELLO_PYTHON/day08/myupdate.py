import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

# data = (
#     ('4', '4', '4', '4'),
#     ('5', '5', '5', '5')
#     )
e_id = 6
e_name = 6
sex = 6
age = 6
sql = f"""insert into emp(e_id,e_name,sex,age) values('{e_id}','{e_name}','{sex}','{age}')"""

cnt = curs.execute(sql)
print(cnt)

conn.commit()

conn.close()