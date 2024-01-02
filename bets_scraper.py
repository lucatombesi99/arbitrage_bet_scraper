from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time
import re
import csv
import os
"""
"""
snai_serieA= 'https://www.snai.it/sport/CALCIO/SERIE%20A'
gold_serieA="https://www.goldbet.it/scommesse/sport/calcio/italia/serie-a/1-1577-93"
william_serieA="https://sports.williamhill.it/betting/it-it/football/competitions/OB_TY321/Serie-A/matches/OB_MGMB/Esito-Finale"
planet_serieA="https://www.planetwin365.it/it/scommesse/calcio/italia/italia-serie-a/7882"
"""
snai_serieA= 'https://www.snai.it/sport/CALCIO/SERIE%20B'
gold_serieA="https://www.goldbet.it/scommesse/sport/calcio/italia/serie-b/1-1577-1626630"
william_serieA="https://sports.williamhill.it/betting/it-it/football/competitions/OB_TY23532/Serie-B/matches/OB_MGMB/Esito-Finale"
planet_serieA="https://www.planetwin365.it/it/scommesse/calcio/italia/italia-serie-b/7844"

"""
"""
snai_serieA= 'https://www.snai.it/sport/CALCIO/LIGUE%201'
gold_serieA="https://www.goldbet.it/scommesse/sport/calcio/francia/ligue-1/1-3039-86"
william_serieA="https://sports.williamhill.it/betting/it-it/football/competitions/OB_TY312/Francia-Ligue-1/matches/OB_MGMB/Esito-Finale"
planet_serieA="https://www.planetwin365.it/it/scommesse/calcio/francia/francia-ligue-1/7918"

"""
path="C:\\Users\\lucat\\OneDrive\\Desktop\\experimento"
driver=webdriver.Chrome()

"""
SNAI

"""


driver.get(snai_serieA)
time.sleep(5)
cookie=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"cookie_consent_banner_closer"))
    )

html=driver.page_source
doc1=BeautifulSoup(html,"html.parser")
doc2=doc1.find_all(class_="margin-bottom-3 ng-scope")
partite_temp=[]
snai_uno=[]
snai_due=[]
snai_x=[]
cookie.click()


for i in doc2:
    partite_temp+=i.find_all(class_="eightFirstCol")



for i in range(len(partite_temp)):
    if(i%5==2):
        temp=partite_temp[i].find(class_="footballBlueBetting ng-binding ng-scope")
        snai_due.append(temp.text.replace(",", "."))

    if(i%5==3):
        temp=partite_temp[i].find(class_="footballBlueBetting ng-binding ng-scope")
        snai_x.append(temp.text.replace(",", "."))

    if(i%5==4):
        temp=partite_temp[i].find(class_="footballBlueBetting ng-binding ng-scope")
        snai_uno.append(temp.text.replace(",", "."))


double_chance=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//*[contains(text(), \"DOPPIA CHANCE\")]"))
    )

double_chance.click()
time.sleep(5)
html=driver.page_source

doc1=BeautifulSoup(html,"html.parser")
snai_double_chance_temp=[]
snai_uno_due=[]
snai_uno_x=[]
snai_x_due=[]
doc2=doc1.find_all(class_="margin-bottom-3 ng-scope")
for i in doc2:
    snai_double_chance_temp+=i.find_all(class_="ng-binding ng-scope")

for i in range(len(snai_double_chance_temp)):
    if(i%3==0):
        temp=snai_double_chance_temp[i]
        temps=temp.text.replace(" ", "")
        temps.strip('\n')
        snai_uno_x.append(temps.replace(",", "."))
    if(i%3==1):
        temp=snai_double_chance_temp[i]
        temps=temp.text.replace(" ", "")
        temps.strip('\n')
        snai_x_due.append(temps.replace(",", "."))
    if(i%3==2):
        temp=snai_double_chance_temp[i]
        temps=temp.text.replace(" ", "")
        temps.strip('\n')
        snai_uno_due.append(temps.replace(",", "."))

"""
GOLDBET

"""



driver.get(gold_serieA)
time.sleep(5)
html=driver.page_source
doc1=BeautifulSoup(html,"html.parser")

gold_1x2=doc1.find_all("span", {"data-markname" : "1X2"})
gold_dc=doc1.find_all("span", {"data-markname" : "DC"})

gold_uno=[]
gold_due=[]
gold_x=[]
gold_uno_due=[]
gold_uno_x=[]
gold_x_due=[]


for i in range(len(gold_1x2)):
    if(i%3==0):
        gold_uno.append(gold_1x2[i].text)
        gold_uno_x.append(gold_dc[i].text)
    if(i%3==1):
        gold_x.append(gold_1x2[i].text)
        gold_uno_due.append(gold_dc[i].text)
    if(i%3==2):
        gold_due.append(gold_1x2[i].text)
        gold_x_due.append(gold_dc[i].text)










"""

william hill

"""
driver.get(william_serieA)
driver.fullscreen_window()
time.sleep(5)

html=driver.page_source

doc1=BeautifulSoup(html,"html.parser")

william_1x2=doc1.find_all(class_="sp-betbutton")
william_uno=[]
william_due=[]
william_x=[]

for i in range(len(william_1x2)):
    if(i<30):
        if(i%3==0):
            william_uno.append(william_1x2[i].find("span").text)
        if(i%3==1):
            william_x.append(william_1x2[i].find("span").text)
        if(i%3==2):
            william_due.append(william_1x2[i].find("span").text)



goal_click=WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id=\"football\"]/div/div/div/div[2]/div[1]/div/ul/li[5]/div/span/a"))
            )
goal_click.click()

william_uno_due=[]
william_uno_x=[]
william_x_due=[]


time.sleep(5)
html=driver.page_source
doc1=BeautifulSoup(html,"html.parser")
william_dc=doc1.find_all(class_="sp-betbutton")
print(len(william_dc))
for i in range(len(william_dc)):
    if(i<30):
        if(i%3==0):
            william_uno_x.append(william_dc[i].find("span").text)
        if(i%3==1):
            william_x_due.append(william_dc[i].find("span").text)
        if(i%3==2):
            william_uno_due.append(william_dc[i].find("span").text)

"""
planetwin

"""



driver.get(planet_serieA)
time.sleep(5)
html=driver.page_source

doc1=BeautifulSoup(html,"html.parser")

planet_quotes=doc1.find_all(class_="oddsQ")
planet_uno=[]
planet_due=[]
planet_x=[] 
planet_uno_due=[]
planet_uno_x=[]
planet_x_due=[]

for i in range(len(planet_quotes)):
    if(i%12==0):
        temp=planet_quotes[i].text
        planet_uno.append(temp.replace(",", "."))
    if(i%12==1):
        temp=planet_quotes[i].text
        planet_x.append(temp.replace(",", "."))
    if(i%12==2):
        temp=planet_quotes[i].text
        planet_due.append(temp.replace(",", "."))
    if(i%12==3):
        temp=planet_quotes[i].text
        planet_uno_x.append(temp.replace(",", "."))
    if(i%12==4):
        temp=planet_quotes[i].text
        planet_uno_due.append(temp.replace(",", "."))
    if(i%12==5):
        temp=planet_quotes[i].text
        planet_x_due.append(temp.replace(",", "."))
     

"""
        


calcolo arbitrages 
"""
arb_1_x2_Snai_Gold=[]
arb_x_12_Snai_Gold=[]
arb_2_1x_Snai_Gold=[]

arb_1_x2_Snai_william=[]
arb_x_12_Snai_william=[]
arb_2_1x_Snai_william=[]

arb_1_x2_Snai_planet=[]
arb_x_12_Snai_planet=[]
arb_2_1x_Snai_planet=[]

arb_1_x2_Gold_william=[]
arb_x_12_Gold_william=[]
arb_2_1x_Gold_william=[]

arb_1_x2_Gold_planet=[]
arb_x_12_Gold_planet=[]
arb_2_1x_Gold_planet=[]

arb_1_x2_william_planet=[]
arb_x_12_william_planet=[]
arb_2_1x_william_planet=[]


for i in range(len(planet_uno)):
    aatemp_1_x2=((1/float(snai_uno[i]))+(1/float(gold_x_due[i])))*100
    aatemp_1_x2_1=((1/float(gold_uno[i]))+(1/float(snai_x_due[i])))*100
    if(aatemp_1_x2<aatemp_1_x2_1):
        aatemp_1_x2=aatemp_1_x2_1
    arb_1_x2_Snai_Gold.append(aatemp_1_x2)

    abtemp_x_12=((1/float(snai_x[i]))+(1/float(gold_uno_due[i])))*100
    abtemp_x_12_1=((1/float(gold_x[i]))+(1/float(snai_uno_due[i])))*100
    if(abtemp_x_12<abtemp_x_12_1):
        abtemp_x_12=abtemp_x_12_1
    arb_x_12_Snai_Gold.append(abtemp_x_12)

    actemp_2_1x=((1/float(snai_due[i]))+(1/float(gold_uno_x[i])))*100
    actemp_2_1x_1=((1/float(gold_due[i]))+(1/float(snai_uno_x[i])))*100
    if(actemp_2_1x<actemp_2_1x_1):
        actemp_2_1x=actemp_2_1x_1
    arb_2_1x_Snai_Gold.append(actemp_2_1x)



    batemp_1_x2=((1/float(snai_uno[i]))+(1/float(william_x_due[i])))*100
    batemp_1_x2_1=((1/float(william_uno[i]))+(1/float(snai_x_due[i])))*100
    if(batemp_1_x2<batemp_1_x2_1):
        batemp_1_x2=batemp_1_x2_1
    arb_1_x2_Snai_william.append(batemp_1_x2)

    bbtemp_x_12=((1/float(snai_x[i]))+(1/float(william_uno_due[i])))*100
    bbtemp_x_12_1=((1/float(william_x[i]))+(1/float(snai_uno_due[i])))*100
    if(bbtemp_x_12<bbtemp_x_12_1):
        bbtemp_x_12=bbtemp_x_12_1
    arb_x_12_Snai_william.append(bbtemp_x_12)

    bctemp_2_1x=((1/float(snai_due[i]))+(1/float(william_uno_x[i])))*100
    bctemp_2_1x_1=((1/float(william_due[i]))+(1/float(snai_uno_x[i])))*100
    if(bctemp_2_1x<bctemp_2_1x_1):
        bctemp_2_1x=bctemp_2_1x_1
    arb_2_1x_Snai_william.append(bctemp_2_1x)



    catemp_1_x2=((1/float(snai_uno[i]))+(1/float(planet_x_due[i])))*100
    catemp_1_x2_1=((1/float(planet_uno[i]))+(1/float(snai_x_due[i])))*100
    if(catemp_1_x2<catemp_1_x2_1):
        catemp_1_x2=catemp_1_x2_1
    arb_1_x2_Snai_planet.append(catemp_1_x2)

    cbtemp_x_12=((1/float(snai_x[i]))+(1/float(planet_uno_due[i])))*100
    cbtemp_x_12_1=((1/float(planet_x[i]))+(1/float(snai_uno_due[i])))*100
    if(cbtemp_x_12<cbtemp_x_12_1):
        cbtemp_x_12=cbtemp_x_12_1
    arb_1_x2_Snai_planet.append(cbtemp_x_12)

    cctemp_2_1x=((1/float(snai_due[i]))+(1/float(planet_uno_x[i])))*100
    cctemp_2_1x_1=((1/float(planet_due[i]))+(1/float(snai_uno_x[i])))*100
    if(cctemp_2_1x<cctemp_2_1x_1):
        cctemp_2_1x=cctemp_2_1x_1
    arb_1_x2_Snai_planet.append(cctemp_2_1x)



    datemp_1_x2=((1/float(gold_uno[i]))+(1/float(william_x_due[i])))*100
    datemp_1_x2_1=((1/float(william_uno[i]))+(1/float(gold_x_due[i])))*100
    if(datemp_1_x2<datemp_1_x2_1):
        datemp_1_x2=datemp_1_x2_1
    arb_1_x2_Gold_william.append(datemp_1_x2)

    dbtemp_x_12=((1/float(gold_x[i]))+(1/float(william_uno_due[i])))*100
    dbtemp_x_12_1=((1/float(william_x[i]))+(1/float(gold_uno_due[i])))*100
    if(dbtemp_x_12<dbtemp_x_12_1):
        dbtemp_x_12=dbtemp_x_12_1
    arb_1_x2_Gold_william.append(dbtemp_x_12)

    dctemp_2_1x=((1/float(gold_due[i]))+(1/float(william_uno_x[i])))*100
    dctemp_2_1x_1=((1/float(william_due[i]))+(1/float(gold_uno_x[i])))*100
    if(dctemp_2_1x<dctemp_2_1x_1):
        dctemp_2_1x=dctemp_2_1x_1
    arb_1_x2_Gold_william.append(dctemp_2_1x)



    eatemp_1_x2=((1/float(gold_uno[i]))+(1/float(planet_x_due[i])))*100
    eatemp_1_x2_1=((1/float(planet_uno[i]))+(1/float(gold_x_due[i])))*100
    if(eatemp_1_x2<eatemp_1_x2_1):
        eatemp_1_x2=eatemp_1_x2_1
    arb_1_x2_Gold_planet.append(eatemp_1_x2)

    ebtemp_x_12=((1/float(gold_x[i]))+(1/float(planet_uno_due[i])))*100
    ebtemp_x_12_1=((1/float(planet_x[i]))+(1/float(gold_uno_due[i])))*100
    if(ebtemp_x_12<ebtemp_x_12_1):
        ebtemp_x_12=ebtemp_x_12_1
    arb_1_x2_Gold_planet.append(ebtemp_x_12)

    ectemp_2_1x=((1/float(gold_due[i]))+(1/float(planet_uno_x[i])))*100
    ectemp_2_1x_1=((1/float(planet_due[i]))+(1/float(gold_uno_x[i])))*100
    if(ectemp_2_1x<ectemp_2_1x_1):
        ectemp_2_1x=ectemp_2_1x_1
    arb_1_x2_Gold_planet.append(ectemp_2_1x)



    fatemp_1_x2=((1/float(william_uno[i]))+(1/float(planet_x_due[i])))*100
    fatemp_1_x2_1=((1/float(planet_uno[i]))+(1/float(william_x_due[i])))*100
    if(fatemp_1_x2<fatemp_1_x2_1):
        fatemp_1_x2=fatemp_1_x2_1
    arb_1_x2_william_planet.append(fatemp_1_x2)

    fbtemp_x_12=((1/float(william_x[i]))+(1/float(planet_uno_due[i])))*100
    fbtemp_x_12_1=((1/float(planet_x[i]))+(1/float(william_uno_due[i])))*100
    if(fbtemp_x_12<fbtemp_x_12_1):
        fbtemp_x_12=fbtemp_x_12_1
    arb_1_x2_william_planet.append(fbtemp_x_12)

    fctemp_2_1x=((1/float(william_due[i]))+(1/float(planet_uno_x[i])))*100
    fctemp_2_1x_1=((1/float(planet_due[i]))+(1/float(william_uno_x[i])))*100
    if(fctemp_2_1x<fctemp_2_1x_1):
        fctemp_2_1x=fctemp_2_1x_1
    arb_1_x2_william_planet.append(fctemp_2_1x)






print("SNAI GOLD")
print(len(arb_1_x2_Snai_Gold))
for i in arb_1_x2_Snai_Gold:
    print(i)
for i in arb_x_12_Snai_Gold:
    print(i)
for i in arb_2_1x_Snai_Gold:
    print(i)

print("________________________________________")

print("SNAI WILLIAM")
print(len(arb_1_x2_Snai_william))
for i in arb_1_x2_Snai_william:
    print(i)
for i in arb_x_12_Snai_william:
    print(i)
for i in arb_2_1x_Snai_william:
    print(i)

print("________________________________________")

print("SNAI PLANET")
print(len(arb_1_x2_Snai_planet))
for i in arb_1_x2_Snai_planet:
    print(i)
for i in arb_x_12_Snai_planet:
    print(i)
for i in arb_2_1x_Snai_planet:
    print(i)

print("________________________________________")

print("GOLD WILLIAM")
print(len(arb_1_x2_Gold_william))
for i in arb_1_x2_Gold_william:
    print(i)
for i in arb_x_12_Gold_william:
    print(i)
for i in arb_2_1x_Gold_william:
    print(i)

print("________________________________________")

print("GOLD PLANET")
print(len(arb_1_x2_Gold_planet))
for i in arb_1_x2_Gold_planet:
    print(i)
for i in arb_1_x2_Gold_planet:
    print(i)
for i in arb_1_x2_Gold_planet:
    print(i)

print("________________________________________")

print("WILLIAM PLANET")
print(len(arb_1_x2_william_planet))
for i in arb_1_x2_william_planet:
    print(i)
for i in arb_x_12_william_planet:
    print(i)
for i in arb_2_1x_william_planet:
    print(i)






