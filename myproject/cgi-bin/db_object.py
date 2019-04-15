# -*- coding: utf-8 -*-
import sqlite3
class DBworker():
    def __init__(self):
        self.connection =sqlite3.connect("db/users.db")
        self.cursor = self.connection.cursor()
    def WievAllUsers(self):
        self.cursor.execute("select * from users;")
        return (self.cursor.fetchall())
    def AddUser(self, username, email, password, info):
        self.cursor.execute("""insert into users(username, email, password, info)
        values('{}','{}','{}','{}');""".format(username, email, password, info))
        self.connection.commit()
    def GetCountUsers(self):
        self.cursor.execute("SELECT count(*) FROM USERS;")
        return self.cursor.fetchall()[0][0]
    def UserExist(self, username):
        self.cursor.execute("select count(*) From users \
                            where username='{}'".format(username))
        if self.cursor.fetchall()[0][0]!=0:
            return True
        else:
            return False
    def UserLogin(self, email, password):
        #SELECT *  FROM USERS WHERE email='none' AND password='none';
        self.cursor.execute("select username from users where email='{}' \
                            and password='{}';".format(email, password))
        result = self.cursor.fetchall()
        if len(result)==0:
            return "WRONG DATA", False
        else:
            return result[0][0], True
        return self.cursor.fetchall()
    def Close(self):
        self.cursor.close()
        self.connection.close()
