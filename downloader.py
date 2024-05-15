import requests
from bs4 import BeautifulSoup


link = input("Введите ссылку на клип: ")

response = requests.get(link)

if response.status_code == 200:
    page = BeautifulSoup(response.text, "html.parser")
    # print(page)
    # print(response.text)
    link_clip = page.findAll("div", class_ = "Layout-sc-1xcs6mc-0 isUGlE")
    print(link_clip)
else:
    print(f"Неверный статус - {response.status_code}")