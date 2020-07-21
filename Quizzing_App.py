from openpyxl import Workbook as p
import openpyxl as P
from openpyxl.workbook import Workbook
# from openpyxl.workbook import load_workbook
from os import path

wb = Workbook()
ws = wb.active
wb.title = "Orgo"

ws.title = "Chapter 1"

ws1 = wb.create_sheet("Chapter 2")
ws2 = wb.create_sheet("Chapter 3")
ws3 = wb.create_sheet("Chapter 4")

d = ws.cell(4, 1, "Ikhla3")

for row in ws.values:
    for value in row:
        print(value)

for x in range(1, 4):
    for y in range(1, 4):
        ws.cell(x, y)


def load_workbook(wb_path):
    if path.exists(wb_path):
        return P.load_workbook(wb_path)
    return P.Workbook()


wb.save("scratch_file.xlsx")
wb2 = load_workbook("Microbiology.xlsx")

for row in ws.iter_rows(min_row=1, max_col=3, max_row=4, values_only=True):
    print(row)

"""
for sheet in wb:
    print(sheet.title)
"""


def new_workbook(namewb: str, namews: str):
    '''Makes a new workbook for a new subject you would like to be tested on. Allows you to name the workbook and
    your first sheet.'''
    wb = Workbook()
    ws = wb.active
    ws.title = namews
    wb.save(namewb + ".xlsx")


"""
new_workbook("Microbiology", "Chapter1")
"""  # This function has been tested and works because it created mirobiology


def add_worksheet(namewb: str, namews: str):
    """Adds a worksheet to an existing workbook"""




def new_question(question: str):
    ...


def new_ans():
    ...


wb1 = Workbook(True, True)
