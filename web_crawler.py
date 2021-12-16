# ---libraries for: download images---
import os
import requests
from bs4 import BeautifulSoup
import shutil


# escribe los temas enter comillas y separados por comas
def download_images(*temas):
    # delete any existing folder
    working_directory = os.getcwd()
    if os.path.exists(working_directory+'/image_pool'):
        shutil.rmtree(working_directory+'/image_pool')

    # ---download images variables---

    # link of google images
    GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
    }

    # name of the folder where the images will be save
    SAVE_FOLDER = 'image_pool'
    os.mkdir(SAVE_FOLDER)

    number_of_images_per_topic = 20

    for topic in temas:

        search_url = GOOGLE_IMAGE + 'q=' + topic.replace(' ', '+')

        # do the requests and create the soup to find the images containers
        response = requests.get(search_url, headers=usr_agent)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # extract images
        images_links = []
        for raw_link in soup.find_all('img', {'class': 'yWs4tf'}, limit=number_of_images_per_topic):
            images_links.append(raw_link.get('src'))

        # save each image with the following format: 'topic name' + image number
        for i, link in enumerate(images_links):
            response = requests.get(link)
            image_name = SAVE_FOLDER + '/' + topic + str(i + 1) + '.jpg'
            with open(image_name, 'wb') as file:
                file.write(response.content)

    file.close()