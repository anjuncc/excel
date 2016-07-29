# -*- coding:utf-8 -*-  
from openpyxl import load_workbook
wb2 = load_workbook('address.xlsx',read_only=True)
print wb2.get_sheet_names()
ws = wb2.get_sheet_by_name(u'工作表1')
keys = ['uniacid', 'openid', 'realname', 'mobile', 'province', 'city', 'area', 'address', 'isdefault', 'zipcode', 'deleted', 'sap_customer_addressid', 'sap_customer_name', 'sap_customerid']
rs=[]

for idx,row in enumerate(ws.rows):
	if idx == 0:  continue;
	vals =[]
	for cell in row:
		vals.append(cell.value) 
	d = dict(zip(keys,vals))
	print d
	rs.append(d)
