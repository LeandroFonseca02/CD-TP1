import pandas as pd
import datetime
import math
import csv
import os

cleanFileName = " "


def ColumnOrder():
    columnsOrder = []
    columnsOrder.append(input("Indique o numero da coluna Latidute: "))
    columnsOrder.append(input("Indique o numero da coluna Longitude: "))
    columnsOrder.append(input("Indique o numero da coluna Date: "))
    columnsOrder.append(input("Indique o numero da coluna Time: "))
    
    return columnsOrder


# method to insert a header in a file
# this method requires the csv name with the extension on it
def InsertNewHeader(fileName):
    with open(fileName, 'r+') as file:
        readcontent = file.read()
        file.seek(0, 0) 
        file.write(input("Indique o nome das colunas com \";\" a separa-los: ") + "\n")
        file.write(readcontent)


# method to determine if there is a header, in case there ain´t a header, goes to InsertNewHeader
# this method requires the csv name with the extension on it
# return the line in which the header is
def HasHeader(fileName):
    print("O CSV tem cabeçalho: s/n")
    headerOnOff = input()
    
    if headerOnOff == 's':
        print(pd.read_csv(fileName, delimiter=';'))
        headerLine = input("Em que linha esta o cabeçalho: ")
    else:
        InsertNewHeader(fileName)
        headerLine = 0

    return headerLine

# method to split column write it into a new file
def NewColumn(df, fileName):
    columnToSplit = input("Que coluna quer dividir: ")
    newColumns = input("Quais os nomes das novas colunas: ")
    newColumns = newColumns.split()
    print(newColumns)
    df[[newColumns[0], newColumns[1]]] = df[columnToSplit].str.split(expand=True)
    df.to_csv(fileName + 'Cleaned.csv', ';', index=False)
   
# method to detect if string has extensio, if not gives it
def CSVextension(csvFile):
    split_tup = os.path.splitext(csvFile)

    if split_tup[1] == '':
        cleanFileName = csvFile + "Cleaned.csv"
        print(cleanFileName)
        csvFile += '.csv'

    elif split_tup[1] != '.csv':
        csvFile = csvFile[:len(csvFile) -4]
        cleanFileName = csvFile + "Cleaned.csv"
        csvFile += '.csv'
        print(cleanFileName)
        
    return csvFile


# method to clean empty spaces, generates a new csv file
# this method requires the csv name with and witout the extension on it
# return the dataframe updated, in case of needing it to later use
def LineAnaliser(file, fileName):
    df = pd.read_csv(file, delimiter=';')
    print(df)

    df.dropna(inplace = True)
    df.to_csv(fileName + 'Cleaned.csv', ';', index=False)
    return df

# method to read file
def OpenCSVfile():
    csvFile = input("Introduzir nome do CSV: ")
    file = CSVextension(csvFile)
    
    print(cleanFileName)
    # headerLine = HasHeader(file)
    # print("Cabeçalho na linha " + str(headerLine))
    
    # LineAnaliser(file, csvFile)

    # df = pd.read_csv(file, delimiter=';')
    # print(df)

    # df = LineAnaliser(file, csvFile)

    
    # if(df["Longitude"] == ''):
    #     print("vazia")
    # print(df["Longitude"])

    # columnOrderNames = ColumnOrder()
    # print(columnOrderNames)


    # print(columnOrderNames)

    # NewColumn(df, csvFile)
    # print(df)
    

def Main():
    os.system('cls')
    OpenCSVfile()

Main()
