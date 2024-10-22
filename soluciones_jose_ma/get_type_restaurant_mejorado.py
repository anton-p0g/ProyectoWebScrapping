import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple
import datetime
import re


def get_type_restaurant(driver) -> List[str]:
    '''
     # Pablo
    A lo mejor hay que crear funciones auxiliares que filtran los diferentes tipos de restaurantes
    '''
    try:
        type_res = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located(
            (By.XPATH, '//*[@id="full-site-content"]/div[3]/div[2]/div/div[1]/article/div/div')))
        if type_res:
            list_type: List[str] = []
            for i in type_res:
                if i.text.endswith("an" or "sh" or "se") and i.text != "Vegan":
                    list_type += [i.text]
            return list_type
        else:
            tipo_secundario = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, "//li[@class='flex items-center flex-wrap']/child::*"))
            )
            list_type: List[str] = []
            for i in tipo_secundario:
                list_type.append(i.text)
            return list_type
    except:
        return []

