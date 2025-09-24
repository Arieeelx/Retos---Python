import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#USO DE MICROSOFT EDGE
service = Service("C:\\Drivers\\edgedriver\\msedgedriver.exe")

driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 100000)

driver.get("https://deportespuentealto.cl/recintos")
time.sleep(2)

#Busca el tipo de instalación
campoBusqueda = wait.until(EC.element_to_be_clickable((By.NAME, "macrotag_id")))
campoBusqueda.send_keys("Instalaciones deportivas")
time.sleep(1)

#Busca la reserva
campoReserva = wait.until(EC.element_to_be_clickable((By.NAME, "tag_id")))
campoReserva.send_keys("Futbolito")

#Cambiar fecha a la correspondiente
campoFecha = wait.until(EC.element_to_be_clickable((By.NAME, "date")))
campoFecha.clear()
campoFecha.send_keys("27/09/2025")

#Hora siempre en 00:00
campoHora = wait.until(EC.element_to_be_clickable((By.NAME, "start_time")))
campoHora.send_keys("00:00")

#click en botónn
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "homeSearchForm-button"))).click()

#click en complejo a reservar
try:
    WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='CANCHA DE FUTBOLITO SAN GERONIMO']"))).click()
except TimeoutException:
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='COMPLEJO DOMINGO TOCORNAL']"))).click()
    except TimeoutException:
        pass

#click en hora
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'complexTimeRange-Tag') and text()='20:00-21:00hrs']"))).click()

time.sleep(2.5)

#click en siguiente
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-complexFormButton-Submit"))).click()

#registro de rut
rutUsuario = wait.until(EC.element_to_be_clickable((By.NAME, "rut")))
rutUsuario.send_keys("13700068-7")

#fecha de nacimiento de usuario
diaNacimiento = wait.until(EC.element_to_be_clickable((By.NAME, "day")))
diaNacimiento.send_keys("1")

#mes de nacimiento de usuario
mesNacimiento = wait.until(EC.element_to_be_clickable((By.NAME, "month")))
mesNacimiento.send_keys("Septiembre")

#año de nacimiento de usuario
anoNacimiento = wait.until(EC.element_to_be_clickable((By.NAME, "year")))
anoNacimiento.send_keys("1975")

#click siguiente pre-finalizar reserva
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-complexFormButton-Submit"))).click()

#click en siguiente ya con datos del usuario
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-complexFormButton-Submit"))).click()

#click en reservarr
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "js-complexFormButton-Submit"))).click()

time.sleep(10000)

