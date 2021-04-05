import xlrd
import math
import wget

url = 'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'
wget.download(url)

wb = xlrd.open_workbook('trekking3.xlsx')

calorii = wb.sheet_by_index(0)
raskladka = wb.sheet_by_index(1)


def numberconter(day):
    total_cals, total_squirels, total_fat, total_ugli = 0, 0, 0, 0

    for m in range(1, 100):  # перебираются дни
        if raskladka.row_values(m)[0] == day:  # если найден искомый день
            item_name = raskladka.row_values(m)[1]  # перебираются продукты в раскладке
            item_cal = float(raskladka.row_values(m)[2]) / 100  # перебираются веса этих продуктов

            for k in range(1, 38):  # перебираются продукты в справочнике

                item_compare = calorii.row_values(k)[0]
                if item_compare == item_name:  # если нужный продукт найден
                    try:  # накапливаются данные о калориях, белках и тд
                        total_cals += float(calorii.row_values(k)[1]) * item_cal
                        total_squirels += float(calorii.row_values(k)[2]) * item_cal
                        total_fat += float(calorii.row_values(k)[3]) * item_cal
                        total_ugli += float(calorii.row_values(k)[4]) * item_cal
                    except:  # на случай если клетка окажется пустой
                        ValueError
    print(math.floor(total_cals), math.floor(total_squirels), math.floor(total_fat), math.floor(total_ugli))


for days in range(1, 10):
    numberconter(days)
