import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#USO DE GOOGLE CHROME
driver = webdriver.Chrome()

driver.get("https://deportespuentealto.cl/recintos")
time.sleep(2)

#Busca el tipo de instalación
campoBusqueda = driver.find_element(By.NAME, "macrotag_id")
campoBusqueda.send_keys("Instalaciones deportivas")
time.sleep(0.15)

#Busca la reserva
campoReserva = driver.find_element(By.NAME, "tag_id")
campoReserva.send_keys("Futbolito")
time.sleep(0.15)

#Cambiar fecha a la correspondiente
campoFecha = driver.find_element(By.NAME, "date")
campoFecha.clear()
campoFecha.send_keys("31/07/2025")
time.sleep(0.15)

#Hora siempre en 00:00
campoHora = driver.find_element(By.NAME, "start_time")
campoHora.send_keys("00:00")
time.sleep(0.15)

#click en botónn
driver.find_element(By.CLASS_NAME, "homeSearchForm-button").click()
time.sleep(4)

#click en complejo a reservar
driver.find_element(By.CSS_SELECTOR, "[title='COMPLEJO DEPORTIVO SAN GERONIMO']").click()
time.sleep(2.5)

#click en hora
driver.find_element(By.XPATH, "//a[contains(@class, 'complexTimeRange-Tag') and text()='20:00-21:00hrs']").click()
time.sleep(2)

#click en siguiente
driver.find_element(By.CLASS_NAME, "js-complexFormButton-Submit").click()
time.sleep(1.5)

#registro de rut
rutUsuario = driver.find_element(By.NAME, "rut")
rutUsuario.send_keys("19562873-4")
time.sleep(0.15)

#fecha de nacimiento de usuario
diaNacimiento = driver.find_element(By.NAME, "day")
diaNacimiento.send_keys("5")
time.sleep(0.15)

#mes de nacimiento de usuario
mesNacimiento = driver.find_element(By.NAME, "month")
mesNacimiento.send_keys("Diciembre")
time.sleep(0.15)

#año de nacimiento de usuario
anoNacimiento = driver.find_element(By.NAME, "year")
anoNacimiento.send_keys("1996")
time.sleep(0.15)

#click siguiente pre-finalizar reserva
driver.find_element(By.CLASS_NAME, "js-complexFormButton-Submit").click()
time.sleep(1.5)

time.sleep(10000)




