from selenium import webdriver
import time
import pandas as pd


def fetch():
    #Webdriver wird gestartet
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

    driver.get("https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time")

    origin_airport = driver.find_element_by_xpath('/html/body/div[3]/div[3]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr[16]/td[4]/a')
    origin_airport.click()

    time.sleep(5)
    origin = driver.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr[19]/td[4]/a')
    origin.click()

    time.sleep(5)
    driver.quit()


def clean():
    df1 = pd.read_csv('C:/Users/usera/Downloads/L_AIRPORT.csv_')
    df1.to_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/AIRPORT.csv', index = False)
    df2 = pd.read_csv('C:/Users/usera/Downloads/L_AIRPORT_ID.csv_')
    df2.to_csv(r'C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle/AIRPORT_ID.csv', index = False)


fetch()
clean()

print('Die beiden CSV-Files AIRPORT.csv und AIRPORT_ID.csv wurden heruntergeladen und im Ordner data_kaggle abgelegt. Nächster Schritt: data_kaggle_cleaner.py')
