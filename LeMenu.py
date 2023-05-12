import csv, os
import pandas as pd

from CSVcleaner import CSVextension, HasHeader, ColumnOrder, LineAnaliser
from Location import Location

def Menu():
    print("1. Visualisar Ficheiro")
    print("2. Tempo decorrido em segundos de ponto para ponto.")
    print("3. Distância entre pontos")
    print("4. Velocidade de deslocação entre pontos em m/s e km/h")
    print("5. Distância total percorrida e o tempo total gasto")
    print("0. Terminar programa:")

def IndicarFicheiro():
    csvFile = input("Introduzir nome do CSV: ")
    file = CSVextension(csvFile)
    
    print("\n\n")

    headerLine = HasHeader(file)
    
    print("\n\n")

    columnOrderNames = ColumnOrder()

    return file, headerLine, columnOrderNames 

def OpcaoMenu():
    file, headerLine, columnOrderNames = IndicarFicheiro()
    df = pd.read_csv(file, delimiter=';')
    
    locations = []

    with open(file, newline='') as csvFile:
        csvreader = csv.reader(csvFile, delimiter=';')
        for i, row in enumerate(csvreader):
            if i >= headerLine:
                a = Location(row[int(columnOrderNames[0])-1], row[int(columnOrderNames[1])-1], row[int(columnOrderNames[2])-1], row[int(columnOrderNames[3])-1])
                locations.append(a)
    
    while True: 
        os.system('cls')
        Menu()
        option = int(input("Clique no numero da opção que pretende: "))

        match option:
            case 0:
                exit
            case 1:
                print(df)
                print("Cabeçalho na linha " + str(headerLine))
                print(columnOrderNames)
                
            case 2:
                for i, location in enumerate(locations):
                    if i < len(locations)-1:
                        tempo = location.delta_time_sec(location, locations[i+1])
                        print("{:.2f}s entre ponto ".format(tempo) + "{:d}".format(i) + " e ponto {:d}".format(i+1))

            case 3:
                for i, location in enumerate(locations):
                    if i < len(locations)-1:
                        dist = location.calculate_distance_meters(location, locations[i+1])
                        print("{:.2f}m entre ponto ".format(dist) + "{:d}".format(i) + " e ponto {:d}".format(i+1))

                
            case 4:
                print(df)

            case 5:
                print(df)

        input("Press to Continue... ")

if __name__ == "__main__":
    OpcaoMenu()