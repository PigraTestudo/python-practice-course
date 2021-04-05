from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

total = 0
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
html = resp.read()
soup = BeautifulSoup(html, "html.parser")
for line in soup.find_all('td'):
    total += int(line.get_text())
print(total)
