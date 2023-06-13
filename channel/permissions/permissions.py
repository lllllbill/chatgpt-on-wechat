from config import conf
from common.singleton import singleton
from .mySQLClient import *

@singleton
class permissions:
    
    def __init__(self):
        config = conf()
        self.client = mySQLClient(
            host=conf().get("mysql_host"),
            port=conf().get("mysql_port"),
            user=conf().get("mysql_user"),
            password=conf().get("mysql_password"),
            database=conf().get("mysql_database"),
        )

    def check(self,from_user_id):
        return self.client.execute("SELECT * FROM users where user_id = '"+str(from_user_id)+"' and end_time > now()")
    
    def addOrUpate(self,from_user_id,cyclical):
        return self.client.executemany("insert into users set user_id = '"+str(from_user_id)+"',start_time = CURDATE(), end_time = DATE_ADD(CURDATE(),INTERVAL 1 "+ str(cyclical) +")  ON DUPLICATE KEY UPDATE end_time = DATE_ADD(end_time,INTERVAL 1 "+ str(cyclical) +")")
