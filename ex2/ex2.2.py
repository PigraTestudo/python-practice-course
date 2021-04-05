import xlrd
import wget
from statistics import mean
from statistics import median

url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
wget.download(url)

wb = xlrd.open_workbook('salaries.xlsx')
sheet = wb.sheet_by_index(0)
i = 1
richestReg = 0
medianSalMax = 0

# Richest region by median salary
while i <= sheet.ncols:
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    subjects = vals[i][1:]
    medianSal = median(subjects)
    if medianSal > medianSalMax:
        medianSalMax = medianSal
        richestReg = i
    i += 1

# Most profitable job
i = 1
meanSalMax = 0
richestJob = 0
while i <= sheet.nrows - 2:
    vals = [sheet.col_values(colnum) for colnum in range(sheet.ncols)]
    subjects = vals[i][1:]
    meanSal = mean(subjects)
    if meanSal > meanSalMax:
        meanSalMax = meanSal
        richestJob = i
    i += 1

print(sheet.row_values(richestReg)[0], sheet.col_values(richestJob)[0])
