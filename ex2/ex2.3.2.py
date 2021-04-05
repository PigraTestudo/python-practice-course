import xlrd
import math
import wget

total_cals = 0      # общее количество калорий
total_squirels = 0  # общее количество белков
total_fat = 0       # общее количество жиров
total_ugli = 0      # общее количество углеводов

# загрузка файла
url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'
wget.download(url)

# открытие файла
wb = xlrd.open_workbook('trekking2.xlsx')
calorii = wb.sheet_by_index(0)
raskladka = wb.sheet_by_index(1)

for i in range(1, 13):

    item_name = raskladka.row_values(i)[0]
    item_cal = raskladka.row_values(i)[1]

    for k in range(1, 38):

        item_compare = calorii.row_values(k)[0]
        if item_compare == item_name:
            try:
                total_cals += float(calorii.row_values(k)[1]) * float(item_cal) / 100
                total_squirels += float(calorii.row_values(k)[2]) * float(item_cal) / 100
                total_fat += float(calorii.row_values(k)[3]) * float(item_cal) / 100
                total_ugli += float(calorii.row_values(k)[4]) * float(item_cal) / 100
            except:
                ValueError

print(math.floor(total_cals), math.floor(total_squirels), math.floor(total_fat), math.floor(total_ugli))
