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


def get_timetable(driver) -> Dict[str, str]:
    # Revisión Edu
    # TODO ¡¡En algunas páginas no funciona!!
    try:
        horario_dict = dict()
        dias = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for dia in dias:
            horario_dict.setdefault(dia, "Closed")
        boton_expandir = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[2]/div/div/a"))
        )

        if not boton_expandir:
            return {"Horario": "No hay horario"}
        else:
            boton_expandir.click()
            time.sleep(1)
            horario_html = driver.find_elements(By.XPATH, "//ul[@class = 'hours-list group flex flex-col open']/child::*")
            for elem in horario_html:
                dia = elem.find_element(By.XPATH, "./p[@class = 'hours-day group-[.open]:w-[105px]']")
                horas = elem.find_element(By.XPATH, "./div")
                horas_limpio = horas.text.replace("\n",
                                                  ", ")  # Si el establecimiento tiene horario partido aparecerá un salto de línea entre las dos franjas horarias.
                if dia.text == "Today":
                    horario_dict[datetime.datetime.today().strftime("%A")] = horas_limpio
                else:
                    horario_dict[dia.text] = horas_limpio
            return horario_dict

    except Exception as e:
        print(f"Error al obtener el horario: {e}")

