# -*- coding: utf-8 -*-
"""
@author : Nicolas
"""
import csv
import os

try:
    os.remove("AFN_transpose.csv")
except:
    pass

with open("AFN_transpose.csv", mode='w') as temp:
    pass

sh = 0
ud = 0
cle=["ud","sh","gc","ge","rd","rf","rj","rl","rm","rn","rp","pj","pm","qd","qh"]
with open("181017151004_2119332-Anonyme.AFN.txt", 'r', encoding='utf-8') as file:
    for line in file:
        if line[0]+line[1] in cle:
            if line[0]+line[1] == "sh":
                sh += 1
                if sh == 1:
                    with open("AFN_transpose.csv", 'a') as result:
                        result.write(line)
            elif line[0]+line[1] == "ud":
                ud += 1
                if ud == 1:
                    with open("AFN_transpose.csv", 'a') as result:
                        result.write(line)
            else:
                with open("AFN_transpose.csv", 'a') as result:
                    result.write(line)
