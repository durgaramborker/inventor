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
        repotWindow = Tk()                                              #this function is called to dgenerate report on products and categories
        repotWindow.geometry('350x350')    
        repotWindow.title("Stock Entry")
        cat=tkinter.StringVar()
        subcat=tkinter.StringVar()
        categoty = ttk.Combobox(repotWindow, width = 12, textvariable = cat)# Adding Values 
        nameBox=ttk.Combobox(repotWindow, width = 12, textvariable = subcat )
        catogaryLabel=tkinter.Label(repotWindow, width=10,text="category")
        nameLabel=tkinter.Label(repotWindow, width=10,text="item")
        showReport= Button(repotWindow, text = "add new item",width=10)
        fromDateLabel=tkinter.Label(repotWindow, width=10,text="From")
        toDateLabel=tkinter.Label(repotWindow, width=10,text="To")
        fromPick = DateEntry(repotWindow, width=12, background='darkblue',foreground='white', borderwidth=2)
        toPick = DateEntry(repotWindow, width=12, background='darkblue',foreground='white', borderwidth=2)
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




