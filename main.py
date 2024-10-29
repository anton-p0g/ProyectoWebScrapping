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
    sleep(4)  # Wait until the whole page is loaded
    # There are 3 different pop-ups to accept cookies
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
                path_pasado: str = "//*[@id='web-home']/div[3]/div/div[2]/div[3]/div/div[2]"
                accept_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path_pasado)))
                accept_button2.click()
                print("Third cookie popup accepted")
            except:
                print("Third cookie popup not found")


def read_restaurant_urls(file: str, start_index: int, stop_index: int) -> List[str]:
    '''
    PRE:    file: A text file that contains the URLs of the restaurants
            start_index: The first url in the range
            stop_index: The last url in the range
    
    POST:   Returns a list of URLs of restaurants that were read from the file given the range of URLs   
    '''
    with open(file, 'r') as file:
        links = file.readlines()
        links_slice = links[start_index-1:stop_index]
    return [link.strip() for link in links_slice]


def get_restaurants_data(driver: webdriver, urls: List[str], ini_count: int, file_name: str):
    '''
    PRE:    driver: The webdriver that we use to search
            urls: A list of urls of the restaurants
            ini_count: The id of the first restaurant in the list
            file_name: Name of the csv file to be created

    POST:   Extracts the data from each restaurant from the list of urls and writes the data to the csv file
    '''

    cookies_accepted: bool = False
    count: int = ini_count
    for url in urls:
        restaurant: Restaurant = Restaurant(driver, url, count)
        if not cookies_accepted:
            accept_cookies(driver)
            cookies_accepted = True
        restaurant_dict = restaurant.fetch_restaurant_data()
        sleep(10)
        combine_restaurants_to_csv(restaurant_dict, file_name)
        count += 1


def combine_restaurants_to_csv(restaurants_data: Dict[str, str], csv_filename: str):
    """
    PRE: restaurants_data: dictionary of string and string
         csv_filename: name of the csv file
    POST: it writes the data of restaurants to a csv file.
          If the file exists it adds the restaurant data. If not, it writes a header and then it adds the information
    """
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

def combinar_csvs(file: str, final_file: str):
    """
    PRE: fichero: name of the file that you want to include into the fichero_verdadero it is a csv file
         fichero_verdadero: the final result of all ficheros it is a csv file
    """
    with open(final_file, "a", newline="") as file_v:
        escritor = csv.writer(file_v)
        with open(file, "r") as file:
            reader = csv.reader(file)
            escritor.writerows(reader)


def main():
    f"""
    Hemos divido las urls en 4 ficheros diferentes para dividirnos el trabajo entre los integrantes de 
    forma equitativa (dependiendo de la potencia de nuestros procesadores).
    
    Indices de comienzo y numero de urls para cada integrante:
    Anton: indice = 508, numero de urls = 240
    Jose: indice = 303, numero de urls = 205
    Pablo: indice = 133, numero de urls = 170
    Edu: indice = 1, numero de urls = 133
    """

    indice_inicio: List[int] = [1, 133, 303, 508]
    numero_urls: List[int] = [133, 170, 205, 240]
    indice_fin: List[int] = list(map(lambda x, y: x+y-1, indice_inicio, numero_urls))

    # Cada uno de los integrantes debe cambiar las funciones para ejecutarlos
    # Aquí dejo el ejemplo del integrante Edu
    urls: List[str] = read_restaurant_urls("fichero_url.txt", indice_inicio[0], indice_fin[0])
    print(urls)
    driver: webdriver = set_up_driver()
    get_restaurants_data(driver, urls, indice_inicio[0],f"ficheros_csv/restaurants_{indice_inicio[0]}_{indice_fin[0]}.csv")
    driver.quit()

    # Una vez hecho todos los ficheros los hemos juntado en un único fichero.
    files: List[str] = ["ficheros_csv/restaurants_1_133.csv", "ficheros_csv/restaurants_134_303.csv", "ficheros_csv/restaurants_303_507.csv", "ficheros_csv/restaurants_508_748.csv"]
    file: str
    for file in files:
        combinar_csvs(file, "ficheros_csv/restaurants_definitivo.csv")
    

if __name__ == "__main__":
    main()