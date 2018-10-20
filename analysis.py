# .*. coding: utf-8 .*.
import csv

dict_code=dict()

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
