import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Función para iniciar el navegador
def iniciar_navegador():
    """
    Inicia el navegador web Edge y carga la página principal.
    """
    driver = webdriver.Edge()  # Aquí se abre Firefox
    driver.get("https://www.tripadvisor.es/")  # Cargamos la página web
    return driver

def aceptar_cookies(driver):
    """
    Acepta el cuadro de cookies si aparece en la página.
    """
    try:
        boton_aceptar = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']"))
        )
        time.sleep(2)
        boton_aceptar.click()
        print("Cookies aceptadas correctamente.")
    except Exception as e:
        print(f"Error al aceptar las cookies: {e}")

# Función principal que coordina todo el proceso
def main():
    driver = iniciar_navegador()  # Abrimos el navegador
    time.sleep(3.5)
    aceptar_cookies(driver)  # Aceptamos las cookies
    time.sleep(4)
    driver.quit()  # Cerramos el navegador

# Este es el punto de inicio del programa
if __name__ == "__main__":
    main()