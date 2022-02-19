import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3305,
                                    user='root',
                                    password='python',
                                    db='python',
                                    charset='utf8')
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
        print("DaoEmp:init") 
        
    def myselect(self):
        sql = """
        select e_id,
               e_name,
               sex,
               age
          from emp
        """
        
        self.curs.execute(sql)
        myList = self.curs.fetchall()
        return myList
    
    def myinsert(self, e_name, sex, age):
        
        sql = f"""
            insert into emp(
            e_name, sex, age
            ) values(
            '{e_name}', '{sex}', '{age}'
            )
        """
        
        cnt = self.curs.execute(sql)
        self.conn.commit()
        
        return cnt
    
    def myupdate(self, e_id, e_name, sex, age):
        
        sql = f"""
        update emp
           set e_name = '{e_name}',
               sex = '{sex}',
               age = '{age}'
         where e_id = '{e_id}'     
        """
        
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        
        print("update 성공")
        
        return cnt
    
    def mydelete(self, e_id):
        
        sql = f"""
            delete 
              from emp
             where e_id = '{e_id}'
        """
        
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        
        print("delete 성공")
        
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        print("DaoEmp:close")
        
if __name__=='__main__' :
    de = DaoEmp()
    # myList = de.myselect()
    # print(myList)
    
    # myInsert = de.myinsert('9','9','9')
    # print(myInsert)
    
    # myUpdate = de.myupdate('13', '8', '8', '8')
    # print(myUpdate)
    
    myDelete = de.mydelete('11')
    print(myDelete)
    
    
