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


class Restaurant:
    def __init__(self, driver: webdriver, url_restaurante: str) -> None:
        self.driver: webdriver = driver
        self.url: str = url_restaurante
        self.driver.get(self.url)

    def get_title(self) -> str:
        # Pablo
        try:
            titulo = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[1]/ul/li[2]/h1')))

            return titulo.text

        except:
            return ""

    def get_address(self) -> str:
        # Edu
        pass

    def get_coordinates(self) -> Tuple[str, str]:
        # Anton
        try:
            map_path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[3]/div[3]/a'
            map_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, map_path)))

            href: str = map_element.get_attribute("href")

            pattern: str = r"(?P<lat>-?[0-9]+\.[0-9]+),(?P<long>-?[0-9]+\.[0-9]+)"
            coordinates: re.Match = re.search(pattern, href)
            lat: str = coordinates.group("lat")
            long: str = coordinates.group("long")

            
            href: str = map_element.get_attribute("href")

            pattern: str = r"(?P<lat>-?[0-9]+\.[0-9]+),(?P<long>-?[0-9]+\.[0-9]+)"
            coordinates: re.Match = re.search(pattern, href)
            lat: str = coordinates.group("lat")
            long: str = coordinates.group("long")
        except:
            return ""
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
        try:
            type_res = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/article/div/div')))
            list_type: List[str] = []
            for i in type_res:
                if i.text.endswith("an" or "sh" or "se") and i.text != "Vegan":
                    list_type += [i]
            return list_type

        except:
            return ""

    def get_bookmarks(self) -> int:
        # Anton
        try:
            path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/div[1]/ul/li[2]/div[3]/span'
            bookmarks = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, path)))
        except:
            return ""    
        return int(bookmarks.text)


    def get_price_range(self) -> str:
        '''
        # Edu
        Crear una función auxiliar que convierte los iconos dollars a: Cheap, Medium, Expensive (o lo que sea)
        '''
        pass

    def get_telephone_number(self) -> str:
        # Pablo
        path: str = '//*[@id="full-site-content"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[3]/a/span'
        try:
            telefono = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, path)))
            return telefono.text

        except:
            return ""

    def get_email(self) -> str:
        # Pablo
        try:
            instagram = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="full-site-content"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li/'
                           'a[@title="Go to Instagram page for this venue"]')))
            return instagram.get_attribute("href")

        except:
            return ""


    def get_restaurant_website(self) -> str:
        '''
        # Anton
        Hacer un try except por si no existe un sitio web del restaurante
        '''
        website_path: str = '//a[contains(text(), "Website")]'
        try:
            website = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, website_path)))
            
            website_link = website.get_attribute("href")
        except:
            return ""
        
        return website_link


    def get_instagram(self) -> str:
        '''
        # Anton
        '''
        instagram_path: str = '//a[contains(text(), "Instagram")]'
        try:
            instagram = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, instagram_path)))
            
            instagram_link = instagram.get_attribute("href")
        except:
            return ""
        
        return instagram_link
    
    
    def get_facebook(self) -> str:
        # Anton
        facebook_path: str = '//a[contains(text(), "Facebook")]'
        try:
            facebook = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, facebook_path)))
            
            facebook_link = facebook.get_attribute("href")
        except:
            return ""
        
        return facebook_link


    def get_timetable(self) -> Dict[str, str]:
        '''
        # Anton
        '''
        try:
            today: str = datetime.datetime.today().strftime("%A") # Para cambiar el texto Today al correcto día de la semana
            view_hours_path: str = "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[2]/div/div/a"
            hours_list_path: str = "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[2]/div/div/ul/li/child::*"

            view_hours_button = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, view_hours_path)))
            view_hours_button.click()
            
            timetable: Dict[str, str] = {}
            day = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH,hours_list_path)))

            for i in range(len(day) // 2):
                timetable[day[i * 2].text] = day[(i * 2) + 1].text

            timetable[today] = timetable.pop("Today")

            # Comprueba si algún día el restaurante está cerrado
            day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for day in day_order:
                timetable.setdefault(day, "Closed")

            # Ordeno correctamente los días
            timetable = {day: timetable[day] for day in day_order}

            return timetable
        except:
            return ""
    