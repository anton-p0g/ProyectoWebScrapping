from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict
import csv
import os

from restaurant_class import Restaurant

def set_up_driver() -> webdriver:
    driver = webdriver.Chrome()
    return driver


def accept_cookies(driver: webdriver):
    sleep(5)  # Esperamos a que se cargue toda la página
    # Existen dos diferentes pop-ups para aceptar cookies
    try:
        path: str = '//*[@id="web-listing"]/div[3]/div/div[2]/div[3]/div/div[2]'
        accept_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        accept_button.click()
        print("First cookie popup accepted")
    except:
        print("First cookie popup not found -- Trying second type cookie")
        try:
            path2: str = '//button[@class="fides-banner-button fides-banner-button-primary fides-accept-all-button"]'
            accept_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path2)))
            accept_button2.click()
            print("Second cookie popup accepted")
        except:
            print("Second cookie popup not found")
            try:
                path_pasado = "//*[@id='web-home']/div[3]/div/div[2]/div[3]/div/div[2]"
                accept_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_pasado)))
                accept_button2.click()
                print("Third cookie popup accepted")
            except:
                print("Third cookie popup not found")




def read_restaurant_urls(file, indice_inicio: int, indice_fin: int) -> List[str]:
    with open(file, 'r') as file:
        links = file.readlines()
        links_slice = links[indice_inicio-1:indice_fin]
    return [link.strip() for link in links_slice]


def get_restaurants_data(driver, urls: List[str], ini_contador: int, file: str):
    cookies_accepted = False
    count: int = ini_contador
    for url in urls:
        restaurant: Restaurant = Restaurant(driver, url, count)
        if not cookies_accepted:
            accept_cookies(driver)
            cookies_accepted = True
        restaurant_dict = restaurant.fetch_restaurant_data()
        sleep(10)
        combine_restaurants_to_csv(restaurant_dict, file)
        count += 1


def combine_restaurants_to_csv(restaurants_data: Dict[str, str], csv_filename: str):
    # Modificacion Pablo
    if restaurants_data:
        fieldnames = restaurants_data.keys()

    exist: bool = os.path.isfile(csv_filename)
    if exist:
        mode: str = "a"
    else:
        mode: str = "w"

    with open(csv_filename, mode=mode, newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not exist:
            writer.writeheader()
        writer.writerow(restaurants_data)

def combinar_csvs(fichero: str, fichero_verdadero: str) -> None:
    """
    PRE: fichero: name of the file that you want to include into the fichero_verdadero it is a csv file
        fichero_verdadero: the final result of all ficheros it is a csv file
    """
    with open(fichero_verdadero, "a", newline="") as file_v:
        escritor = csv.writer(file_v)
        with open(fichero, "r") as file:
            reader = csv.reader(file)
            escritor.writerows(reader)


def main():
    f"""
    Indices de comienzo y numero de urls para cada integrante:
    Anton: indice = 508, numero de urls = 240
    Jose: indice = 303, numero de urls = 205
    Pablo: indice = 133, numero de urls = 170
    Edu: indice = 1, numero de urls = 133
    """
    indice_inicio = [1, 133, 303, 508]
    numero_urls = [133, 170, 205, 240]
    indice_fin = list(map(lambda x, y: x+y-1, indice_inicio, numero_urls))

<<<<<<< HEAD
    urls: List[str] = read_restaurant_urls("fichero_url.txt", 401, 405)
    print(urls)
    driver: webdriver = set_up_driver()
    get_restaurants_data(driver, [urls[4]], 405,f"ficheros_csv/restaurants_{401}_{405}.csv")
=======
    urls: List[str] = read_restaurant_urls("fichero_url.txt", 728, indice_fin[3])
    print(urls)
    driver: webdriver = set_up_driver()
    get_restaurants_data(driver, urls, 728,f"ficheros_csv/restaurants_{indice_inicio[3]}_{indice_fin[3]}.csv")

>>>>>>> adf398a33293ab0a4dd51133dd7449b92736d012
    """
    Para combinar los ficheros
    
    list_file = list(map(lambda x, y: f"ficheros_csv/restaurants_{x}_{y}.csv", indice_inicio, numero_urls))
    for file in list_file:
        get_restaurants_data(driver, urls, file)
        combinar_csvs(file, "ficheros_csv/fichero_verdader.csv")
    """

    driver.quit()

if __name__ == "__main__":
    main()