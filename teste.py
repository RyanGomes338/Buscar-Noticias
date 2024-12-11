from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://g1.globo.com/")

search_box = driver.find_element(By.ID, "busca-campo")
search_box.send_keys("Inteligência Artificial")
search_box.submit()

time.sleep(5) 


noticias = driver.find_elements(By.CLASS_NAME, "widget--info__title")

datas = driver.find_elements(By.CLASS_NAME, "widget--info__meta")


with open("noticias.txt", "a") as news_file: 
    for noticia, data in zip(noticias, datas):
        try: 
            titulo = noticia.text 
            data_publicacao = data.text
            news_file.write(f"Título: {titulo}\n") 
            news_file.write(f"Data de Publicação: {data_publicacao}\n") 
            news_file.write("-" * 50 + "\n")
        except: 
            continue

driver.quit()
