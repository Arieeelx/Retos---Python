import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://deportespuentealto.cl/recintos")
time.sleep(2)

#Busca el tipo de instalación
campoBusqueda = driver.find_element(By.NAME, "macrotag_id")
campoBusqueda.send_keys("Instalaciones deportivas")
time.sleep(0.5)

#Busca la reserva
campoReserva = driver.find_element(By.NAME, "tag_id")
campoReserva.send_keys("Futbolito")
time.sleep(0.5)

#Cambiar fecha a la correspondiente
campoFecha = driver.find_element(By.NAME, "date")
campoFecha.clear()
campoFecha.send_keys("31/07/2025")
time.sleep(0.5)

#Hora siempre en 00:00
campoHora = driver.find_element(By.NAME, "start_time")
campoHora.send_keys("00:00")
time.sleep(0.5)

#click en botónn
driver.find_element(By.CLASS_NAME, "homeSearchForm-button").click()
time.sleep(4)

#click en complejo a reservar
driver.find_element(By.CSS_SELECTOR, "[title='COMPLEJO DOMINGO TOCORNAL']").click()
time.sleep(4)

driver.find_element(By.XPATH, "//a[contains(@class, 'complexTimeRange-Tag') and text()='10:00-11:00hrs']").click()
time.sleep(4)

time.sleep(10000)




