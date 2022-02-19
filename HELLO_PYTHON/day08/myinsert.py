import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', 
                       password='python', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)


# e_id = 6
# e_name = 7
# sex = 7
# age = 7

# sql = f""" insert into emp (e_id, e_name, sex, age)
#              values('{e_id}', '{e_name}', '{sex}', '{age}')
# """
sql = f""" insert into emp (e_id, e_name, sex, age)
             values(%s, %s, %s, %s)
"""

# cnt = curs.execute(sql)



# 복수개의 자료 insert

data = (
    ('6', '6', '6', '6'),
    ('7', '7', '7', '7')
    )

cnt = curs.executemany(sql, data)

print(cnt)

# 커밋을 꼭 해주어야 반영이 된다. 응

conn.commit()

conn.close()