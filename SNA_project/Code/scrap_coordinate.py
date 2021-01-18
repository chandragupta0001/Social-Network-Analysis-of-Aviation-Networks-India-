from time import sleep, strftime
from random import randint
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
import csv
chromedriver_path = 'C:\\Users\\Chandragupta\\Desktop\\SNA_project\\chrome\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
ease_my_trip="https://www.gps-coordinates.net"
driver.get(ease_my_trip)
sleep(7)
air_data=pd.read_csv("C:\\Users\\Chandragupta\\Desktop\\SNA_project\\Data\\air_data_24_dec.csv")
places=air_data.Source.unique()
is_NaN = air_data.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = air_data[row_has_NaN]
print(air_data.isnull().sum())


def fill_pd(details):
    file = open('C:\\Users\\Chandragupta\\Desktop\\SNA_project\\temp\\airport_coordinates.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows([details])
# international_airport=["DEL-Delhi","BOM-Mumbai","BJS-Beijing","ISB-Islamabad","LHR-London","SFO-San Francisco","ROM-Rome","SDV-Tel Aviv Yafo","TLV-Tel Aviv Yafo","MEL-Melbourne","MBW-Melbourne","MEL-Melbourne","MLB-Melbourne","TYO-Tokyo","ICN-Seoul","AUH-Abu Dhabi"]
for place in places:
    # print(place)
    # continue
    driver.find_element_by_id("address").clear()
    inputElement = driver.find_element_by_id("address")
    inputElement.send_keys("airport "+place)

    driver.find_element_by_xpath('''//*[@id="wrap"]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button''').click()
    sleep(2)
    inputLat = driver.find_element_by_id("latitude")
    inputLon = driver.find_element_by_id("longitude")
    lat=inputLat.get_attribute("value")
    lon=inputLon.get_attribute("value")
    # print(place,lat,lon)
    row=[place,lat,lon]
    print(row)
    fill_pd(row)
    sleep(1)