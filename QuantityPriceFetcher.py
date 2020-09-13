import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconnection import connector



class Fetch:

            def __init__(self):
                pass


            def getPrice(tableName,subTableName):
                sqlConnector=connector()                                #get the connector to the db
                connection=sqlConnector.getConnector() 
                cursor = connection.cursor()
                cursor.execute("USE archa")                                       
                querry="select Price from "+str(tableName)+" where Name = '"+str(subTableName)+"'"
                cursor.execute(querry)
                priceTable = cursor.fetchall()
                price=int(priceTable[0][0])
                return price
            def getQuantity(tableName,subTableName):
                sqlConnector=connector()                                #get the connector to the db
                connection=sqlConnector.getConnector() 
                cursor = connection.cursor()
                qtyArray=[]                           
                cursor.execute("USE archa")
                querry="select qty from "+str(tableName)+" where Name = '"+str(subTableName)+"'"    
                cursor.execute(querry)
                qtytTable = cursor.fetchall()
                quantity=qtytTable[0] 
                return quantity
