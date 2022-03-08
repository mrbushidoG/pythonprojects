from openpyxl import Workbook

wb = Workbook()
#ws1 = wb.active
ws1 = wb.create_sheet("Range numbers")
for row in range(1,40):
    ws1.append(range(600))

#ws2 = wb.active
ws2 = wb.create_sheet("Second Range")

for row in range(1,40,2):
    ws2.append(range(200))

wb.save("C:\\Users\\mrbushido90\\workbook.xlsx")

#wb.close()