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
from restaurant_class_copia import Restaurant

def accept_cookies(driver: webdriver, path: str):
    accept_button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, path)))
    accept_button.click()

def main():
    cookies = "/html/body/div[3]/div/div[2]/div[3]/div/div[2]"
    driver = webdriver.Chrome()
    url = "https://www.happycow.net/reviews/starbucks-madrid-357203"
    restaurante = Restaurant(driver, url)
    time.sleep(1)
    restaurante.accept_cookies(cookies)
    time.sleep(5)
    time_table: Dict[str, str] = restaurante.get_timetable()
    print(time_table)

if __name__ == "__main__":
    main()