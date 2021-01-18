from time import sleep, strftime
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

import csv

chromedriver_path = 'C:\\Users\\Chandragupta\\Desktop\\SNA_project\\chrome\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)

ease_my_trip="https://www.easemytrip.com/"
driver.get(ease_my_trip)
sleep(3)

Airports = ["IXA-Agartala", "AGX-Agatti Island", "AGR-Agra", "AMD-Ahmedabad", "AJL-Aizawl", "AKD-Akola",
            "IXD-Allahabad", "IXV-Along", "ATQ-Amritsar", "IXU-Aurangabad", "IXB-Bagdogra", "RGH-Balurghat",
            "BLR-Bangalore", "BEK-Bareli", "IXG-Belgaum", "BEP-Bellary", "BUP-Bhatinda", "BHU-Bhavnagar",
            "BHO-Bhopal", "BBI-Bhubaneswar", "BHJ-Bhuj", "BKB-Bikaner", "PAB-Bilaspur", "BOM-Mumbai", "CCU-Kolkata",
            "CBD-Car Nicobar", "IXC-Chandigarh", "CJB-Coimbatore", "COH-Cooch Behar", "CDP-Cuddapah", "NMB-Daman",
            "DAE-Daparizo", "DAI-Darjeeling", "DED-Dehra Dun", "DEL-Delhi", "DEP-Deparizo", "DBD-Dhanbad",
            "DHM-Dharamsala", "DIB-Dibrugarh", "DMU-Dimapur", "DIU-Diu", "GAY-Gaya", "GOI-Goa", "GOP-Gorakhpur",
            "GUX-Guna", "GAU-Guwahati", "GWL-Gwalior", "HSS-Hissar", "HBX-Hubli", "HYD-Hyderabad", "IMF-Imphal",
            "IDR-Indore", "JLR-Jabalpur", "JGB-Jagdalpur", "JAI-Jaipur", "JSA-Jaisalmer", "IXJ-Jammu",
            "JGA-Jamnagar", "IXW-Jamshedpur", "PYB-Jeypore", "JDH-Jodhpur", "JRH-Jorhat", "IXH-Kailashahar",
            "IXQ-Kamalpur", "IXY-Kandla", "KNU-Kanpur", "IXK-Keshod", "HJR-Khajuraho", "IXN-Khowai", "COK-Kochi",
            "KLH-Kolhapur", "KTU-Kota", "CCJ-Kozhikode", "KUU-Kulu", "IXL-Leh", "IXI-Lilabari", "LKO-Lucknow",
            "LUH-Ludhiana", "MAA-Madras (Chennai)", "IXM-Madurai", "LDA-Malda", "IXE-Mangalore", "MOH-Mohanbari",
            "MZA-Muzaffarnagar", "MZU-Muzaffarpur", "MYQ-Mysore", "NAG-Nagpur", "NDC-Nanded", "ISK-Nasik",
            "NVY-Neyveli", "OMN-Osmanabad", "PGH-Pantnagar", "IXT-Pasighat", "IXP-Pathankot", "PAT-Patna",
            "PNY-Pondicherry", "PBD-Porbandar", "IXZ-Port Blair", "PNQ-Pune", "PUT-Puttaparthi", "RPR-Raipur",
            "RJA-Rajahmundry", "RAJ-Rajkot", "RJI-Rajouri", "RMD-Ramagundam", "IXR-Ranchi", "RTC-Ratnagiri",
            "REW-Rewa", "RRK-Rourkela", "RUP-Rupsi", "SXV-Salem", "TNI-Satna", "SHL-Shillong", "SSE-Sholapur",
            "IXS-Silchar", "SLV-Simla", "SXR-Srinagar", "STV-Surat", "TEZ-Tezpur", "TEI-Tezu", "TJV-Thanjavur",
            "TRV-Thiruvananthapuram", "TRZ-Tiruchirapally", "TIR-Tirupati", "TCR-Tuticorin", "UDR-Udaipur",
            "BDQ-Vadodara", "VNS-Varanasi", "VGA-Vijayawada", "VTZ-Visakhapatnam", "WGC-Warangal", "ZER-Zero"]


def fdetail(i):
    xp_sections =str("""//*[@id="divFlightDetailSec""")+str(i-1)+str(""""]""")
    sections = driver.find_elements_by_xpath(xp_sections)
    sections_list = [value.text for value in sections]
    print(sections_list[0].split("\n"))

def fill_pd(details):
    file = open('C:\\Users\\Chandragupta\\Desktop\\SNA_project\\temp\\flight_details.csv', 'a+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows([details[0:9]])


def start_ease(city_from, city_to, date):
    ease_my_trip = "https://flight.easemytrip.com/FlightList/Index?srch=" \
                   + city_from + "-India|" \
                   + city_to + "-India|" \
                   + date + "&px=1-0-0&cbn=0&ar=undefined&isow=true&isdm=true&lng=&utm_source=google&utm_medium=cpc&utm_campaign=788997081&utm_content=39319940377&utm_term=easemytrip&utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_easemytrip&adgroupid=39319940377&gclid=EAIaIQobChMI4J2MgbTc7QIVigVyCh1QmgJlEAAYASAAEgLDBPD_BwE&IsDoubleSeat=false"
    driver.get(ease_my_trip)
    sleep(randint(5, 8))

    flag = True
    i = 1
    while flag == True:
        xp_sections = '//*[@id="ResultDiv"]/div/div/div[3]/div[' + str(i) + ']'
        i = i + 1
        sections = driver.find_elements_by_xpath(xp_sections)
        sections_list = [value.text for value in sections]
        if sections_list[0] == '':
            flag = False
            continue
        details = sections_list[0].split("\n")
        if details[5] == '1-stop':
            #            fdetail(i-1)
            t = 5
        fill_pd(details)
        print(sections_list[0].split("\n"))


def start_scrap():
    for f in Airports:
        for t in Airports:
            if f == t:
                continue
            start_ease(f, t, "24/1/2021")


start_scrap()