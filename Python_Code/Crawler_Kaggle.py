from selenium import webdriver
import time
from zipfile import ZipFile


def fetch():
    #Webdriver wird gestartet
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

    driver.set_window_size(1400,1200)

    driver.get("https://www.kaggle.com/account/login?phase=startSignInTab&returnUrl=https%3A%2F%2Fwww.kaggle.com%2F")

    time.sleep(5)

    #Login Prozess

    login_button = driver.find_element_by_xpath('//*[@id="site-container"]/div[1]/div/form/div[2]/div/div[2]/a/li/span')
    login_button.click()

    mail_input = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div[2]/div[1]/div/div/input')
    mail_input.send_keys('testseleniumhslu@hotmail.com')


    mail_paswortd = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div[2]/div[2]/div/div/input')
    time.sleep(2)
    mail_paswortd.click()
    mail_paswortd.send_keys('TestHSLU')

    time.sleep(2)

    #Webdriver öffnet Seite mit geüwünschtem Dataset

    sign_in = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/form/div[2]/div[3]/div/button/span')
    sign_in.click()

    time.sleep(2)

    driver.get('https://www.kaggle.com/usdot/flight-delays')


    #Driver startet Download
    download_button = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a[1]/div/span')

    download_button.click()

    time.sleep(10)

    driver.quit()

    #Die heruntergeladenen Dateien werden entzippt und in Ordner Data kaggle gespeichert
    with ZipFile('C:/Users/usera/Downloads/flight-delays.zip', 'r') as zipObj:
        zipObj.extractall('C:/CIP_Projekt_Gruppe_16/Data/Data_kaggle')


fetch()

print('Daten in Ordner Data_kaggle gespeichert und entzippt. Nächster Schritt: Crawler Wikipedia.')









