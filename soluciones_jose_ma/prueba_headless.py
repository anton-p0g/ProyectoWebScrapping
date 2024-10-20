from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Opciones de Chrome para modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo headless
chrome_options.add_argument("--no-sandbox")  # Recomendado para evitar errores en algunas configuraciones
chrome_options.add_argument("--disable-dev-shm-usage")  # Soluciona errores de memoria compartida en algunos sistemas


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.happycow.net")

titulo = driver.title
print(f"El título de la página es: {titulo}")

driver.quit()
