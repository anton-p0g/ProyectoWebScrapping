from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple

from main import set_up_driver, access_web_site

class Restaurant:
    def __init__(self, driver: webdriver, url_restaurante: "str") -> None:
        self.driver: webdriver = driver
        self.url: str = url_restaurante


    def get_title(self) -> str:
        # Pablo
        pass


    def get_address(self) -> str:
        # Edu
        pass


    def get_coordinates(self) -> Tuple[str, str]:
        # Anton
        pass


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
        pass


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
        pass


    def get_timetable(self) -> Dict[str, str]:
        '''
        # Anton
        Crear un diccionario con clave siendo el día de la semana y el valor el horario ese día
        '''
        pass
    

    