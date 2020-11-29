import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import CommonUtils
import DBUtils
from DBUtils import DbUtils
from CommonUtils import Fetch
from tkinter import ttk
from tkinter import messagebox
from dbconnection import connector
from ttkthemes import themed_tk as tk


class insertStock:

            def __init__(self):
                pass
            
            def  insertStock(self):
                def loadNames(event):
                    sqlConnector=connector()                                #get the connector to the db
                    connection=sqlConnector.getConnector() 
                    cursor = connection.cursor()
                    cursor.execute("USE archa")                             #this function is called to display products under a category
                    querry=" select Name from "+str(categoty.get())
                    cursor.execute(querry)
                    subTables = cursor.fetchall()
                    nameBox['values']=subTables
                def addNewStock():
                    nameBox.forget()
                    nameLabel.grid(row=1,column=1)
                   
                def getcurrentQty():
                    quantity=Fetch.getQuantity(str(categoty.get()),str(nameBox.get()),cursor)   
                    return quantity[0]   


                def addStock():
                    sqlConnector=connector()                                #get the connector to the db
                    connection=sqlConnector.getConnector() 
                    cursor = connection.cursor()
                    
                    if((str(nameBox.get())=='')):
                        
                        attrList={}
                        attrList[0]=str(nameLabel.get("1.0",'end-1c'))
                        attrList[2]=str(priceText.get("1.0",'end-1c'))
                        attrList[1]=str(qtyText.get("1.0",'end-1c'))
                        attrList[3]=str(costprice.get("1.0",'end-1c'))

                        DbUtils.insertIntoDB(str(categoty.get()),attrList,cursor)
                        connection.commit()
                    else:
                        quantity=0
                        
                        quantity=getcurrentQty()
                        quantity+=int(qtyText.get("1.0",'end-1c'))
                        querry="UPDATE "+str(categoty.get())+" SET  `qty` ="+str(quantity)+" WHERE `"+str(categoty.get())+"`.`Name`= '"+str(nameBox.get())+"'"
                        cursor.execute(querry)
                        connection.commit()
                    sqlConnector=connector()                                #get the connector to the db
                    connection=sqlConnector.getConnector() 
                    cursor = connection.cursor()
                    formatted_date = Fetch.getFormattedDate()
                    if(str(nameLabel.get("1.0",'end-1c'))==''):
                        name=str(nameBox.get())
                    else:
                        name=str(nameLabel.get("1.0",'end-1c'))
                    attrList={}
                    attrList[0]=str(categoty.get())
                    attrList[1]=name
                    attrList[2]=str(qtyText.get("1.0",'end-1c'))
                    attrList[3]=str(costprice.get("1.0",'end-1c'))
                    attrList[4]=str(priceText.get("1.0",'end-1c'))
                    attrList[5]=formatted_date
                    attrList[6]=int(qtyText.get("1.0",'end-1c'))*int(costprice.get("1.0",'end-1c'))
                    DbUtils.insertIntoDB('newstock',attrList,cursor)
                    connection.commit()
                    messagebox.showinfo("","The item has been successfully added to the stock")
                    newStock.destroy()
                    
                def putPrice(event):                                         #this function populated price if trying to add existing stock
                     price=Fetch.getPrice(str(categoty.get()),str(nameBox.get()),cursor,"salesprice")
                     priceText.delete(1.0,"end")
                     priceText.insert(1.0,str(price))
                     price=Fetch.getPrice(str(categoty.get()),str(nameBox.get()),cursor,"costprice")
                     costprice.delete(1.0,"end")
                     costprice.insert(1.0,str(price))




                newStock =  tk.ThemedTk()
                newStock.get_themes()
                newStock.set_theme("scidgreen")     
                newStock.geometry('350x350')    
                newStock.title("Stock Entry")
                cat=tkinter.StringVar()
                subcat=tkinter.StringVar()
                categoty = ttk.Combobox(newStock, width = 12, textvariable = cat)# Adding Values 
                nameBox=ttk.Combobox(newStock, width = 12, textvariable = subcat )
                qtyText=tkinter.Text(newStock,width=11,height=1)
                priceText=tkinter.Text(newStock,width=11,height=1)
                addStockButton= ttk.Button(newStock, text = "add",width=13,command=addStock)
                nameLabel=tkinter.Text(newStock,width=11,height=1)
                costprice=tkinter.Text(newStock,width=11,height=1)
                addNewStockButton= ttk.Button(newStock, text = "add new item",width=13,command=addNewStock)
                addStockButton.grid(row=6,column=1)
                addNewStockButton.grid(row=1,column=2)
                qtyText.grid(row=2,column=1)
                priceText.grid(row=4,column=1)
                costprice.grid(row=3,column=1)
                categoty.grid(column = 1, row =0)
                nameBox.grid(column = 1, row =1)
                sqlConnector=connector()                                #get the connector to the db
                connection=sqlConnector.getConnector() 
                cursor = connection.cursor()
                cursor.execute("USE archa")
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                tables2=[]
                for i in range(len(tables)):
                    if tables[i][0]=='newstock':
                        continue
                    else:
                        tables2.append(tables[i][0])              
                categoty['values'] = tables2  
                categoty.bind("<<ComboboxSelected>>",loadNames)
                nameBox.bind("<<ComboboxSelected>>",putPrice)
                field_names = Fetch.getFields('newstock')
                for j in range(len(field_names)-1):
                   
                   label=tkinter.Label(newStock, width=10,text=field_names[j])
                   label.grid(row=j,column=0)
                newStock.mainloop()
                   
                
                            







                