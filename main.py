from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple

from restaurant_class import Restaurant

def set_up_driver() -> webdriver:
    driver = webdriver.Chrome()
    return driver


def accept_cookies(driver: webdriver):
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
            accept_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path2)))[0]
            accept_button2.click()
            print("Second cookie popup accepted")
        except:
            print("Second cookie popup not found")

def read_restaurant_urls(file) -> List[str]:
    '''
    Leer el fichero obtenido y guardar los urls en una lista
    '''
    pass

# Con un for se crea una clase para cada nuevo url 
# Se puede crear una función que combina todas las funciones de restaurante para obtener toda la información 
# Retorna un diccionario y ese restaurante se añade a una lista. Tendremos una lista de diccionarios que luego se 
# convierte en un csv

def get_restaurant_data(restaurant: Restaurant) -> Dict[str, str]:
    pass


def combine_restaurants_to_csv(restaurants: List[Dict[str, str]]):
    pass

# ---- Para hacer testing ---- #
driver: webdriver = set_up_driver()

url = "https://www.happycow.net/reviews/viva-chapata-madrid-34396"

resturant: Restaurant = Restaurant(driver, url)
accept_cookies(driver)

rest_dict = resturant.get_timetable()
print(rest_dict)

driver.quit()   

