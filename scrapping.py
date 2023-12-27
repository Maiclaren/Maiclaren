from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os

def google_flights():  
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.google.com/travel/flights")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Απόρριψη όλων')]"))).click()  
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="II2One j0Ppje zmMKJ LbIaRd"]'))).send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="II2One j0Ppje zmMKJ LbIaRd"]'))).send_keys("Λονδίνο, Ηνωμένο Βασίλειο")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="zsRT0d"]'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="II2One j0Ppje zmMKJ LbIaRd"]'))).send_keys(Keys.TAB)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="II2One j0Ppje zmMKJ LbIaRd"]'))).send_keys(Keys.TAB + "CHQ")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="zsRT0d"]'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="RLVa8 GeHXyb"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/ul/li[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="TP4Lpb eoY5cb j0Ppje"]'))).send_keys("01/04/2024" + Keys.TAB)
    sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button/span[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/button/span"))).click()

def kayak():    
    driver = webdriver.Firefox()
    driver.get("https://www.gr.kayak.com/")
    sleep(1)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Όχι ευχαριστώ')]").click()
    
google_flights()    

#webpage = input("From which webpage do you want to webscrape? kayak or googleflights:\n")
#try:
#    if webpage == "kayak":
#        kayak()
#    elif webpage == "googleflights":
#        google_flights()
        
#except:
#    print("Your choice is not correct.Choose between: kayak & googleflights")
    
