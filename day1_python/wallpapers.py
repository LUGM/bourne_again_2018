import requests
from bs4 import BeautifulSoup

base_url = "https://wallpaperstock.net/nature-wallpapers_p{}_1.html"
urls = []
img_urls = []

# creating webpage urls
for i in range(1, 2):
    urls.append(base_url.format(i))

# getting the image urls
for url in urls:
    page = requests.get(url).content
    soup = BeautifulSoup(page, 'lxml')
    tags = soup.find_all(class_=['image wide', 'image hd'])
    for tag in tags:
        thumbnail_url = 'http:' + tag.img['src']
        full_img_url = thumbnail_url.replace('thumbs', 'thumbs1')
        img_urls.append(full_img_url)

# downloading the images
for img_url in img_urls:
    file_name = img_url.split("/")[-1]
    image_data = requests.get(img_url).content
    f = open(file_name, "wb")
    f.write(image_data)
    print("Saved ", file_name)
