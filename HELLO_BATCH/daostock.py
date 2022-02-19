import pymysql
class DaoStock:
    def __init__(self):
        print("DaoStock init!")
        self.conn = pymysql.connect(host='localhost',
                                    port=3305,
                                    user='root',
                                    password='python',
                                    db='python',
                                    charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def myinsert(self,s_code,s_name,s_price,ymd_hm):
        sql = f"""
            insert into stock(
                s_code,s_name,s_price,ymd_hm) values(
                '{s_code}', '{s_name}', '{s_price}', '{ymd_hm}') 
        """
        
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        
        return cnt
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        print("DaoStock delete!")

if __name__=='__main__':
    ds = DaoStock()
    cnt = ds.myinsert('2', '2', '2', '2')
    print("cnt", cnt)