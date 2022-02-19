import pymysql

class MemberDAO:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    port=3305,
                                    user='root',
                                    password='python',
                                    db='python',
                                    charset='utf8')
        
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        
        print("MemeberDAO init")
        
    def myselect(self):
        sql = f"""
        select m_id,
               m_name,
               tel,
               addr
          from member
        """
        
        self.cursor.execute(sql)
        
        memberlist = self.cursor.fetchall()
        
        return memberlist
        
    def myinsert(self, m_name, tel, addr):
        sql = f"""
            insert into member(
                m_id, m_name, tel, aadr
                ) values(
                '{m_name}', '{tel}', '{addr}
                )
        """
    
        cnt = self.cursor.execute(sql)
    
        self.conn.commit()
    
        return cnt
    
    def myupdate(self, m_id, m_name, tel, addr):
        sql = f"""
            update member
               set m_name = '{m_name}',
                   tel = '{tel}',
                   addr = '{addr}'
             where m_id = '{m_id}'      
        """
    
        cnt = self.cursor.execute(sql)
    
        self.conn.commit()
    
        return cnt
    
    def mydelete(self, m_id):
        sql = f"""
            delete
              from member
             where m_id = {m_id}
        """
    
        cnt = self.cursor.execute(sql)
    
        self.conn.commit()
    
        return cnt
    
    def __del__(self):
        self.cursor.close()    
        self.conn.close()
    
        print("MemeberDAO close")
        
if __name__=='__main__' :
    member = MemberDAO()
    
    result = member.myinsert('1','1','1')
    print(result)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        