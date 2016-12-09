# coding= shift_jis

import xlwt
import os

os.chdir('/home/masakazu-o/tmp')

book = xlwt.Workbook()
#book.add_sheet('NewSheet_1')
#book.save('sample.xls')

newSheet_1 = book.add_sheet('NewSheet_1')

"""
newSheet_1.write(0, 0, 'A1')

newSheet_1_row_1 = newSheet_1.row(1)
newSheet_1_row_1.write(0, 'A2')
newSheet_1_row_1.write(1, 'B2')
newSheet_1_row_1.write(2, 'C2')
newSheet_1_row_1.write(3, 'D2')
newSheet_1_row_1.write(4, 'E2')

newSheet_1_column_1 = newSheet_1.col(2)
newSheet_1_column_1.width = 5000
"""

c_font_1 = xlwt.Font()
c_font_1.bold = True
c_style_1 = xlwt.XFStyle()
c_style_1.font = c_font_1

c_font_2 = xlwt.Font()
c_font_2.name = 'Arial'
c_style_2 = xlwt.XFStyle()
c_style_2.font = c_font_2

newSheet_1.write(0, 0, 'Font-Bold', c_style_1)
newSheet_1.write(1, 0, 'Font-Arial', c_style_2)

book.save('sample.xls')
