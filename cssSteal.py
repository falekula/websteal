import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def extract_css(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        css_links = soup.find_all('link', rel="stylesheet")
        
        for link in css_links:
            css_url = urljoin(url, link.get('href'))
            parsed_url = urlparse(css_url)
            path = parsed_url.path.strip("/")
            directory = os.path.join("output", os.path.dirname(path))
            os.makedirs(directory, exist_ok=True)
            
            try:
                css_response = requests.get(css_url, headers=headers)
                css_filename = os.path.join("output", path)
                with open(css_filename, 'w', encoding='utf-8') as css_file:
                    css_file.write(css_response.text)
                print(f"CSS файл сохранён: {css_filename}")
            except Exception as e:
                print(f"Ошибка при загрузке CSS: {e}")
    else:
        print(f"Не удалось загрузить CSS, код: {response.status_code}")
