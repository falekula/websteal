import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def extract_images(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        
        os.makedirs("output/images", exist_ok=True)
        
        for img in img_tags:
            img_url = urljoin(url, img.get('src'))  
            try:
                img_response = requests.get(img_url, headers=headers)
                img_filename = os.path.join("output/images", img_url.split('/')[-1])
                with open(img_filename, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"Изображение сохранено: {img_filename}")
            except Exception as e:
                print(f"Ошибка при загрузке изображения: {e}")
    else:
        print(f"Не удалось загрузить изображения, код: {response.status_code}")
