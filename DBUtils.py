import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import CommonUtils
from CommonUtils import Fetch
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconnection import connector


class DbUtils:

                def __init__():
                    pass

                def insertIntoDB(tableName,attList,cursor):
                    field_names = Fetch.getFields(tableName)
                    querry= "insert into "+str(tableName)+ "("
                    for j in range(len(field_names)):
                        if(j!=len(field_names)-1):
                            querry=querry+"`"+field_names[j]+"`,"
                        else:
                            querry=querry+"`"+field_names[j]+"`"
                    querry=querry+") VALUES ("
                    for i in range(len(attList)):
                        if(i!=len(attList)-1):
                            querry=querry+"'"+str(attList[i])+"',"
                        else:
                            querry=querry+"'"+str(attList[i])+"' )"
                    cursor.execute(querry)   
                def updateDB(tableName,attList,conditionList,cursor):
                    querry="update "+str(tableName)+" set "
                    attKeysList=list(attList)
                    conditionKeysList=list(conditionList)
                    for i in range(len(attList)):
                        if(i!=len(attList)-1):
                            querry=querry+"`"+str(attKeysList[i])+"` = '"+attList[str(attKeysList[i])]+"', "
                        else:
                            querry=querry+"`"+str(attKeysList[i])+"` = '"+attList[str(attKeysList[i])]+"' Where "
                    for j in range(len(conditionList)):
                        if(j!=len(conditionList)-1):
                            querry=querry+"`"+str(tableName)+"`.`"+str(conditionKeysList[i])+"` = '"+conditionList[str(conditionKeysList[i])]+"' AND "
                        else:
                              querry=querry+"`"+str(tableName)+"`.`"+str(conditionKeysList[i])+"` = '"+conditionList[str(conditionKeysList[i])]+"'"
                    
                    cursor.execute(querry)  


                    
