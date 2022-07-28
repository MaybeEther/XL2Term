import pandas as pd
import xlrd
def TooTerm(file):

    df = pd.read_excel(file)
    final = "+"
    dashes = ""
    spaces = ""
    largest = ""
    content = ("")
    celly = 0
    cellx = 0
    biggest = 0
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    if df.empty:
        print("This File is Empty!!!")
    else:
        for x in df.values.flatten().tolist():
            y = len(str(x))
            if y > biggest:
                biggest = y
        for x in range(biggest):
            dashes = (dashes + "-")
        for x in list(df):
            final = (final + dashes + "+")
        megafinale = (final)
        for x in range(df.shape[0] + 1):
            for x in range(df.shape[1]):
                spaces = biggest - len(str(sheet.cell_value(cellx, celly)))
                for x in range(spaces):
                    largest = largest + " "
                content = content + str(sheet.cell_value(cellx, celly)) + largest + "|"
                largest = ""
                celly = celly + 1
            cellx = cellx + 1
            celly = 0
            megafinale = megafinale + "\n|" + content + "\n" + final
            content = ("")
        print(megafinale)
