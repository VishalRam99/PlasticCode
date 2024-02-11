'''
Just sit back and let this run. I tried only giving 500 as input, but ig we can push more than 1000 values based on the CPU.
You try and see. Check and say if I should correct something.
'''
#Also, RUN and Check MySQL. Also check the Folder "Vishal" ;-) I finished the barcode part too.
#Give the rows as 1000. I added time delay for CPU's sake. Will take around 2 minutes to complete.

import mysql.connector as MySQL 
import time
import datetime
import random
import barcode as Bar
from barcode.writer import ImageWriter
#import pyautogui as PG
import os

def OpenDB():
    DB = "Plastic_Data" #Replacable with Input Command
    DBDrop = "DROP DATABASE " + DB
    MyCur.execute(DBDrop)
    DBvar = "CREATE DATABASE " + DB
    print("\nExecuting Program...")
    print(DBvar)
    return DBvar

def CreateTable():
    TB = "Bottle_Data" #Replacable with Input Command
    totlist = [TB]
    tot = 'CREATE TABLE IF NOT EXISTS ' + TB + " ("
    samlist = ["Bot_ID BIGINT PRIMARY KEY",
                "Bot_Name VARCHAR(20) NOT NULL",
                "Man_Name VARCHAR(20) NOT NULL",
                "Man_Date DATE NOT NULL"]
    for i in range(4):
        if i != 3:
            RName = samlist[i]
            totlist.append(RName)
            tot += RName + " ,"
        else:
            RName = samlist[i]
            totlist.append(RName)
            tot += RName + ")"

    print("\nExecuting Program...")
    totlist.append(tot)
    print(tot)
    return totlist

def InsertTable(totlist, RowList):
    TR = len(RowList)
    VarList = []
    for i in range(1, TR + 1):
        EleList = []
        VarEle = str()
        VarEle = "INSERT INTO " + totlist[0] + " VALUES ("
        for j in range(1, len(totlist) - 1):
            row = RowList[i-1][j-1]
            EleList.append(row)
            if j == (len(totlist) - 2):
                VarEle += "\'" + row + "\'"
            elif j == (len(totlist) - 3) or j == (len(totlist) - 4):
                VarEle += "\'" + row + "\'" + ", "
            else:    
                VarEle += row + ", "   
        VarEle += ")"
        print("\nExecuting...")
        print(VarEle)
        VarList.append(EleList)
        time.sleep(0.1)
        MyCur.execute(VarEle)
    return VarList

def RanVal():
    inp = int(input("\nHow many Rows are we talking about?\n"))
    RowList = []

    for i in range(1, inp + 1):
        BatchNo = str(random.randint(1,99))
        if len(BatchNo) == 1:
            BatchNo = "0" + BatchNo
        CurrYear = str(datetime.datetime.now().year)[2::]
        CurrMonth = str(datetime.datetime.now().month)
        if len(CurrMonth) == 1:
            CurrMonth = "0" + CurrMonth
        ManCode = str(random.randint(1000,9999))
        BotCode = str(random.randint(100,999))
        UniqueID = BatchNo + CurrYear  + CurrMonth + ManCode + BotCode
        
        if len(RowList) != 0:
            if UniqueID in RowList[len(RowList)-1]:
                i -= 1
            else:
                pass
        else:
            pass
        
        BotName = "Bottle " + chr(random.randint(65,90))
        ManName = "Manufacturer " + chr(random.randint(65,90))
        date = str(datetime.date(random.randint(2020,2024), random.randint(1,12),random.randint(1,28)))
        EleList = [UniqueID,BotName,ManName,date]
        RowList.append(EleList)

    return RowList

def BarCode(Rowlist):
    print("\nCreating Bar Codes. Please Wait.")
    pathname = "C:\\Users\\wesle\\OneDrive\\Documents\\Vishal\\BarCode"

    for filename in os.listdir(pathname): 
        file_path = os.path.join(pathname, filename)  
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  
            elif os.path.isdir(file_path):  
                os.rmdir(file_path)  
        except Exception:  
            pass

    TxtFile = open("C:\\Users\\wesle\\OneDrive\\Documents\\Vishal\\BarCode\\UniqueCodes.txt", 'w')
    for i in range(1, len(Rowlist) + 1):
        Num = str(Rowlist[i-1][0]) + "\n"
        TxtFile.write(Num)
        Bcode = Bar.EAN13(str(Rowlist[i-1][0]), writer = ImageWriter())
        Path = "C:\\Users\\wesle\\OneDrive\\Documents\\Vishal\\BarCode\\Bar " + str(i)
        Bcode.save(Path)
    TxtFile.flush()
    TxtFile.close()


'''

DON'T UNCOMMENT THIS

def CheckOpen():
    os.startfile("C:\\Program Files\\MySQL\\MySQL Server 8.3\\bin\\mysql.exe")
    PG.sleep(3)
    pg_list = ["enter", 
               "Done>Perfect", 
               "USE Plastic_Data;" , 
               "SHOW TABLES;", 
               "SELECT * FROM Bottle_Data;"]
    PG.typewrite(pg_list[1])
    PG.sleep(1)
    PG.typewrite([pg_list[0]])
    PG.sleep(0.5)
    PG.typewrite(pg_list[2])
    PG.sleep(1)
    PG.typewrite([pg_list[0]])
    PG.sleep(0.5)
    PG.typewrite(pg_list[3])
    PG.sleep(1)
    PG.typewrite(pg_list[0])
    PG.sleep(0.5)
    PG.typewrite(pg_list[4])
    PG.sleep(1)
    PG.typewrite(pg_list[0])
    PG.sleep(0.5)
'''

if __name__ == "__main__":
    MyDB = MySQL.connect(host = "localhost", 
                         user = "Vishal",
                         password = "SciForLife")
    MyCur = MyDB.cursor()

    print()
    Data = OpenDB()
    MyCur.execute(Data)
    Data = "USE " + Data[15::]
    MyCur.execute(Data)
    Table1 = CreateTable()
    TabVal = Table1[len(Table1)-1]
    MyCur.execute(TabVal)
    RanList = RanVal()
    InsertTable(Table1,RanList)
    BarCode(RanList)
    print("\n\nAll Done Bruv\n\n")
    MyDB.commit()
    MyCur.close()
    MyDB.close()

    #CheckOpen() I did this for fun, don't remove the comments. Don't even think about it.
