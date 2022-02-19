import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

e_id = 6
e_name = 7
sex = 7
age = 7

sql = f""" delete from emp
            where e_id = '{e_id}'
        """

cnt = curs.execute(sql)
print(cnt)

conn.commit()

conn.close()