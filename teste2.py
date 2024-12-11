from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o WebDriver (substitua o caminho pelo caminho do seu WebDriver)
driver_path = 'path/to/chromedriver'  # Exemplo: 'C:/path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Acessar o site do G1
    driver.get('https://g1.globo.com/')
    time.sleep(5)  # Esperar a página carregar

    # Encontrar a barra de pesquisa e buscar por "inteligência artificial"
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('inteligência artificial')
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Esperar os resultados carregarem

    # Encontrar os elementos que contêm os títulos das notícias
    articles = driver.find_elements(By.CSS_SELECTOR, 'div.feed-post-body-title')

    # Abrir um arquivo .txt para salvar as notícias
    with open('noticias_inteligencia_artificial.txt', 'w', encoding='utf-8') as file:
        for article in articles:
            title = article.text
            link = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
            file.write(f'Título: {title}\nLink: {link}\n\n')

finally:
    # Fechar o WebDriver
 driver.quit()