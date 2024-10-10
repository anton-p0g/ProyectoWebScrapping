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


def search_city(driver: webdriver, city:str):
    pass


def apply_filters(driver: webdriver):
    pass


def get_urls(driver: webdriver) -> List[str]:
    pass


def create_file_restaurant_urls(urls: List[str]):
    pass