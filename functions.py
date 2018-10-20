# .*. coding:utf-8 .*.

import csv
import os
import pickle

import poche
import prescription





def recuperation(inputname, outputname):
    sh = 0
    ud = 0
    ej = 0

    try:
        os.remove(outputname)
    except:
        pass

    with open(outputname, mode='w'):
        pass

    cle = ["ud", "sh", "ge", "rd", "rf", "rj", "rl", "rm", "rn", "rp", "pj", "pm", "qd", "ej"]
    with open(inputname, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0]+line[1] in cle:
                if line[0]+line[1] == "sh":
                    sh += 1
                    if sh == 1:
                        with open(outputname, 'a') as result:
                            result.write(line)
                elif line[0]+line[1] == "ud":
                    ud += 1
                    if ud == 1:
                        with open(outputname, 'a') as result:
                            result.write(line)
                elif line[0]+line[1] == "ej":
                    ej += 1
                    if ej == 1:
                        with open(outputname, 'a') as result:
                            result.write(line)
                else:
                    with open(outputname, 'a') as result:
                        result.write(line)

def translate(inputname, outputname):
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

    with open(inputname) as csvfile:
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
        os.remove(outputname)
    except:
        pass

    with open(outputname, mode='w') as temp:
        pass


    with open(outputname, 'w', newline='') as temp:
        spamwritter = csv.writer(temp, delimiter=',')
        for i, j in zip(key, values):
            spamwritter.writerow([i, j])

def analysis(inputname, outputname):
    """Analysing all input data in AFNOR format"""
    i = 0
    pocket = dict()

    with open(inputname) as temp:
        spamreader = csv.reader(temp)
        for row in spamreader:
            if row[0] == "pj":
                i += 1
                pocket["poche_" + str(i)] = poche.Poche(row[1])
            elif row[0] == "pm":
                pocket["poche_" + str(i)].set_code_identification(row[1])
            elif row[0] == "qd":
                if "Irradié" in row[1]:
                    pocket["poche_" + str(i)].set_irradier(True)
                else:
                    pocket["poche_" + str(i)].set_phenotype(True)
            elif row[0] == "ej":
                file = prescription.Prescription(row[1])
                dico = {"ud" : file.set_service_prescripteur,
                        "sh" : file.set_etablissement,
                        "ge" : file.set_bon_commande,
                        "rd" : file.set_nomf,
                        "rf" : file.set_pnom,
                        "rj" : file.set_sexe,
                        "rl" : file.set_naissance,
                        "rm" : file.set_lieu_naissance,
                        "rn" : file.set_id_etablissement,
                        "rp" : file.set_id_inlog
                       }
            else:
                dico[row[0]](row[1])


        file.set_poches(pocket)

    file.__repr__()
    with open(outputname, "wb") as test:
        pickle.dump(file, test)


def load_object(inputname):
    """Loading previously created object."""
    with open(inputname, "rb") as test:
        obj = pickle.load(test)
        print(obj)
