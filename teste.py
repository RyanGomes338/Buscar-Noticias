from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://g1.globo.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Inteligência Artificial")
search_box.submit()

time.sleep(5) 

noticias = driver.find_elements(By.CSS_SELECTOR, "feed-post-body-title")
datas = driver.find_elements(By.CSS_SELECTOR, "feed-post-datetime")

with open("noticias.txt", "w", encoding="utf-8") as file: 
    for noticia, data in zip(noticias, datas):
        try: 
            titulo = noticias.text 
            data_publicacao = data.text
            file.write(f"Título: {titulo}\n") 
            file.write(f"Data de Publicação: {data_publicacao}\n") 
            file.write("-" * 50 + "\n")
        except: 
            continue

driver.quit()