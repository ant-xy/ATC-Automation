import csv
import requests

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

# Download File

def downloadFile(url, path):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(path, 'wb') as file:
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
    fileDownloaded = downloadFile(url, "data/temp.csv")

    if fileDownloaded:
        dbAirports = [
            ["name","latitude","longitude","municipality","type"],
        ]

        c = 1

        with open(f'data/temp.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                dbAirports.append([row[3],row[4],row[5],row[10],row[2]])

        with open(f"data/{fileName}", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dbAirports)


        print(f"[{Fore.GREEN}*{Style.RESET_ALL}] Data all initialized in path: data/{fileName}\n")
