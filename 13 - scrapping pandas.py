from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
import time

navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 10)

url = "https://www.distribuidoralira.cl/product-category/alimento-para-gatos/"
navegador.get(url)
data = []

while True:
    time.sleep(2)

    elementos_listado = navegador.find_elements(By.CSS_SELECTOR, 'div.product-small.col.has-hover.product')

    for elemento in elementos_listado:
        try:
            titulo_elemento = elemento.find_element(By.CSS_SELECTOR, 'p.name a')
            try:
                precio_elemento = elemento.find_element(By.CSS_SELECTOR, 'span.price ins span.amount')
            except NoSuchElementException:
                precio_elemento = elemento.find_element(By.CSS_SELECTOR, 'span.price span.amount')
            imagen = elemento.find_element(By.TAG_NAME, 'img').get_attribute('src')

            data.append({
                'Titulo': titulo_elemento.text,
                'Precio': precio_elemento.text,
                'Imagen': imagen,
            })
        except NoSuchElementException:
            pass

    try:
        siguiente = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.next.page-number')))
        siguiente.click()
    except (NoSuchElementException, TimeoutException):
        break

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

#df.to_json('data.json', orient='records', force_ascii=False, indent=4) <- json

navegador.quit()

