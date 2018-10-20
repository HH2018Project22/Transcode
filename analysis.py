# .*. coding: utf-8 .*.
"""
Author: Korgan
"""
import csv
import pickle
import poche
import prescription
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
        elif row[0] == "ej":
            file = prescription.Prescription(row[1])
        elif row[0] == "ud":
            file.set_service_prescripteur(row[1])
        elif row[0] == "sh":
            file.set_etablissement(row[1])
        elif row[0] == "ge":
            file.set_bon_commande(row[1])
        elif row[0] == "rd":
            file.set_nomf(row[1])
        elif row[0] == "rf":
            file.set_pnom(row[1])
        elif row[0] == "rj":
            file.set_sexe(row[1])
        elif row[0] == "rl":
            file.set_naissance(row[1])
        elif row[0] == "rm":
            file.set_lieu_naissance(row[1])
        elif row[0] == "rn":
            file.set_id_etablissement(row[1])
        elif row[0] == "rp":
            file.set_id_inlog(row[1])
        else:
            pass

    file.set_poches(pocket)

file.__repr__()
with open("test.obj","wb") as test:
    pickle.dump(file, test)
