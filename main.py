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

def access_web_site(driver: webdriver, url: str):
    driver.get(url)


def accept_cookies(driver: webdriver):
    pass



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
access_web_site(driver)
sleep(3)
driver.quit()

# resturant: Restaurant = Restaurant(driver=driver)
# address = resturant.get_address()