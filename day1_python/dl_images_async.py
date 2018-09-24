import aiohttp
import asyncio
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

base_url = 'https://www.stradia.in/cars/?page='
x = 1
img_urls, file_names = [], []
urls = [base_url + str(i) for i in range(2, 10)]
responses = []


# fetching an item from a url
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.read()


# fetching all urls
async def get_urls():
    tasks = []
    async with aiohttp.ClientSession(read_timeout=0) as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)

        global responses
        responses = await asyncio.gather(*tasks)


# parsing the page and getting the image url
def parse_url(page):
    soup = BeautifulSoup(page, 'lxml')
    a_tags = soup.find_all(class_='offer-item__photo-link')
    global x, img_urls, file_names
    for a_tag in a_tags:
        if not a_tag.has_attr('style'):
            continue
        img_urls.append(a_tag['style'][23:-2])
        file_names.append(str(x).zfill(6) + '.jpg')
        x += 1


# downloading all the images from image urls
async def get_images():
    tasks = []
    async with aiohttp.ClientSession(read_timeout=0) as session:
        for img_url in img_urls:
            task = asyncio.ensure_future(fetch(session, img_url))
            tasks.append(task)

        global responses
        responses = await asyncio.gather(*tasks)


# saving the image
def save_image(img, file_name):
    with open(file_name, 'wb') as f:
        f.write(img)


loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_urls())
loop.run_until_complete(future)

print("Downloaded pages")

url_pool = Pool()
url_pool.map(parse_url, responses)

print("Parsed pages")

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_images())
loop.run_until_complete(future)

print("Downloaded images")

img_pool = Pool()
img_pool.starmap(save_image, zip(responses, file_names))

print("Saved images")
