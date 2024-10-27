import time
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple

from main import accept_cookies

# Como solo queremos un archivo que contiene todos los urls de nuestros restuarantes, este script solo
# se va a ejecutar una vez.
# Crea un archivo txt con los urls

# Jose


def search_city(driver: webdriver, city: str):
    """
    PRE:    driver: The webdriver that we use to search
            city: the string of the city, this should be the city and the country like Barcelona,Spain

    POST: It searches for the city in the website and click the enter button
    """
    buscar = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Search for city, region, or zipcode']"))
    )
    buscar.send_keys(city)
    time.sleep(1)
    lupa = "/html/body/div[1]/div[1]/div[3]/div[4]/div/div/form/div/button"
    search_click(driver, lupa)
    time.sleep(1)

def apply_filters(driver: webdriver, list_filters: List[str]):
    """
    PRE:    driver: The webdriver that we use to search
            list_filters: A list of all path of filters including the path of the filter, apply and search area button

    POST: It clicks the filter button and all the filters, then it clicks the button apply and finally it clicks the area.
    """
    for filtro in list_filters:
        search_click(driver, filtro)
        time.sleep(1.5)


def get_urls(driver: webdriver, clase_a: str) -> List[str]:
    result: List[str] = []
    paginas_web = driver.find_elements(By.CLASS_NAME, clase_a)
    contador_pagina: int = 1
    ultimo_elemento: int = 10

    path_flecha = "//a[@title='Next page']"
    flecha = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, path_flecha))
    )

    while contador_pagina <= ultimo_elemento:
        for pagina in paginas_web:
            url = pagina.get_attribute("href")
            if url:
                result.append(url)

        if contador_pagina < ultimo_elemento:
            flecha.click()
            time.sleep(4)
            flecha = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, path_flecha))
            )
            paginas_web = driver.find_elements(By.CLASS_NAME, clase_a)
        contador_pagina += 1

    return result


def create_file_restaurant_urls(urls: List[str]):
    """
    PRE:    url: list of url got by get_urls
    POST: it creates a file with all urls
    """
    with open("fichero_url.txt", "w") as file:
        for url in urls:
            file.writelines(f"{url}\n")



# funciones auxiliares
def search_click(driver, path: str):
    """
    Auxiliary function for clicking
    PRE:    driver: The webdriver that we use to search
            path: The path of the place to click
    """
    button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, path))
    )
    button.click()

