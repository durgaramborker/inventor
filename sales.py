import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import QuantityPriceFetcher
from QuantityPriceFetcher import Fetch
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconnection import connector


class Sale:

            def __init__(self):
               pass

            def Sales(self):
                                         #this function is called to display the sales page
                
                        def selectcat(event):                                                   
                                cursor.execute("USE archa")                             #this function is called to display products under a category
                                querry=" select Name from "+str(table.get())
                                cursor.execute(querry)
                                subTables = cursor.fetchall()
                                subTable['values']=subTables
                                
                               
                                
                        def finalizeSale():                     # this function finalizes sale and reflects the updated aty back into the db
                                qtyTable.set(1)
                                connection.commit()
                                saleFrame.destroy()
                               
                               
                        def addSale():
                                                                #this function is the main function that adds sale to the totalsale, updates price, updates qty
                                if(isAvailable()):
                                        
                                        price=Fetch.getPrice(str(table.get()), str(subTable.get()))
                                        individualprice=int(price)
                                        prevprice=int(w.cget("text"))
                                        items=int(totalItems .cget("text"))
                                        items+=1
                                        totalItems.config(text=str(items))                                       
                                        totalprice=prevprice+(int(qtyTable.get())*individualprice)
                                        w.config(text=str(totalprice))
                                        List=[]
                                        for i in range(3):
                                                
                                                ea = Entry(saleFrame, width=10, fg='blue')                                 
                                                ea.grid(row=items+7,column=i)                                              
                                                ea.insert(END, str(table.get()))if i==0 else ea.insert(END, str(subTable.get())) if i==1 else ea.insert(END, str(qtyTable.get()))
                                                List.append(ea)
                                                
                                        makeSaleButton = Button(saleFrame, text = "remove", width=10,command=lambda:removeSale(List,makeSaleButton))
                                        makeSaleButton.grid(row = items+7,  column= i+1)
                                else:
                                        messagebox.showerror("out of stock","Sorry, the item"+str(subTable.get())+"is out of stock")
                        def isAvailable():
                                qtyArray=[]                             #this function checks if selected item is available and populates the qty box with available qty
                                cursor.execute("USE archa")
                                querry="select qty from "+str(table.get())+" where Name = '"+str(subTable.get()+"'")    
                                cursor.execute(querry)
                                qtytTable = cursor.fetchall()
                                quantity=qtytTable[0]        
                                if(quantity[0]==0):
                                        return False
                                else:
                                       
                                        cursor.execute("USE archa")
                                        querry="update "+str(table.get())+" set qty= '"+str(quantity[0]-int(qtyTable.get()))+"' where Name = '"+str(subTable.get()+"'")
                                        cursor.execute(querry)
                                        for i in range(int(quantity[0]-int(qtyTable.get()))):
                                                qtyArray.append(i+1)
                                                i+=1
                                        qtyTable['values']=qtyArray                     # populates the qty box with available qty                                      
                                        return True
                        def updateQuantity(event):
                                qtyArray=[]
                                cursor.execute("USE archa")
                                querry="select qty from "+str(table.get())+" where Name = '"+str(subTable.get()+"'")
                                cursor.execute(querry)
                                qtytTable = cursor.fetchall()
                                quantity=qtytTable[0] 
                                j=0                                       
                                for i in range(int(quantity[0])):
                                        qtyArray.append(i+1)
                                        i+=1
                                qtyTable['values']=qtyArray             #update the qty availalbe in the quantity box again as available qty-whatever was added to sale
                               
                        def removeSale(ea,buton):
                                table=ea[0].get()
                                subtable=ea[1].get()
                                quantityValue=ea[2].get()      
                                price=Fetch.getPrice(str(table), str(subtable))
                                cursor.execute("USE archa")
                                querry="select qty from "+str(table)+" where Name = '"+str(subtable)+"'"
                                cursor.execute(querry)
                                qtytTable = cursor.fetchall()
                                quantity=qtytTable[0]   
                                cursor.execute("USE archa")
                                querry="update "+str(table)+" set qty= '"+str(quantity[0]+int(quantityValue))+"' where Name = '"+str(subtable)+"'"
                                cursor.execute(querry)
                                priceFinal=int(price*int(quantityValue))
                                w.config(text=str(int(w.cget("text"))-priceFinal)) #update the price in the totalsale as subtract whatever is removed
                                qtyArray=[]
                                for i in range(int(quantity[0]+int(quantityValue))):    #update the qty availalbein the quantity box again as available qty+whatever was removed
                                        qtyArray.append(i+1)
                                        i+=1
                                        qtyTable['values']=qtyArray
                                for i in range(len(ea)):        
                                        ea[i].destroy()
                                        buton.destroy()
                        
                                       
                        sqlConnector=connector()                                #get the connector to the db
                        connection=sqlConnector.getConnector() 
                        cursor = connection.cursor()
                        saleFrame = Tk()
                        saleFrame.geometry('350x350')
                        saleFrame.title("Make Sale")
                        number=tkinter.StringVar()
                        number2=tkinter.StringVar()
                        number3=tkinter.StringVar()
                        table = ttk.Combobox(saleFrame, width = 12, textvariable = number)
                        subTable = ttk.Combobox(saleFrame, width = 12, textvariable = number2)
                        qtyTable = ttk.Combobox(saleFrame, width = 12, textvariable = number3)
                        selectTable = tkinter.Label(saleFrame, text="Please select Type of Item")
                        selectItem = tkinter.Label(saleFrame, text="Please select  the Item       ")
                        selectQuantity = tkinter.Label(saleFrame, text="Please select  the quantity") 
                        table.grid(column = 1, row = 1) 
                        subTable.grid(column = 1, row = 2)
                        qtyTable.grid(column = 1, row = 3)
                        selectTable.grid(column = 0, row = 1)
                        selectItem.grid(column = 0, row = 2)
                        selectQuantity.grid(column = 0, row = 3)                      
                        cursor.execute("USE archa")
                        cursor.execute("SHOW TABLES")
                        tables = cursor.fetchall()
                        #cursor.execute("SELECT name FROM connection WHERE type='table';")
                        table['values'] = tables                      
                        table.bind("<<ComboboxSelected>>", selectcat)                        
                        subTable.bind("<<ComboboxSelected>>", updateQuantity)                        
                        totalLabel = tkinter.Label(saleFrame, text="total")
                        w = tkinter.Label(saleFrame,text="0")
                        totalLabel.grid(column = 2, row = 4)
                        w.grid(column = 3, row = 4)
                        totalItems = tkinter.Label(saleFrame,text="0")
                        totalItems.pack_forget()
                        makeSaleButton = Button(saleFrame, text = "Add to sale", width=10,command=addSale)
                        finalizeSaleButton = Button(saleFrame, text = "Finalize sale", width=10,command=finalizeSale)
                        #makeSaleButton.bind("<Button-1>", make)
                        makeSaleButton.grid(column = 0, row = 4)
                        finalizeSaleButton.grid(column = 1, row = 4)
                        
                        #ea.pack_forget()                   
                        saleFrame.mainloop()



    
