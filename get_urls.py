from main import accept_cookies, set_up_driver
from get_urls_functions import *
import time


def main():
    try:
        url = "https://www.happycow.net/"
        driver = set_up_driver()
        driver.get(url)
        accept_cookies(driver)
        time.sleep(3)

        """
        Una vez accedido a la pagina web, procedemos a buscar la ciudad de Madrid
        """
        ciudad: str = "Madrid, Spain"
        search_city(driver, ciudad)

        """
        Una vez accedido a la pagina de nuestra ciudad, aplicamos los filtros. 
        Debemos tener la lista que contenga el filtro y los filtros
        """

        time.sleep(3)
        lista_filtros: List[str] = [
            "//button[@id='filter-btn']",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[1]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[2]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[3]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[1]/div/div[4]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[1]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[3]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[4]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[5]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[7]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[9]/button",
            "/html/body/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div/div[5]/div[2]/div/div/div[2]/div/div[10]/button",
            "//button[contains(text(), 'Apply')]",
            "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/a[2]",
            "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/a[2]",
            "/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div",
        ]
        apply_filters(driver, lista_filtros)    # Aplicamos los filtros

        """
        Una vez aplicado los filtros, procedemos a obtener las urls
        """
        time.sleep(3)

        class_a = "thumbnail-link"  # The class name of the web pages
        lista_url = get_urls(driver, class_a)
        #Now we can create the file of restaurant urls
        create_file_restaurant_urls(lista_url)
        driver.quit()

    except Exception as e:
        print("No funciona")
        print(e)


if __name__ == "__main__":
    main()