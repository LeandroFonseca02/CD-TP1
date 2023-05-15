import pandas as pd
import datetime
from Location import Location
import numpy as np
import math
import csv
import os

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

    headerLine = HasHeader(file)
    print("Cabeçalho na linha " + str(headerLine))


    df = pd.read_csv(file, delimiter=';')
   

    df = LineAnaliser(file, df)


    columnOrderNames = ColumnOrder()
    print(columnOrderNames)


    # df = NewColumn(df, csvFile)
    # df.to_csv(csvFile + 'Cleaned.csv', ';', index=False)

    locations = []
    velocities = []
    loc1Indx = []
    loc2Indx = []

    with open(file, newline='') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        for i, row in enumerate(csvreader):
            if i >= headerLine:
                a = Location(row[int(columnOrderNames[0]) - 1], row[int(columnOrderNames[1]) - 1],
                            row[int(columnOrderNames[2]) - 1], row[int(columnOrderNames[3]) - 1])
                locations.append(a)


    for i, location in enumerate(locations):
        if i < len(locations) - 2:
            velocities.append(location.calculate_velocity_ms(location, locations[i + 1]))
            loc1Indx.append(i)
            loc2Indx.append(i+1)

    velocityData = {'velocity': velocities, 'loc1Indx': loc1Indx, 'loc2Indx': loc2Indx}
    velocityDF = pd.DataFrame(data=velocityData)
        
    veloThirdQrt = velocityDF.quantile(q=0.75, axis=0)
    veloThirdQrt["velocity"]
    



    # npArray =  np.array(velocities)
    # veloThirdQrt = np.quantile(npArray,[0.75])



    


def clean():
    os.system('cls')
    OpenCSVfile()
if __name__ == "__main__":
    clean()


