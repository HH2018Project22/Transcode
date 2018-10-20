# -*- coding: utf-8 -*-
"""
@author : Nicolas
"""
cle=["ud","sh","gc","ge","rd","rf","rj","rl","rm","rn","rp","pj","pm","qd","qh"]
with open("181017151004_2119332-Anonyme.AFN.txt", 'r', encoding='utf-8') as file:
    for line in file:
        if str(line[0]+line[1]) in cle:
            with open("AFN_transpose.csv", 'a') as result:
                result.write(line)
