import pandas as pd
import datetime
import math
import csv
import os

from pathlib import Path

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
        # print(pd.read_csv(fileName, delimiter=';'))
        headerLine = 1
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

    return df
    # df.to_csv(fileName + 'Cleaned.csv', ';', index=False)

   
# method to detect if string has extensio, if not gives it
def CSVextension(csvFile):
    split_tup = os.path.splitext(csvFile)

    if split_tup[1] == '':
        csvFile += '.csv'

    elif split_tup[1] != '.csv':
        csvFile = csvFile[:len(csvFile) -4]
        csvFile += '.csv'
        
    return csvFile


# method to clean empty spaces, generates a new csv file
# this method requires the csv name with and witout the extension on it
# return the dataframe updated, in case of needing it to later use
def LineAnaliser(file, df):
    # df = pd.read_csv(file, delimiter=';')
    # print(df)

    df.dropna(inplace = True)
    print("Linhas incorretas, apagadas.")
    # df.to_csv(fileName + 'Cleaned.csv', ';', index=False)
    return df

# method to read file
def OpenCSVfile():
    csvFile = input("Introduzir nome do CSV: ")
    file = CSVextension(csvFile)
    print()

    headerLine = HasHeader(file)
    print("Cabeçalho na linha " + str(headerLine))


    df = pd.read_csv(file, delimiter=';')
   

    df = LineAnaliser(file, df)


    columnOrderNames = ColumnOrder()
    print(columnOrderNames)


    # df = NewColumn(df, csvFile)

    df.to_csv(csvFile + 'Cleaned.csv', ';', index=False)


def clean():
    os.system('cls')
    OpenCSVfile()
if __name__ == "__main__":
    clean()


