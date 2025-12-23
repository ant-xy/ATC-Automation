from haversine import distance as haversineDistance
from fuzzywuzzy import fuzz

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

import math
import csv
import time

colorama_init()
print(f"[{Fore.GREEN}*{Style.RESET_ALL}] Welcome to this application!{Style.RESET_ALL}\n1: Create Route\n2: Edit Route\n3: Print Route")

dbAirports = []

with open('data/fixed.csv', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        dbAirports.append(row[0])

def searchAirport(airport : str, threshold: int) -> list: # 90%

    with open('data/fixed.csv', newline = '') as f:
        tempAirportSelections = []
        reader = csv.reader(f)

        for row in reader:
            name = row[0]
            if fuzz.partial_ratio(airport.lower(), name.lower()) >= threshold:
                tempAirportSelections.append([row, fuzz.partial_ratio(airport.lower(), name.lower())])
        #print("Search completed.")
        return tempAirportSelections

def outputAirports(airportTable, maxCount):
    count = 1

    for select in airportTable:
        print(f'{count}. {select[0][0]}, Accuracy: {select[1]}')

        count += 1

        if count >= maxCount:
            break

class Path:
    def __init__(self, airport, lat, long, totalDist):
        self.airport = airport
        self.lat = lat
        self.long = long

class Route:
    def __init__(self, routeName, aircraftType, aircraftID, primAirport, secAirport, totalDistance):
        self.routeName = routeName
        self.aircraftType = aircraftType
        self.aircraftID = aircraftID
        self.primAirport = primAirport
        self.secAirport = secAirport
        self.totalDistance = totalDistance

    def __str__(self):
        return f"Route Name: {self.routeName}\nAircraft Type: {self.aircraftType}\nAircraft ID: {self.aircraftID}\nPrimary Airport: {self.primAirport.airport}\nSecondary Airport: {self.secAirport.airport}\nTotal Distance: {self.totalDistance} km"

def airportSelect():
    airport = None

    while not airport:
        airportName = input(f"[{Fore.GREEN}*{Style.RESET_ALL}]Please enter airport: ")
        potentialAirports = searchAirport(airportName, 90)
        outputAirports(potentialAirports, 3)
        
        print(f"[{Fore.YELLOW}*{Style.RESET_ALL}] Please select an airport from the following using the index.")
        option = int(input(">>> "))

        #print(potentialairports[option-1][0])

        try:
            airport = potentialAirports[option-1][0]
        except IndexError:
            print(f"[{Fore.RED}*{Style.RESET_ALL}] Error! Please try again.")
        except:
            print(f"[{Fore.RED}*{Style.RESET_ALL}] Something went wrong.{Style.RESET_ALL}")
    return airport


routes = []

while True:
    option = input(f"{Fore.BLUE}>>>{Style.RESET_ALL} ")

    if int(option) == 1000:
        while True:
            print(f"[{Fore.GREEN}*{Style.RESET_ALL}]Enter name of the route: ")
            
            name = input(">>> ")
            routeTaken = False

            for route in routes:
                if route.routeName == name:
                    print(f"[{Fore.YELLOW}*{Style.RESET_ALL}] Route already exists! Try again.")
                    routeTaken = True
                    break
            if routeTaken == True:
                continue

            routes.append(Route(name, None, None, None, None))
            print("[{Fore.GREEN}*{Style.RESET_ALL}] Route successfully made!")
            break

    if int(option) == 1:
        print(f"[{Fore.GREEN}*{Style.RESET_ALL}] To create a route, please follow the following instruction:")
        # gathering info 
        aircraftType = input("Please enter aircraft type: ")
        aircraftID  = input("Please enter aircraft ID: ")
        
        primaryAirport = None
        secondAirport = None

        # airport selection
        
        print(f"[{Fore.GREEN}*{Style.RESET_ALL}] Please select your Primary and Secondary airports in the respective order.")
        primaryAirport = airportSelect()
        secondAirport = airportSelect()

        
        primAirport = Path(primaryAirport[0], primaryAirport[1], primaryAirport[2], None)
        secAirport = Path(secondAirport[0], secondAirport[1], secondAirport[2], None)

        #print("Initialized:", primaryAirport[0], primaryAirport[1], primaryAirport[2])
        

        route = None

        while not route:
            inputRoute = input(f"[{Fore.GREEN}*{Style.RESET_ALL}] Please enter route name: ")

            for route in routes:
                print(route)
                if route.routeName == inputRoute:
                    route = None
                    print(f"[{Fore.YELLOW}*{Style.RESET_ALL}] Route name already exists!")
                    break
                else:
                    route = Route(inputRoute, aircraftType, aircraftID, primAirport, secAirport, None)
                    routes.append(route)
                    print(route)
                    break
            if len(routes) == 0:
                route = Route(inputRoute, aircraftType, aircraftID, primAirport, secAirport, None)
                routes.append(route)

        # initializing distance
        
        lat1 = route.primAirport.lat
        lon1 = route.primAirport.long
        lat2 = route.secAirport.lat
        lon2 = route.secAirport.long
        
        totalDistance = haversineDistance(lat1, lat2, lon1, lon2)
        route.totalDistance = totalDistance
        
    if int(option) == 3:
        
        for route in routes:
            print("-------------------------------------------------------")
            print(route)
            print("-------------------------------------------------------")
