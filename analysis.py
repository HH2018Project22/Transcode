# .*. coding: utf-8 .*.
"""
Author: Korgan
"""
import csv

import poche
i = 0
pocket = dict()

with open("result.csv") as temp:
    spamreader = csv.reader(temp)
    for row in spamreader:
        if row[0] == 'pj':
            i += 1
            pocket["poche_"+str(i)] = poche.Poche(row[1])
        elif row[0] == 'pm':
            pocket["poche_"+str(i)].set_code_identification(row[1])
        elif row[0] == 'qd':
            if 'Irradié' in row[1]:
                pocket["poche_"+str(i)].set_irradier(True)
            else:
                pocket["poche_"+str(i)].set_phenotype(True)
        else:
            pass

for val in pocket.values():
    val.__repr__()
    print("\n")
