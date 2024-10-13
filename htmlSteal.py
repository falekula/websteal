import requests
from bs4 import BeautifulSoup
import os

def extract_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        html_content = soup.prettify()

        os.makedirs("output", exist_ok=True)
        with open("output/index.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        print("HTML успешно сохранён в 'output/index.html'.")
    else:
        print(f"Не удалось загрузить страницу, код: {response.status_code}")
