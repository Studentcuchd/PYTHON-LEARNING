import requests
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
from threading import Thread


img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start_time=time.time()

def image_downloader(url):
    image_bytes=requests.get(url).content
    image_name=url.split("/")[3]
    image_name=f"{image_name}.jpeg"
    
    with open(f'Threading_project/{image_name}','wb') as downloader:
        downloader.write(image_bytes)
        print(f"{image_name} downloaded successfully")
        
        
with ThreadPoolExecutor() as executor:
    executor.map(image_downloader,img_urls)
    
    
    
# without map
# with ThreadPoolExecutor() as executor:
#     image_comprehension=[executor.submit(image_downloader,url) for url in img_urls]
#     for i in as_completed(image_comprehension):
#         print(i.result())    
        
end_time=time.time()

print(f"Total time taken= {end_time-start_time}")



