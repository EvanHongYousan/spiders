__author__ = 'yantianyu'

import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.add_line(1)
wb.save('example.xls')
