import requests
from twitchAPI import twitch
from bs4 import BeautifulSoup


link = input("Введите ссылку на клип: ")

main_path = "B:\Projests\Downloader_twitch_clips\loaded_clips"

def request_twitch():
    response = requests.get(link)

    if response.status_code == 200:
        page = BeautifulSoup(response.text, "html.parser")
        # print(page)
        # print(response.text)
        link_clip = page.findAll("div", class_ = "Layout-sc-1xcs6mc-0 isUGlE")
        print(link_clip)
    else:
        print(f"Неверный статус - {response.status_code}")


if __name__=="__main__":
    request_twitch()