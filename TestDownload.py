import threading
import time
import requests
import multiprocessing
import concurrent.futures
import sys

img_url=['https://cdn.pixabay.com/photo/2021/12/29/17/34/girl-6902365_640.png','https://cdn.pixabay.com/photo/2022/01/18/07/36/cat-6946498__340.jpg','https://cdn.pixabay.com/photo/2016/09/21/22/02/halloween-1685848__340.png']


def download_image(img_url):
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[9]
        with open(img_name + '.jpg', 'wb') as img_file:
            img_file.write(img_bytes)
            print(f"{img_name} was downloaded")
try:
    y=sys.argv[1]
    a=int(y[5:1024])
except (ValueError):
    print("ce n'est pas une valeurs entière")
else:
    if __name__ == '__main__':
        for i in range(a):
            start = time.perf_counter()

            for i in range (len(img_url)):
                p1=threading.Thread(target=download_image, args=[img_url[i]])

                p1.start()

                p1.join()
            end = time.perf_counter()
            print(f"Tasks ended in {round(end - start, 2)} second(s)")

            start = time.perf_counter()
            p1 = multiprocessing.Process(
                target=download_image('https://cdn.pixabay.com/photo/2016/09/21/22/02/halloween-1685848__340.png'))
            p2 = multiprocessing.Process(
                target=download_image('https://cdn.pixabay.com/photo/2022/01/18/07/36/cat-6946498__340.jpg'))
            p3 = multiprocessing.Process(
                target=download_image('https://cdn.pixabay.com/photo/2021/12/29/17/34/girl-6902365_640.png'))
            p1.start()
            p2.start()
            p3.start()
            end = time.perf_counter()
            print(f"Tasks ended in {round(end - start, 2)} second(s)")

            start = time.perf_counter()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(download_image, img_url)
            end = time.perf_counter()
            print(f"Tasks ended in {round(end - start, 2)} second(s)")