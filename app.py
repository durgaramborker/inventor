import os
import math
import MySQLdb
import tkinter
import sqlite3
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
from ttkthemes import themed_tk as tk

class app:
        def __init__(self):                                     #the outer app
                window = tk.ThemedTk()

                window.title("Inventory management system")
                window.get_themes()
                window.set_theme("scidgreen")
                
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
                    
                insertButton = ttk.Button(window, text = "Add Stock", width=18,command=addStock) 
                insertButton.place(relx = 0.4, rely = 0.1, anchor = CENTER)
                updateButton = ttk.Button(window, text = "Update",width=18)
                updateButton.place(relx = 0.4, rely = 0.2, anchor = CENTER)
                displayStockButton = ttk.Button(window, text = "Display Stock",width=18,command=displayStockFrame)
                displayStockButton.place(relx = 0.4, rely = 0.3, anchor = CENTER) 
                generateReport = ttk.Button(window, text = "Generate Report",width=18,command=showReport)
                generateReport.place(relx = 0.4, rely = 0.4, anchor = CENTER) 
                makeSales = ttk.Button(window, text = "make sale",width=18,command=makeSale)
                makeSales.place(relx = 0.4, rely = 0.5, anchor = CENTER) 
                window.geometry('350x350')
                window.mainloop()
                
t=app()






