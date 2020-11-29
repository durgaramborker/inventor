import os
import math
import MySQLdb
import tkinter
import pymysql
import mysql.connector
import CommonUtils
from CommonUtils import Fetch
from dbconnection import connector


class DbUtils:                                                                                          #this class contains common DB methods, that can be used dynamically

                def __init__(self):
                    pass #just init

                def insertIntoDB(tableName,attList,cursor):                     #This function inserts into DB dynamically. takes table attributes names from @param tableName
                    field_names = Fetch.getFields(tableName)                    #Takes cell values from attList.attList mst contain values in the same order as column names in the DB
                    querry= "insert into "+str(tableName)+ "("                  #else, there will be inconsistencies and sometimes querry execution may fail due to type constraints 
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
                def updateDB(tableName,attList,conditionList,cursor):           #This function updates into db dynamocally. takes attributes to be updated
                    querry="update "+str(tableName)+" set "                     #as maps or dictionaries of structure(attributename:new value) in attList. @sample:attlist={Name:'abc'}
                    attKeysList=list(attList)                                   #takes conditions for update statements in conditionlist map or dictionary of structure(condition attribute:attribute value)
                    conditionKeysList=list(conditionList)                       #@sample: suppose condition is, "update tablename set colname="newValue where comumn2=value2.."this will have structure (comumn2:value2)  
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


                    
