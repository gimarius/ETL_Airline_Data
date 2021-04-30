import pandas as pd
import numpy as np

# Import Datensatz flights.csv
df = pd.read_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/flights.csv')
print("Datensatz flights.csv wurde geladen.")
print("Der Datensatz enthält " + str(len(df)) + " Datensätze.")
print('----------------------')

# Ausgabe Kopf des Datensatzes
#print(df.head())

# Ausgabe Spalten des Datensatzes
# pritn(df.columns)

# ---------------------------------------------------------------------------------------
# Laden der airports.csv
df_airports = pd.read_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/airports.csv')
print('airports.csv wurde geladen.')
print("Der Datensatz airports.csv enthält " + str(len(df_airports)) + " Datensätze.")
print('----------------------')
# print(df_airports.head())
# print(len(df_airports))
# Output: 322

# ---------------------------------------------------------------------------------------
# Import Datensatz AIRPORT_ID.csv
airport_id = pd.read_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/AIRPORT_ID.csv')
# airport_id.head()
# airport_id.index

print("Der Datensatz AIRPORT_ID.csv wurde geladen. Er enthält " + str(len(airport_id)) + " Datensätze.")
print('----------------------')
# ---------------------------------------------------------------------------------------
# Import Datensatz AIRPORT.csv
airport = pd.read_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/AIRPORT.csv')
print("Der Datensatz AIRPORT.csv wurde geladen. Er enthält " + str(len(airport)) + " Datensätze.")
print('----------------------')
# airport.head()
# airport.index

# ---------------------------------------------------------------------------------------
# Merge von airports.csv mit der AIRPORT.csv
a_1 = df_airports.merge(airport, left_on = 'IATA_CODE', right_on = 'Code', how = 'left')
# a_1.head()
print('Merge von airports.csv und AIRPORT.csv. Die verknüpfte Datei a_1 hat eine Länge von ' + str(len(a_1)))
print('----------------------')
# Merge von a_1 mit der AIRPORT_ID.csv
a_2 = a_1.merge(airport_id, left_on = 'Description', right_on = 'Description', how = 'left')
print('Merge von a_1 und AIRPORT_ID.csv. Die verknüpfte Datei a_2 hat eine Länge von ' + str(len(a_2)))
print('----------------------')
# ---------------------------------------------------------------------------------------
# Prüfen auf doppelte Inhalte:
v = a_2['Description'].duplicated()
dupl = (a_2[v])
# print(dupl)

# a_2.tail()
print('321 und 322 haben denselben IATA_Code. Die IDs sind 16218 und 13758.')
print('----------------------')
# ---------------------------------------------------------------------------------------
# Überprüfen, ob die Daten in den Spalten des Datensatzes "df" ORIGIN_AIRPORT und DESTINATON_AIRPORT enthalten sind.
z = df.loc[df['ORIGIN_AIRPORT'] == 16218]
#print(z)
z = df.loc[df['ORIGIN_AIRPORT'] == 13758]
#print(z)

z = df.loc[df['DESTINATION_AIRPORT'] == 13785]
#print(z)
z = df.loc[df['DESTINATION_AIRPORT'] == 16218]
#print(z)

print('Es ist nur die ID 16218 im Datensatz "df" enthalten. Also wird die Zeile mit der ID 13758 gelöscht.')
print('----------------------')

# ---------------------------------------------------------------------------------------
# Die Zeile mit der ID = 13785 ist nicht im Datensatz "df" enthalten, deshalb wird diese gelöscht.
# Diese liegt im Datensatz df_airports im Index 321.
a_2.drop(index=321)
print('Zeile mit dem Index 321 wurde gelöscht.')
print('----------------------')

# ---------------------------------------------------------------------------------------
# Erstellen eines Dataframes mit IATA-Codes und IDs aus dem Dataframe a_2.
list_2 = []

for i in a_2.to_numpy().tolist():
    list_1 = []
    vari = str(i[9])
    list_1.append(vari)
    list_1.append(i[7])
    list_2.append(list_1)
#print(list_2)

codes = pd.DataFrame(list_2, columns = ['ID','IATA'])
# df_test.head()


# ---------------------------------------------------------------------------------------
# Series erstellen, welche anschliessend an den Datensatz "df" angehängt werden.
flights_1 = df['ORIGIN_AIRPORT']
flights_2 = df['DESTINATION_AIRPORT']
#print(len(flights_1))
#f1 = flights_1.head(10)
#print(f1)

# ---------------------------------------------------------------------------------------
# Die beiden Series werden nun an den Datensatz "df" angehängt.
df['Origin'] = flights_1
df['Destination'] = flights_2
#print(df_h)
#print(type(df_h))

# ---------------------------------------------------------------------------------------
# Verknüpfen der von df und codes
merge_origin = df.merge(codes, left_on = 'ORIGIN_AIRPORT', right_on = 'ID', how = 'left')
# print(merge)
# merge_origin.head()

# Ersetzten der ID durch den IATA-Code in der Spalte "Origin"
merge_origin.loc[(merge_origin['ORIGIN_AIRPORT']) == (merge_origin['ID']), 'Origin'] = merge_origin.IATA

# Löschen der folgenden Spalten, da diese nicht mehr gebraucht werden.
del merge_origin['ORIGIN_AIRPORT']
del merge_origin['ID']
del merge_origin['IATA']

# Umbenennen der Spalte Origin zu ORIGIN_AIRPORT.
merge_origin.rename(columns={'Origin': 'ORIGIN_AIRPORT'}, inplace=True)

# TESTING merge_origin
# is_october = merge_origin['MONTH'] == 10
# a = merge_origin[is_october]
# a.head(10)
# print(len(merge))

# ---------------------------------------------------------------------------------------
# Verknüpfen der von merge_origin und codes
merge_dest = merge_origin.merge(codes, left_on = 'DESTINATION_AIRPORT', right_on = 'ID', how = 'left')
# merge_dest.head()

# Ersetzten der ID durch den IATA-Code in der Spalte "Destination"
merge_dest.loc[(merge_dest['DESTINATION_AIRPORT']) == (merge_dest['ID']), 'Destination'] = merge_dest.IATA

# Löschen der folgenden Spalten, da diese nicht mehr gebraucht werden.
del merge_dest['DESTINATION_AIRPORT']
del merge_dest['ID']
del merge_dest['IATA']

# Umbenennen der Spalte Origin zu DESTINATION_AIRPORT.
merge_dest.rename(columns={'Destination': 'DESTINATION_AIRPORT'}, inplace=True)

# is_october = merge_dest['MONTH'] == 10
# b = merge_dest[is_october]
# b.head(10)

# ---------------------------------------------------------------------------------------
# Prüfen auf NAs:
print(merge_dest['ORIGIN_AIRPORT'].isna().sum())
print(merge_dest['DESTINATION_AIRPORT'].isna().sum())
print('----------------------')

# ---------------------------------------------------------------------------------------
# Prüfen, ob neuer und alter Datensatz dieselbe länge haben
print('Differenz zwischen alten und neuem Datensatz: ' + str(len(merge_dest) - len(df)))
print('----------------------')

# ---------------------------------------------------------------------------------------
# Ausgabe als CSV-Datei
print('CSV wird erstellt.')
print('----------------------')
merge_dest.to_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/flights_new.csv', index = False)
print('CSV wurde erstellt. Datenaufbereitung ist abgeschlossen!')
