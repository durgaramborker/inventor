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
from datetime import datetime



class Fetch:

            def __init__(self):
                pass


            def getPrice(tableName,subTableName,cursor):
                cursor.execute("USE archa")                                       
                querry="select Price from "+str(tableName)+" where Name = '"+str(subTableName)+"'"
                cursor.execute(querry)
                priceTable = cursor.fetchall()
                price=int(priceTable[0][0])
                return price
            def getQuantity(tableName,subTableName,cursor): 
                qtyArray=[]                           
                cursor.execute("USE archa")
                querry="select qty from "+str(tableName)+" where Name = '"+str(subTableName)+"'"    
                cursor.execute(querry)
                qtytTable = cursor.fetchall()
                quantity=qtytTable[0] 
                return quantity
            def getFields(tableName):               #returns all fields in the table
                sqlConnector=connector()                                #get the connector to the db
                connection=sqlConnector.getConnector() 
                cursor = connection.cursor()
                querry= "SELECT * FROM "
                querry=querry+ str(tableName)      
                cursor.execute(querry)
                field_names = {}
                column=0
                num_fields = len(cursor.description)
                for d in cursor.description:
                    field_names[column] = d[0]
                    column+=1
                    continue
                return field_names
            def getFormattedDate():                 #returns the current date
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d')
                return formatted_date


