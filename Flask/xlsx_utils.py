import openpyxl

def get_xlsx():
    book = openpyxl.open("studdents.xlsx", read_only= True)
    sheet = book.active
    html = []

    for row in  range(0, sheet.max_row):
        html.append(list())
        for index in range(0,8):
            html[row].append(str(sheet[row+1][index].value))

    return html