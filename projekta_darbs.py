import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import requests
import bs4

import time

import openpyxl
from openpyxl import workbook

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = option)

preces_data = []

#nosaka cik preču un kādas preces tiks meklētas
print("Cik preces tiks meklētas: ")
n = input()

print("Kādas preces tiks meklētas: ")
for _ in range(int(n)):
    x = input()
    preces_data.append(x)
'''
#tiek atvērts 1a.lv
url = "https://www.1a.lv"
driver.get(url)
time.sleep(2)

#tiek meklētas attiecīgās preces 1a.lv un dodas uz to rezultātu mājaslapu
for line in preces_data:

    find = driver.find_element(By.ID, "q")
    find.clear()
    find.send_keys(line)

    button = driver.find_element(By.CLASS_NAME, "main-search__submit")
    button.click()
    time.sleep(2)

    #tiek atrasti TOP 3 populārāko preču parametri, nosaukumi, cenas un tie tiek ieraksstīti CSV failos
    ##parametri
    pop_preces = 0
    f = open("parametri_"+ line + ".csv", "a", encoding = "utf-8")

    lapas_saturs = bs4.BeautifulSoup(driver.page_source, "html.parser")
    parametri = lapas_saturs.find_all(class_ = "ks-new-product-attributes")

    for i in parametri:
        if pop_preces < 5:
            pop_preces += 1
            f.write(str(i.text.strip()) + " " + "\n")
        else:
            break
    f.close()

    #--------------------------------------------------
    ##nosaukumi
    pop_preces = 0
    f = open("nosaukumi_" + line + ".csv", "a", encoding = "utf-8")

    lapas_saturs = bs4.BeautifulSoup(driver.page_source, "html.parser")
    nosaukums = lapas_saturs.find_all(class_ = "ks-new-product-name")

    for i in nosaukums:
        if pop_preces< 5:
            pop_preces += 1
            f.write(str(i.text.strip()) + " " + "\n")
        else:
            break
    f.close()

    #--------------------------------------------------
    ##cenas
    pop_preces = 0
    f = open("cenas_" + line + ".csv", "a", encoding = "utf-8")

    lapas_saturs = bs4.BeautifulSoup(driver.page_source, "html.parser")
    cena = lapas_saturs.find_all(class_ = "ks-new-product-price")

    for i in cena:
        if pop_preces < 5:
            pop_preces += 1
            f.write(str(i.text.strip()) + " " + "\n")
        else:
            break
    f.close()'''

#dati no csv failiem tiek pārvietoti uz excel failu attiecīgi izvelētās excel šūnās
wb = openpyxl.Workbook()
jauns_nosaukums = "rezultats"
page = wb["Sheet"]
page.title = jauns_nosaukums

for line in preces_data:
    page = wb.create_sheet(line)
    page['A1'] = "Nosaukums"
    page['E1'] = "Cena (EUR)"