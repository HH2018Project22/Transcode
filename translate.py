# .*. coding: utf-8 .*.
"""
Author: Korgan
"""
import csv
import os

def translate(filename):
    """Analyse filename"""
    dict_code = dict()
    values = []
    keys = []
    key = []

    with open("Code_Facturation_Inlog.csv") as facturation:
        dict_temp = dict()
        temp = csv.reader(facturation)
        for row in temp:
            dict_temp[row[0]] = row[1]
            dict_code.update(dict_temp)

    with open("Code_Produits_Inlog.csv") as products:
        dict_temp = dict()
        temp = csv.reader(products)
        for row in temp:
            dict_temp[row[0]] = row[1]
            dict_code.update(dict_temp)

    for i in dict_code.keys():
        keys.append(str(i))

    with open(filename) as csvfile:
        temp = csv.reader(csvfile)
        for row in temp:
            val = row[1]
            key.append(row[0])
            if val[0] == '0' and row[0] != "ud":
                val = val[1:]
            if val in keys:
                values.append(dict_code[val])
            else:
                values.append(val)

    try:
        os.remove("result.csv")
    except:
        pass

    with open("result.csv", mode='w') as temp:
        pass


    with open("result.csv", 'w', newline='') as temp:
        spamwritter = csv.writer(temp, delimiter=',')
        for i, j in zip(key, values):
            spamwritter.writerow([i, j])

    # with open("result.txt", encoding="utf-8", mode='w') as result:
    #     for i in values:
    #         result.write(i+'\n')

translate("AFN_transpose.csv")
