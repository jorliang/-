import xlrd
import xlwt
import os

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
workbook.save('Excel_Workbook.xls')
os.startfile('Excel_Workbook.xls')
