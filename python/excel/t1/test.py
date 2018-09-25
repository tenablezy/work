import xlrd
# 打开 xls 文件
book = xlrd.open_workbook("test.xlsx")
print ("表单数量:", book.nsheets)
print ("表单名称:", book.sheet_names())
# 获取第1个表单
sh = book.sheet_by_index(0)
print ("表单 %s 共 %d 行 %d 列" % (sh.name, sh.nrows, sh.ncols))
print ("第二行第三列:", sh.cell_value(1, 2))
# 遍历所有表单
for s in book.sheets():
    for r in range(s.nrows):
        # 输出指定行
        print (s.row(r))

for s in book.sheets():
  print ('Sheet:',s.name)
  for row in range(s.nrows):
    values = []
    for col in range(s.ncols):
      print (chr(col+ord('A')),row+1,'-',s.cell(row,col).value)
