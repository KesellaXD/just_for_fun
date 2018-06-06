#coding:utf-8
import os
import time
import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
#from openpyxl.style import Fonts, Style
os.chdir(r'C:\Users\93181\Desktop\parttimejob')
month = time.strftime('%m',time.localtime(time.time()))
day = time.strftime('%d',time.localtime(time.time()))
print(month)
print(day)
wb = openpyxl.load_workbook('template5.xlsx')
sheet1 = wb.get_sheet_by_name('Sheet1')
sheet1['A2']=str(int(month)) + '月'
sheet1['A3']=str(int(day)) + '日'
sheet2 = wb.get_sheet_by_name('Sheet2')
sheet2['A2']=str(int(month)) + '月'
sheet2['A3']=str(int(day)) + '日'
sheet1['A1':'BE66'].border = Border(left=Side(border_style='thin',color='FF000000'),
right=Side(border_style='thin',color='FF000000'),
top=Side(border_style='thin',color='FF000000'),
bottom=Side(border_style='thin',color='FF000000'))
wb.save('2018'+ month + day +'.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
# sheet.columns(1)
# print(sheet['A' + str(1)].value)
