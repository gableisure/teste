from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()

""" options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage') """


DRIVER_PATH = '/home/gabriel/Área de Trabalho/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get('https://google.com')