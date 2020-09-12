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

class Stock:

            def __init__(self):
                pass
            
            def  Stock(self):
                def clicked(tablename):
                                                                                        #this function displays the availble stock of a product
                       

                    if(str(tablename)!=''):                                                     
                        querry= "SELECT * FROM "
                        querry=querry+ str(tablename)      
                        cursor.execute(querry)
                        field_names = {}
                        column=0
                        num_fields = len(cursor.description)
                        for d in cursor.description:
                                field_names[column] = d[0]
                                column+=1
                                continue
                                
                       
                        stock = Tk()
                        stock.title("Stock for "+tablename)
                        for j in range(len(field_names)):
                                e = Entry(stock, width=10, fg='blue')         
                                e.grid(row=0, column=j)
                                e.insert(END, field_names[j])
                        i=0 
                       
                        for bags in cursor: 
                                for j in range(len(bags)): 
                                         e = Entry(stock, width=10, fg='blue')         
                                         e.grid(row=i+1, column=j)
                                         e.insert(END, bags[j])
                                i=i+1
                                if(i==1):
                                         for k in range(len(bags)): 
                                                e = Entry(stock, width=10, fg='blue')         
                                                e.grid(row=i, column=k)
                                                e.insert(END, bags[k])
                    else:
                            print('as')
                
                def callbackFunc(event):
                    clicked(numberChosen.get())                                              
                
                
                
                
                sqlConnector=connector()                                #get the connector to the db
                connection=sqlConnector.getConnector() 
                cursor = connection.cursor()
                stock = Tk()                                              #this function is called to display availale product categories
                stock.geometry('350x350')       
                number=tkinter.StringVar()
                numberChosen = ttk.Combobox(stock, width = 12, textvariable = number)# Adding Values 
                cursor.execute("USE archa")
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                #cursor.execute("SELECT name FROM connection WHERE type='table';")
                numberChosen['values'] = tables
                numberChosen.grid(column = 0, row = 1)  
                #showReport = Button(stock, text = "show stock",width=10,command=clicked)
                #showReport.grid(column = 1, row = 1)
                numberChosen.bind("<<ComboboxSelected>>", callbackFunc)
                stock.mainloop()  


