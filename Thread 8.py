import threading
import time
import requests
img_url=['https://cdn.pixabay.com/photo/2021/12/29/17/34/girl-6902365_640.png','https://cdn.pixabay.com/photo/2022/01/18/07/36/cat-6946498__340.jpg','https://cdn.pixabay.com/photo/2016/09/21/22/02/halloween-1685848__340.png']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name + '.jpg', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()

    for i in range (len(img_url)):
        p1=threading.Thread(target=download_image, args=[img_url[i]])

        p1.start()

        p1.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")