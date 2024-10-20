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

"""
Se supone que hemos entrado ya en la url del restaurante
"""
class Restaurant:
    def __init__(self, driver: webdriver, url_restaurante: str) -> None:
        self.driver: webdriver = driver
        self.url: str = url_restaurante

        self.driver.get(self.url)

    def get_title(self) -> str:
        # Pablo
        pass


    def get_address(self) -> str:
        # Edu
        print("Hello")
        pass


    def get_coordinates(self) -> Tuple[str, str]:
        # Anton
        map_path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[3]/a'
        map_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, map_path)))
        
        href: str = map_element.get_attribute("href")

        pattern: str = r"(?P<lat>-?[0-9]+\.[0-9]+),(?P<long>-?[0-9]+\.[0-9]+)"
        coordinates: re.Match = re.search(pattern, href)
        lat: str = coordinates.group("lat")
        long: str = coordinates.group("long")

        return (lat, long)

    def get_total_rating(self) -> int:
        # Edu
        pass


    def get_rating(self) -> int:
        # Edu
        pass


    def get_type_restaurant(self) -> List[str]:
        '''
         # Pablo
        A lo mejor hay que crear funciones auxiliares que filtran los diferentes tipos de restaurantes
        '''
        pass

    def get_bookmarks(self) -> int:
        # Anton
        path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[1]/ul/li[2]/div[3]/span'
        bookmarks = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, path)))
        
        return int(bookmarks.text)



    def get_price_range(self) -> str:
        '''
        # Edu
        Crear una función auxiliar que convierte los iconos dollars a: Cheap, Medium, Expensive (o lo que sea)
        '''
        pass


    def get_telephone_number(self) -> str:
         # Pablo
        pass


    def get_email(self) -> str:
         # Pablo
        pass


    def get_restaurant_website(self) -> str:
        '''
        # Anton
        Hacer un try except por si no existe un sitio web del restaurante
        '''
        try:
            website_path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[1]/ul/li[2]/a'
            website = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, website_path)))
            
            print(website.get_attribute("href"))
        except Exception as e:
            print(f"Error al obtener el sitio web\n\n:{e}")



    def get_timetable(self) -> Dict[str, str]:
        '''
        # Anton
        Crear un diccionario con clave siendo el día de la semana y el valor el horario ese día
        '''
        today: str = datetime.datetime.today().strftime("%A")

        view_hours_path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[4]/ul/li[2]/div/div/a'
    
        view_hours_button = self.driver.find_element(By.XPATH, '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[4]/ul/li[2]/div/div/a/span')

        print(view_hours_button.text)
        
        
        
        #hours_list_path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[4]/ul/li[2]/div/div/ul'
        # hours_list = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.XPATH, hours_list_path)))

        # print(hours_list.text)
    