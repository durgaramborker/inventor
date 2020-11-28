import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import CommonUtils
import DBUtils
import tkcalendar
import PyPDF2
import reportlab
import os
from reportlab.platypus import SimpleDocTemplate 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table,TableStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfgen import canvas 
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter as w
from pathlib import Path
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


        def showReport():                                   #this function starts the report genertion
            mainCategory=''
            subCategory=''
            mainCategory=str(categoty.get())
            subCategory=str(nameBox.get())
            fromDate=fromPick.get_date()
            toDate=toPick.get_date()
            show(mainCategory,subCategory,fromDate,toDate)
            
           
        def createPdf(data):                    #this function ccepts the data formatted, and draws and saves it into pdf
            
            fileName="report"+" for "+str(categoty.get())+" - "+str(nameBox.get())+".pdf"
          
            pdf= SimpleDocTemplate(
               fileName ,pagesize=letter,showBoundary=1
            )
            table =Table(data)
            elems=[]
            elems.append(table)
            style = TableStyle([
            ('BACKGROUND', (0,0), (4,0), colors.green),
            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 14),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND',(0,1),(-1,-1),colors.beige),])
            table.setStyle(style)
            ts = TableStyle([('BOX',(0,0),(-1,-1),2,colors.black),
            ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
            ('LINEABOVE',(0,2),(-1,2),2,colors.green),
            ('GRID',(0,1),(-1,-1),2,colors.black),])
            table.setStyle(ts)
            pdf.build(elems)
            os.startfile(fileName)
           # pdf = canvas.Canvas(fileName)
            #pdfmetrics.registerFont(TTFont('abc', 'timesbd.ttf'))
            #pdf.setFont('abc', 36)
            #pdf.drawCentredString(300, 770, "report"+" for "+str(categoty.get())+" - "+str(nameBox.get()))
            #pdf.save()

            
            #messagebox.showinfo("info","report has been successfully generated")
            #subprocess.Popen([file],shell=True)
        def DrawReportIntoPdf():                                        #this function formats the DB date into table, passes the same to pdfwriter            
            field_names =Fetch.getFields("saleout")
            column=0
            data=[]
            list1=[]
            list2=[]
            totalQty=0
            totalPrice=0
            for j in range(len(field_names)):                               #populate upper row with column names
                list1.append(field_names[j])       
            data.append(list1)
            for bags in cursor:                                                                 #popultate topmost row
                for j in range(len(bags)): 
                    list2.append(str(bags[j]))
                    if (j==2):
                        totalQty+=int(bags[j])
                    if (j==3):
                        totalPrice+=int(bags[j])
                data.append(list2.copy())
                list2.clear()
            data.append(['Total Price and Qty sold','',str(totalQty),str(totalPrice),''])      
            createPdf(data)

        def show(mainCategory,subCategory,fromDate,toDate):             #this function fetches details about the selected criterias from the DB
                                                                                    
                    if(str(mainCategory)!=''):                                                     
                        querry= "SELECT * FROM saleout where category = '"
                        querry=querry+ str(mainCategory)+"'"
                        if(subCategory!=''):
                            querry=querry+" and Name = '"
                            querry=querry+ str(subCategory)+"'" 
                       
                        querry=querry+" and date between  '"
                        querry=querry+str(fromPick.get_date())+"'"
                        querry=querry+" and '"
                        querry=querry+str(toPick.get_date())+"'"
                        cursor.execute(querry)
                        DrawReportIntoPdf()          
                    else:
                            querry= "SELECT * FROM saleout"
                            querry=querry+" where date between  '"
                            querry=querry+str(fromPick.get_date())+"'"
                            querry=querry+" and '"
                            querry=querry+str(toPick.get_date())+"'"
                            cursor.execute(querry)
                            DrawReportIntoPdf()  

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




