import cssSteal
import htmlSteal
import jsSteal
import imageSteal

def main():
    url = input("Введите ссылку на сайт: ")

    print("Извлечение HTML...")
    htmlSteal.extract_html(url)
    
    print("Извлечение CSS...")
    cssSteal.extract_css(url)
    
    print("Извлечение JavaScript...")
    jsSteal.extract_js(url)
    
    print("Извлечение изображений...")
    imageSteal.extract_images(url)

if __name__ == "__main__":
    main()
