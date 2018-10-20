# .*. coding: utf-8 .*.
import csv
import os

dict_code=dict()
values=[]
key=[]

with open("Code_Facturation_Inlog.csv") as facturation:
    dict_temp=dict()
    temp = csv.reader(facturation)
    for row in temp:
        dict_temp[row[0]]=row[1]
        dict_code.update(dict_temp)

with open("Code_Produits_Inlog.csv") as products:
    dict_temp=dict()
    temp = csv.reader(products)
    for row in temp:
        dict_temp[row[0]]=row[1]
        dict_code.update(dict_temp)

for i in dict_code.keys():
    key.append(str(i))

with open("test.csv") as csvfile:
    temp = csv.reader(csvfile)
    for row in temp:
        val=row[1]
        if val[0]=='0':
            val=val[1:]
        if val in key:
            values.append(dict_code[val])

try:
    os.remove("result.txt")
except:
    pass

with open("result.txt", mode='w') as temp:
    pass

with open("result.txt", encoding="utf-8", mode='w') as result:
    for i in values:
        result.write(i+'\n')
