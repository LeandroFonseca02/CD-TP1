import csv

from CSVcleaner import CSVextension, HasHeader, ColumnOrder
from Location import Location


def teste():
    csvFile = input("Introduzir nome do CSV: ")
    file = CSVextension(csvFile)

    headerLine = HasHeader(file)
    print("Cabeçalho na linha " + str(headerLine))

    columnOrderNames = ColumnOrder()

    locations = []

    with open(file, newline='') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        for i, row in enumerate(csvreader):
            if i >= headerLine:
                a = Location(row[int(columnOrderNames[0])-1], row[int(columnOrderNames[1])-1], row[int(columnOrderNames[2])-1], row[int(columnOrderNames[3])-1])
                locations.append(a)




if __name__ == "__main__":
    teste()