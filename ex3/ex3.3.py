from bs4 import BeautifulSoup
import wget


url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
wget.download(url)

with open('map2.osm', "r", encoding='utf-8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml').find_all('node')
    s = BeautifulSoup(str(soup), 'lxml').find_all('tag', k='amenity', v='fuel')
    print(len(s))




