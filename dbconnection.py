
import pymysql
import mysql.connector


class connector:
    def __init__(self): 
        pass            #just init
    def getConnector(self):
            connection=mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="root",
            database="archa"
            )
           
            return connection


    