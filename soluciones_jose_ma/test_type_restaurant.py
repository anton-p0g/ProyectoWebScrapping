import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple
import datetime
import re
from get_type_restaurant_mejorado import get_type_restaurant

def accept_cookies(driver: webdriver):
    sleep(5) # Esperamos a que se cargue toda la página
    # Existen dos diferentes pop-ups para aceptar cookies
    try:
        path: str = '//*[@id="web-listing"]/div[3]/div/div[2]/div[3]/div/div[2]'
        accept_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        accept_button.click()
        print("First cookie popup accepted")
    except:
        print("First cookie popup not found -- Trying second type cookie")
        try:
            path2: str = '//button[@class="fides-banner-button fides-banner-button-primary fides-accept-all-button"]'
            accept_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path2)))
            accept_button2.click()
            print("Second cookie popup accepted")
        except:
            print("Second cookie popup not found")

def main():
    driver = webdriver.Chrome()
    url = ["https://www.happycow.net/reviews/la-oveja-negra-madrid-32567",
            "https://www.happycow.net/reviews/viva-chapata-madrid-34396",
            "https://www.happycow.net/reviews/mad-mad-vegan-madrid-232175",
            "https://www.happycow.net/reviews/freedom-cakes-diner-madrid-101451"]
    for i in url:
        driver.get(i)
        time.sleep(2)
        accept_cookies(driver)
        time.sleep(2)
        listado = get_type_restaurant(driver)
        print(listado)
        time.sleep(10)


if __name__ == "__main__":
    main()
