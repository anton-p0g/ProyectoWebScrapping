import time
import re
import unittest
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple

from main import accept_cookies, set_up_driver
from get_restaurant_urls import *


def prueba1():
    try:
        url = "https://www.happycow.net/"
        driver = set_up_driver()
        driver.get(url)
        time.sleep(2)
        path: str = "/html/body/div[3]/div/div[2]/div[3]/div/div[2]"
        accept_cookies(driver, path)
        time.sleep(3)
        ciudad: str = "Madrid, Spain"
        """
        Una vez accedido a la pagina web, procedemos a buscar la ciudad de Madrid
        """
        search_city(driver, ciudad)
        print("Ha funcionado 1")

        """
        Una vez accedido a la pagina de nuestra ciudad, aplicamos los filtros. Debemos tener la lista que contenga el filtro y los filtros
        """
        time.sleep(3)
        lista_filtros: List[str] = ["//button[@id='filter-btn']",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[1]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[2]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[3]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[4]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[1]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[3]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[4]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[5]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[7]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[9]/button",
                                    "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[10]/button",
                                    "//button[contains(text(), 'Apply')]",
                                    "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/a[2]",
                                    "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/a[2]",
                                    "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div",]
        apply_filters(driver, lista_filtros)
        print("Ha funcionado 2")
        time.sleep(3)

    except Exception as e:
        print("No furula")

    finally:
        driver.quit()


def prueba2():
    try:
        url = "https://www.happycow.net/searchmap?s=3&location=Madrid%2C+Spain&filters=vegan-vegetarian-vegfriendly-chains-bakery-catering-coffee-delivery-foodtruck-icecream-juicebar&metric=km&limit=81&order=default&lat=40.38532392817201&lng=-3.664627075195313&zoom=12&page=1&bb=40.222664983810056%2C-3.832511901855469%2C40.547982872533964%2C-3.4967422485351567&radius=0"
        driver = set_up_driver()
        driver.get(url)
        time.sleep(2)
        path: str = "/html/body/div[3]/div/div[2]/div[3]/div/div[2]"
        accept_cookies(driver, path)

        time.sleep(3)

        class_a = "thumbnail-link"
        lista_url = get_urls(driver, class_a)
        print(lista_url)
        print(len(lista_url))


    except Exception as e:
        print("No furula")
        print(e)

    finally:
        driver.quit()



if __name__ == "__main__":
    prueba1()
    prueba2()