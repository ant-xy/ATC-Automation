import csv
import requests

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

from pathlib import Path
# Download File

fileName = "airports.csv"
p = Path('.')

csvFile = p / "data" / fileName

def downloadFile(url, path):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(path, 'wb', encoding="utf8") as file:
                file.write(response.content)
            print(f"[{Fore.GREEN}*{Style.RESET_ALL}] File downloaded in path: {path}")
            return True
        else:
            print(f"[{Fore.RED}*{Style.RESET_ALL}] Failed to download file.", response.status_code)
            return False
    except Exception as e:
        print("[{Fore.RED}*{Style.RESET_ALL}] Something went wrong. Error: ", e)
        return False


def downloadRun(url, fileName):

    tempFile = p / "data" / "temp.csv"
    fileDownloaded = downloadFile(url, tempFile)

    if fileDownloaded:
        dbAirports = [
            ["name","latitude","longitude","municipality","type"],
        ]

        c = 1

        with open(tempFile, newline='', encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                dbAirports.append([row[3],row[4],row[5],row[10],row[2]])

        with open(csvFile, "w", newline='', encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerows(dbAirports)


        print(f"[{Fore.GREEN}*{Style.RESET_ALL}] Data all initialized in path: {tempFile}\n")


def initializeData():
    if csvFile.exists():
        pass
    else:
        print(f"[{Fore.RED}*{Style.RESET_ALL}] Data does not exist, initializing.")
        downloadRun("https://davidmegginson.github.io/ourairports-data/airports.csv", csvFile) 
    return csvFile 
