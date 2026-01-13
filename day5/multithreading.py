#Multithreading coding challenge-1 
import concurrent.futures 
import time 
import requests
import random 
import os 

def image_downloader(url):
    count = random.random()
    img_bytes = requests.get(url).content
    img_name = url.split("/")[3]
    img_name = f"{img_name}-{int(count * 1000)}.jpg"

    os.makedirs("images",exist_ok=True)
    img_path = os.path.join("images",img_name)

    with open(img_path,"wb") as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')
    return img_name + "Downloaded successfully."

        
url = "https://picsum.photos/2000/3000"

start = time.perf_counter()

# Normal Code - runs one by one 
# for _ in range(5):
#     image_downloader(url)

# multhreading code
with concurrent.futures.ThreadPoolExecutor() as executer:
    results = executer.map(image_downloader,[url] * 5)
    for result in results:
        print(result)

end = time.perf_counter()

print(f"Program Excecuted in {end - start} time.")