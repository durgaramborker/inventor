import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import ttkthemes
from ttkthemes import ThemedStyle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconnection import connector
import sales
import stock
import addstock
import reportGenerator
from reportGenerator import report
from sales import Sale
from stock import Stock
from addstock import insertStock

class app:
        def __init__(self):                                     #the outer app
                window = Tk()
                window.title("Inventory management system")
                style = ThemedStyle(window)
                style.set_theme("black")
                
                def displayStockFrame():
                    getstock=Stock()
                    getstock.Stock()
                def makeSale():
                       sale =Sale()
                       sale.Sales()
                def addStock():
                    newStock=insertStock()
                    newStock.insertStock()

                def showReport():
                    reportW=report()
                    reportW.report()
                insertButton = Button(window, text = "Add Stock", width=10,command=addStock) 
                insertButton.place(relx = 0.4, rely = 0.1, anchor = CENTER)
                updateButton = Button(window, text = "Update",width=10)
                updateButton.place(relx = 0.4, rely = 0.2, anchor = CENTER)
                displayStockButton = Button(window, text = "Display Stock",width=10,command=displayStockFrame)
                displayStockButton.place(relx = 0.4, rely = 0.3, anchor = CENTER) 
                generateReport = Button(window, text = "Generate Report",width=12,command=showReport)
                generateReport.place(relx = 0.4, rely = 0.4, anchor = CENTER) 
                makeSales = Button(window, text = "make sale",width=10,command=makeSale)
                makeSales.place(relx = 0.4, rely = 0.5, anchor = CENTER) 
                window.geometry('350x350')
                window.mainloop()
                
t=app()






