import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def extract_js(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        js_links = soup.find_all('script', src=True)
        
        os.makedirs("output/js", exist_ok=True)
        
        for link in js_links:
            js_url = urljoin(url, link.get('src'))  
            try:
                js_response = requests.get(js_url, headers=headers)
                js_filename = os.path.join("output/js", js_url.split('/')[-1])
                with open(js_filename, 'w', encoding='utf-8') as js_file:
                    js_file.write(js_response.text)
                print(f"JS файл сохранён: {js_filename}")
            except Exception as e:
                print(f"Ошибка при загрузке JS: {e}")
    else:
        print(f"Не удалось загрузить JavaScript, код: {response.status_code}")
