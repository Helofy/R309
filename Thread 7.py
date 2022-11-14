import time
import concurrent.futures
import requests
img_urls = ['https://cdn.pixabay.com/photo/2018/02/23/21/50/hammer-3176709__340.png']
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[9]
    with open(img_name + '.jpg', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")