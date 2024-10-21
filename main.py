from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from typing import List, Dict, Tuple
import csv

from restaurant_class import Restaurant

def set_up_driver() -> webdriver:
    driver = webdriver.Chrome()
    return driver


def accept_cookies(driver: webdriver):
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


def read_restaurant_urls(file) -> List[str]:
    with open(file, 'r') as file:
        links = file.readlines()
    return [link.strip() for link in links]


def get_restaurants_data(driver, urls: List[str]) -> List[Dict[str, str]]:
    restaurants: List[Restaurant] = []
    cookies_accepted = False

    for url in urls:
        restaurant: Restaurant = Restaurant(driver, url)
        if not cookies_accepted:
            accept_cookies(driver)
            cookies_accepted = True
            
        restaurant_dict = restaurant.fetch_restaurant_data()
        restaurants.append(restaurant_dict)
    
    return restaurants


def combine_restaurants_to_csv(restaurants_data: List[Dict[str, str]], csv_filename: str):
    if restaurants_data:
        fieldnames = restaurants_data[0].keys()

    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(restaurants_data)



# ---- Para hacer testing ---- #


# url = "https://www.happycow.net/reviews/viva-chapata-madrid-34396"

# resturant: Restaurant = Restaurant(driver, url)
# accept_cookies(driver)
# restaurant_list = []
# rest_dict = resturant.fetch_restaurant_data()
# restaurant_list.append(rest_dict)
# print(rest_dict)
# combine_restaurants_to_csv(restaurant_list, "ABC")

def main():
    urls = read_restaurant_urls("urls_small.txt")
    driver: webdriver = set_up_driver() 

    restaurants_data = get_restaurants_data(driver, urls)
    combine_restaurants_to_csv(restaurants_data, "csv_test.csv")

    driver.quit()
if __name__ == "__main__":
    main()  