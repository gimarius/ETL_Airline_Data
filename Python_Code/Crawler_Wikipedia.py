import requests
import time
from bs4 import BeautifulSoup
import csv


print('Daten von Kaggle wurden gecrawlt. Jetzt wird Wikipedia Seite gecrawlt Rufzeichen der Airlines zu erhalten.')


###Klassen Definition Airline
class Airline():
    def __init__(self, name,iatacode,icao,rufzeichen):
        self.name = name
        self.iatacode = iatacode
        self.icao = icao
        self.rufzeichen = rufzeichen


###Klassen Definition Data
class Data():
    def fetch(self):
        time.sleep(1)
        r = requests.get("https://de.wikipedia.org/wiki/Liste_von_Fluggesellschaften")

        airline = []

        doc = BeautifulSoup(r.text, "html.parser")
        doc.find_all("table", class_="wikitable sortable")
        My_table = doc.find("table", {"class":"wikitable sortable"})
        tr_table = My_table.findAll("tr")

        for i in range(1, len(tr_table)):
            columns = tr_table[i].text
            items = columns.split('\n')
            t1 = Airline(items[1], items[3], items[5], items[7])
            airline.append(t1)

        return airline


fetcher = Data()

with open('C:/CIP_Projekt_Gruppe_16/Data/Data_Wikipedia/crawler_wikipedia_output.csv', 'w', newline='',encoding='utf-8') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for t in fetcher.fetch():
        articlewriter.writerow([t.name, t.iatacode, t.icao, t.rufzeichen])


print('Daten in Ordner Data_wikipedia gespeichert. Nächster Schritt: Cleaner.')
