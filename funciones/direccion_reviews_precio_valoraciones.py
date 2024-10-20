import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_navegador():
    """
    Inicia el navegador web Edge y carga la página principal.
    """
    driver = webdriver.Edge()  # Aquí se abre Edge
    driver.get("https://www.happycow.net/reviews/mad-mad-madrid-154608")  # Cargamos la página web
    # driver.get("https://www.happycow.net/reviews/flower-burger-madrid-409399")  # Cargamos la página web
    # driver.get("https://www.happycow.net/reviews/jardin-secreto-madrid-287468")  # Cargamos la página web
    return driver

def aceptar_cookies(driver):
    """
    Acepta el cuadro de cookies si aparece en la página.
    """
    try:
        boton_aceptar = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='web-listing']/div[3]/div/div[2]/div[3]/div/div[2]"))
        ) # XPath de las cookies cuando visitas un restaurante en concreto
        time.sleep(2)
        boton_aceptar.click()
        print("Cookies aceptadas correctamente.")
    except Exception as e:
        print(f"Error al aceptar las cookies: {e}")

def obtener_direccion(driver) -> str:
    """
    Obtiene la dirección del restaurante
    """
    try:
        calle = driver.find_element(By.XPATH, "//span[@itemprop='streetAddress']").get_attribute("textContent")
        ciudad = driver.find_element(By.XPATH, "//span[@itemprop='addressLocality']").get_attribute("textContent")
        pais = driver.find_element(By.XPATH, "//span[@itemprop='addressCountry']").get_attribute("textContent")
        codigo_postal = driver.find_element(By.XPATH, "//span[@itemprop='postalCode']").get_attribute("textContent")

        direccion = calle + ", " + ciudad + ", " + pais + ", " + codigo_postal
        return direccion
    except Exception as e:
        print(f"Error al obtener la direccion: {e}")

def obtener_total_rating(driver) -> str:
    """
    Obtiene el número de reviews del restaurante y lo muestra limpio (le quita los paréntesis)
    """
    try:
        ratings = driver.find_element(By.XPATH, "//span[@class='rating-reviews leading-7 text-sm text-gray-500 ml-0']")
        ratings_limpio = re.sub(r"[()]", "", ratings.text)
        return ratings_limpio
    except Exception as e:
        print(f"Error al obtener la cantidad de reviews: {e}")

def obtener_precio(driver) -> str:
    """
    Obtiene el nivel de precio según el número de dólares en amarillo
    """
    try:
        cantidad_dolares = driver.find_elements(By.XPATH, "//*[@class='h-4.5 w-4.5 -mx-0.5 text-yellow-500']")
        if len(cantidad_dolares) == 1:
            return "Barato"
        elif len(cantidad_dolares) == 2:
            return "Moderado"
        elif len(cantidad_dolares) == 3:
            return "Caro"
        else:
            return "?"
    except Exception as e:
        print(f"Error al obtener el precio: {e}")

def obtener_valoracion(driver) -> str:
    """
    Obtiene el número de estrellas del restaurante
    """
    try:
        valoracion = driver.find_element(By.XPATH, "//meta[@itemprop='ratingValue']").get_attribute("content")
        return valoracion
    except Exception as e:
        print(f"Error al obtener el precio: {e}")


# Test
def main():
    driver = iniciar_navegador()  # Abrimos el navegador
    time.sleep(2)
    aceptar_cookies(driver)  # Aceptamos las cookies
    time.sleep(3.5)
    print(obtener_direccion(driver)) # Printea dirección
    print(obtener_total_rating(driver)) # Printea n.º reviews
    time.sleep(3)
    print(obtener_precio(driver)) # Printea nivel de precio
    time.sleep(2)
    print(obtener_valoracion(driver)) # Printea n.º estrellas
    driver.quit()  # Cerramos el navegador

# Este es el punto de inicio del programa
if __name__ == "__main__":
    main()
