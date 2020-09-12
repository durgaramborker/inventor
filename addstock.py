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

class insertStock:

            def __init__(self):
                pass
            
            def  insertStock(self):
                def addNewStock():
                    sqlConnector=connector()                                #get the connector to the db
                    connection=sqlConnector.getConnector() 
                    cursor = connection.cursor()
                    querry= "SELECT * FROM "
                    querry=querry+ str(categoty.get())      
                    cursor.execute(querry)
                    field_names = {}
                    column=0
                    num_fields = len(cursor.description)
                    for d in cursor.description:
                        field_names[column] = d[0]
                        column+=1
                        continue
                    sqlConnector=connector()                                #get the connector to the db
                    connection=sqlConnector.getConnector() 
                    cursor = connection.cursor()
                    querry= "insert into "+str(categoty.get())+" ("
                    for j in range(len(field_names)):
                        if(j!=len(field_names)-1):
                            querry=querry+"`"+field_names[j]+"`,"
                        else:
                            querry=querry+"`"+field_names[j]+"`"
                    querry=querry+") VALUES ("

                    querry=querry+"'"+str('dr3')+"', '"+str('34')+"', '"+str('10')+"' )"
                    cursor.execute(querry)
                    connection.commit()
                sqlConnector=connector()                                #get the connector to the db
                connection=sqlConnector.getConnector() 
                cursor = connection.cursor()
                newStock = Tk()                                              #this function is called to display availale product categories
                newStock.geometry('350x350')    
                newStock.title("Stock Entry")
                number=tkinter.StringVar()
                categoty = ttk.Combobox(newStock, width = 12, textvariable = number)# Adding Values 
                nameLabel=tkinter.Text(newStock,width=11,height=1)
                qtyLabel=tkinter.Text(newStock,width=11,height=1)
                priceLabel=tkinter.Text(newStock,width=11,height=1)
                addStockButton= Button(newStock, text = "add",width=10,command=addNewStock)
                addStockButton.grid(row=5,column=1)
                nameLabel.grid(row=0,column=1)
                qtyLabel.grid(row=2,column=1)
                priceLabel.grid(row=3,column=1)
                categoty.grid(column = 1, row =1)

                cursor.execute("USE archa")
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                tables2=[]
                for i in range(len(tables)):
                    if tables[i][0]=='newstock':
                        continue
                    else:
                        tables2.append(tables[i][0])              
                #cursor.execute("SELECT name FROM connection WHERE type='table';")
                categoty['values'] = tables2  
               
                querry= "SELECT * FROM newstock " 
                cursor.execute(querry)
                field_names = {}
                column=0
                labelList=[]
                num_fields = len(cursor.description)
                for d in cursor.description:
                    field_names[column] = d[0]
                    column+=1
                    continue
                for j in range(len(field_names)-1):
                   label=tkinter.Label(newStock, width=10,text=field_names[j])
                   label.grid(row=j,column=0)
                   
                
                            







                