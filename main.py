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
    path: str = '//*[@id="web-listing"]/div[3]/div/div[2]/div[3]/div/div[2]'
    accept_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, path)))
    accept_button.click()



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
# driver.get("https://www.happycow.net/")
# sleep(3)
# driver.quit()

url = "https://www.happycow.net/reviews/la-oveja-negra-madrid-32567"

resturant: Restaurant = Restaurant(driver, url)
accept_cookies(driver)

address = resturant.get_timetable()
print(address)
sleep(2)
driver.quit()   

