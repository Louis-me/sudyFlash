import pymysql

dbinfo = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456",
    "port": 3306
}


class MysqlDB(object):
    def __init__(self):
        # self.db 只要修改表，必须用self.db.commit()进行事务提交，如果报错可以用self.db.rollback()进行回滚
        self.db = pymysql.connect(cursorclass=pymysql.cursors.DictCursor,
                                  **dbinfo)
        # self.cursor 用来查询
        self.cursor = self.db.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        print("--insert---")
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

        #     self.db.rollback()
        # try:
        #     self.cursor.execute(sql)
        #     self.db.commit()
        # except:
        #     self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()
