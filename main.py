import sys
import pandas as pd
import xlrd

#FILE = sys.argv[1]

FILE = "test.xls"
df = pd.read_excel(FILE)
FINAL = ("+")
DASHES = ""
SPACES = ""
largest = ""
content = ("")
ROWS = df.size
COLUMNS = len(df)
LENGTH = list(range(ROWS))

cellY = 0
cellX = 0
biggest = 0
wb = xlrd.open_workbook(FILE)
sheet = wb.sheet_by_index(0)

if df.empty:
    print("This File is Empty!!!")
else:
    for x in df.values.flatten().tolist():
        y = len(str(x))
        if y > biggest:
            biggest = y
    for x in range(biggest):
        DASHES = (DASHES + "-")
    for x in list(df):
        FINAL = (FINAL + DASHES + "+")
    MegaFinale = (FINAL)
    for x in range(df.shape[0] + 1):
        for x in range(df.shape[1]):
            SPACES = biggest - len(str(sheet.cell_value(cellX, cellY)))
            for x in range(SPACES):
                largest = largest + " "
            content = content + str(sheet.cell_value(cellX, cellY)) + largest + "|"
            largest = ""
            cellY = cellY + 1
        cellX = cellX + 1
        cellY = 0
        MegaFinale = MegaFinale + "\n|" + content + "\n" + FINAL
        content = ("")
    print(MegaFinale)
