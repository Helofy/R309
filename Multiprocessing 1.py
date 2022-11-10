import time
import multiprocessing
import requests
def task():
    print(f"Task starts for 1 second")
    time.sleep(1)
    print(f"Task ends")

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name + '.jpg', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=download_image('https://cdn.pixabay.com/photo/2016/09/21/22/02/halloween-1685848__340.png'))
    p2 = multiprocessing.Process(target=download_image('https://cdn.pixabay.com/photo/2022/01/18/07/36/cat-6946498__340.jpg'))
    p3=multiprocessing.Process(target=download_image('https://cdn.pixabay.com/photo/2021/12/29/17/34/girl-6902365_640.png'))
    p1.start()
    p2.start()
    p3.start()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")