import pandas as pd

print('Daten von Kaggle und Wikipedia wurden gecrawlt. Jetzt werden die Daten bereinigt und erste Vereinigungen vorgenommen.')

def clean():

    df1 = pd.read_csv('C:/CIP_Projekt_Gruppe_16/Data/Data_Wikipedia/crawler_wikipedia_output.csv', sep=";")
    df1.columns = ['Name','IATA_CODE','ICAO','Rufzeichen']

    ###Drop all NA's
    df1 = df1.dropna()

    ###Update Index
    transform = lambda x: x+1
    df1.index = df1.index.map(transform)

    ### Load downloaded csv-file
    df2 = pd.read_csv('C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/airlines.csv', sep=',')
    df2.index = df2.index.map(transform)

    ### Merge csv df with df2 to create df3
    df3 = pd.merge(df2,df1[['IATA_CODE','ICAO','Rufzeichen']],how="left",on = "IATA_CODE")
    df3.index = df3.index.map(transform)

    #Manually Add missing values to df3
    #US Airways IACO: AWE und Rufzeichen Cactus
    values_us_airways = {'ICAO':'AWE','Rufzeichen':'CACTUS'}
    df3 =df3.fillna(value=values_us_airways, limit=1)

    #Atlantic Southeast Airlines ICAO: ASQ und Rufzeichen ACEY
    values_atlantic_southeast = {'ICAO':'ASQ','Rufzeichen':'ACEY'}
    df3 = df3.fillna(value=values_atlantic_southeast, limit=1)

    #Virgin America ICAO: VRD und Rufzeicehn ALASKA
    values_virgin_america = {'ICAO':'VRD','Rufzeichen':'ALASKA'}
    df3 = df3.fillna(value=values_virgin_america, limit=1)

    ### Save as csv file
    df3.to_csv("C:/CIP_Projekt_Gruppe_16/Data/Data_Python/airlines_merged.csv",index = False, header=True)


clean()

print('Daten bereinigt und in Ordner Data_Python als CSV-Datei airlines_merged abgespeichert. Nächster Schritt: Crawler_Airport_ID.py')
