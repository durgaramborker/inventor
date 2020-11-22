import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import CommonUtils
import DBUtils
import tkcalendar
from DBUtils import DbUtils
from CommonUtils import Fetch
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconnection import connector
from tkcalendar import DateEntry

class report:




    def __init__(self):
        pass

    def report(self):
        def selectcat(event):                                                   
            cursor.execute("USE archa")                             #this function is called to display products under a category
            querry=" select Name from "+str(categoty.get())
            cursor.execute(querry)
            subTables = cursor.fetchall()
            nameBox['values']=subTables


        def showReport():
            mainCategory=''
            subCategory=''
            mainCategory=str(categoty.get())
            subCategory=str(nameBox.get())
            fromDate=fromPick.get_date()
            toDate=toPick.get_date()
            show(mainCategory,subCategory,fromDate,toDate)
           
             


        def show(mainCategory,subCategory,fromDate,toDate):
                                                                                        #this function displays the availble stock of a product
                       

                    if(str(mainCategory)!=''):                                                     
                        querry= "SELECT * FROM saleout where category = '"
                        querry=querry+ str(mainCategory)+"'"
                        if(subCategory!=''):
                            querry=querry+" and Name = '"
                            querry=querry+ str(subCategory)+"'"      
                        cursor.execute(querry)
                        field_names =Fetch.getFields("saleout")
                        column=0
                        stock = Tk() 
                        stock.title("Stock for ")
                        for j in range(len(field_names)):                               #populate upper row with column names
                                e = Entry(stock, width=20, fg='blue')         
                                e.grid(row=0, column=j)
                                e.insert(END, field_names[j])
                        i=0 
                       
                        for bags in cursor:                                                                 #popultate topmost row
                                for j in range(len(bags)): 
                                         e = Entry(stock, width=20, fg='blue')         
                                         e.grid(row=i+1, column=j)
                                         e.insert(END, bags[j])
                                i=i+1
                                
                    else:
                            print('as')









        sqlConnector=connector()                                #get the connector to the db
        connection=sqlConnector.getConnector() 
        cursor = connection.cursor()
        repotWindow = Tk()                                              #this function is called to dgenerate report on products and categories
        repotWindow.geometry('350x350')    
        repotWindow.title("Stock Entry")
        cat=tkinter.StringVar()
        subcat=tkinter.StringVar()
        categoty = ttk.Combobox(repotWindow, width = 12, textvariable = cat)# Adding Values 
        nameBox=ttk.Combobox(repotWindow, width = 12, textvariable = subcat )
        catogaryLabel=tkinter.Label(repotWindow, width=10,text="category")
        nameLabel=tkinter.Label(repotWindow, width=10,text="item")
        showReport= Button(repotWindow, text = "show report",width=10 ,command=showReport)
        fromDateLabel=tkinter.Label(repotWindow, width=10,text="From")
        toDateLabel=tkinter.Label(repotWindow, width=10,text="To")
        fromPick = DateEntry(repotWindow, width=12,date_pattern='y/mm/dd', background='darkblue',foreground='white', borderwidth=2)
        toPick = DateEntry(repotWindow, width=12,date_pattern='y/mm/dd', background='darkblue',foreground='white', borderwidth=2)
        cursor.execute("USE archa")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        #cursor.execute("SELECT name FROM connection WHERE type='table';")
        categoty['values'] = tables
        categoty.bind("<<ComboboxSelected>>", selectcat)                
        toPick.grid(column = 1, row =2)
        showReport.grid(column=2,row=4)
        catogaryLabel.grid(column=0,row=0)
        fromDateLabel.grid(column=0,row=2)
        toDateLabel.grid(column=0,row=3)
        nameLabel.grid(column=0,row=1)
        categoty.grid(column = 1, row =0)
        nameBox.grid(column = 1, row =1)
        fromPick.grid(column = 1, row =2)
        toPick.grid(column = 1, row =3)
        repotWindow.mainloop()




