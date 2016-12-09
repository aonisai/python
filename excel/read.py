# coding= shift_jis

import xlrd
import os

os.chdir("/home/masakazu-o/tmp")
#print(os.getcwd())
#print(os.listdir())

#book = xlrd.open_workbook('test_book.xls')
book = xlrd.open_workbook('kabu.xlsx')
"""
print("-----------------------------------")
print(book.nsheets)

print("-----------------------------------")
for name in book.sheet_names():
    print(name)
"""

print(book.sheet_by_index(0).name)
#print(book.sheet_by_name(u'Sheet1').name)

sheet_1 = book.sheet_by_index(0)
print(sheet_1.ncols)
print(sheet_1.nrows)

#for col in range(sheet_1.ncols):
for col in range(5):
    print('-------------------------------')
    #for row in range(sheet_1.nrows):
    for row in range(10):
        print(sheet_1.cell(row, col).value)
