import xlrd
import sys
import wget
import zipfile

url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
wget.download(url)

z = zipfile.ZipFile('rogaikopyta.zip', 'r')
z.extractall()
z.close()
stdoutOrigin = sys.stdout
sys.stdout = open('ex2.4.txt', 'w', encoding='utf-8')

names = []
salaries = []

for i in range(1, 1001):
    PATH = str(i) + '.xlsx'
    wb = xlrd.open_workbook(PATH)
    sheet = wb.sheet_by_index(0)
    names.append(sheet.row_values(1)[1])
    salaries.append(sheet.row_values(1)[3])

data = zip(names, salaries)
data_s = sorted(data, key=lambda tup: tup[0])
names = [x[0] for x in data_s]
salaries = [x[1] for x in data_s]

for i in range(len(names)):
    print(names[i], int(salaries[i]))

sys.stdout.close()
sys.stdout = stdoutOrigin
