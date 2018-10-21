# .*. coding:utf-8 .*.

import csv
import os
import pickle

import poche
import prescription

DICT_CODE = dict()




def recuperation(inputname, outputname):
    """Get all data needed in the bases AFNOR file"""
    SH = 0
    UD = 0
    EJ = 0

    try:
        os.remove(outputname)
    except FileNotFoundError:
        pass

    with open(outputname, mode='w'):
        pass

    cle = ["ud", "sh", "ge", "rd", "rf", "rj", "rl", "rm", "rn", "rp", "pj", "pm", "qd", "ej"]
    with open(inputname, 'r', encoding='utf-8') as file:
        for line in file:
            if line[0]+line[1] in cle:
                if line[0]+line[1] == "sh":
                    SH += 1
                    if SH == 1:
                        with open(outputname, 'a') as result:
                            result.write(line)
                elif line[0]+line[1] == "ud":
                    UD += 1
                    if UD == 1:
                        with open(outputname, 'a') as result:
                            result.write(line)
                elif line[0]+line[1] == "ej":
                    EJ += 1
                    if EJ == 1:
                        with open(outputname, 'a') as result:
                            result.write(line)
                else:
                    with open(outputname, 'a') as result:
                        result.write(line)

def translate(inputname, outputname):
    """Analyse filename"""
    VALUES = []
    KEY = []
    KEYS = []

    with open("Code_Facturation_Inlog.csv") as facturation:
        dict_temp = dict()
        temp = csv.reader(facturation)
        for row in temp:
            dict_temp[row[0]] = row[1]
            DICT_CODE.update(dict_temp)

    with open("Code_Produits_Inlog.csv") as products:
        dict_temp = dict()
        temp = csv.reader(products)
        for row in temp:
            dict_temp[row[0]] = row[1]
            DICT_CODE.update(dict_temp)

    for i in DICT_CODE:
        KEYS.append(str(i))

    with open(inputname) as csvfile:
        temp = csv.reader(csvfile)
        for row in temp:
            val = row[1]
            KEY.append(row[0])
            if val[0] == '0' and row[0] != "ud":
                val = val[1:]
            if val in KEYS:
                VALUES.append(DICT_CODE[val])
            else:
                VALUES.append(val)

    try:
        os.remove(outputname)
    except FileNotFoundError:
        pass

    with open(outputname, mode='w') as temp:
        pass

    temp = 0
    with open(outputname, 'w', newline='') as temp:
        spamwritter = csv.writer(temp, delimiter=',')
        for i, j in zip(KEY, VALUES):
            spamwritter.writerow([i, j])

def analysis(inputname, outputname):
    """Analysing all input data in AFNOR format"""
    i = 0
    pocket = 0
    pocket = dict()

    with open(inputname) as temp:
        spamreader = csv.reader(temp)
        for row, w in zip(spamreader,range(19)):
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

    with open(outputname, "wb") as test:
        pickle.dump(file, test)


def load_object(inputname):
    """Loading previously created object."""
    with open(inputname, "rb") as test:
        obj = pickle.load(test)
    return obj

def compare_prescription(presc1, presc2):
    """Make a compareason between two prescription"""
    dict_attribute1 = {"Name":presc1.get_nom,
                       "Id_inlog":presc1.get_id_inlog,
                       "Id_etablissement":presc1.get_id_etablissement,
                       "Service_distributeur":presc1.get_service_distributeur,
                       "Servce_prescriveur":presc1.get_service_prescriveur,
                       "Etablissement":presc1.get_etablissement,
                       "Bon_commande":presc1.get_bon_commande,
                       "Sexe":presc1.get_sexe,
                       "Date_naissance":presc1.get_naissance,
                       "Lieu_naissance":presc1.get_lieu_naissance
                      }
    dict_attribute2 = {"Name":presc2.get_nom,
                       "Id_inlog":presc2.get_id_inlog,
                       "Id_etablissement":presc2.get_id_etablissement,
                       "Service_distributeur":presc2.get_service_distributeur,
                       "Servce_prescriveur":presc2.get_service_prescriveur,
                       "Etablissement":presc2.get_etablissement,
                       "Bon_commande":presc2.get_bon_commande,
                       "Sexe":presc2.get_sexe,
                       "Date_naissance":presc2.get_naissance,
                       "Lieu_naissance":presc2.get_lieu_naissance
                      }
    fatal_error = ["Name", "Etablissement", "Bon_commande", "Id_etablissement",\
                   "Contenu", "Code_ID"]

    for i in dict_attribute1:
        if dict_attribute1[i]() != dict_attribute2[i]():
            if i in fatal_error:
                print("Fatal Error!! at {0}, {1} does not match with {2}".format(i,\
                dict_attribute1[i](), dict_attribute2[i]()))
                return
            else:
                print("Important Warning! Take a look at {0}, {1} does not \
match with {2}".format(i, dict_attribute1[i](), dict_attribute2[i]()))
    print("Identity match. Starting comparing blood pocket.")

    poche_presc1 = presc1.get_poches()
    poche_presc2 = presc2.get_poches()

    for i, j in zip(poche_presc1.values(), poche_presc2.values()):
        dict_i = {"Contenu":i.get_contenu,
                  "Phenotype":i.get_phenotype,
                  "Irradier":i.get_irradier,
                  "Code_ID":i.get_code_identification
                 }
        dict_j = {"Contenu":j.get_contenu,
                  "Phenotype":j.get_phenotype,
                  "Irradier":j.get_irradier,
                  "Code_ID":j.get_code_identification
                 }

        for k in dict_i:
            if dict_i[k]() != dict_j[k]():
                if k in fatal_error:
                    print("Fatal Error!! at {0}, {1} does not match with {2}".format(k,\
                    dict_i[k](), dict_j[k]()))
                    return
                else:
                    print("Important Warning! Take a look at {0}, {1} does not \
match with {2}".format(i, dict_i[k](), dict_j[k]()))
    print("Identity match 100%. compareason is over.")
