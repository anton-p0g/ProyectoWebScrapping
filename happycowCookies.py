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
    driver = webdriver.Edge()  # Aquí se abre Edge
    driver.get("https://www.happycow.net/")  # Cargamos la página web
    return driver

def aceptar_cookies(driver):
    """
    Acepta el cuadro de cookies si aparece en la página.
    """
    try:
        boton_aceptar = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='web-home']/div[3]/div/div[2]/div[3]/div/div[2]"))
        )
        time.sleep(2)
        boton_aceptar.click()
        print("Cookies aceptadas correctamente.")
    except Exception as e:
        print(f"Error al aceptar las cookies: {e}")

# Función principal que coordina todo el proceso
def main():
    driver = iniciar_navegador()  # Abrimos el navegador
    time.sleep(4)
    aceptar_cookies(driver)  # Aceptamos las cookies
    time.sleep(4)
    driver.quit()  # Cerramos el navegador

# Este es el punto de inicio del programa
if __name__ == "__main__":
    main()