import xmltodict
import wget


url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
wget.download(url)
fin = open('map1.osm', 'r', encoding='utf-8')

text = fin.read()
fin.close()
all_nodes = 0
with_tag = 0
dct = xmltodict.parse(text)
for node in dct['osm']['node']:
    all_nodes += 1
    if 'tag' in node:
        with_tag += 1

print(with_tag, all_nodes - with_tag)
