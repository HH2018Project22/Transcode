import os

import functions

FILE_AFNOR = "181017151004_2119332-Anonyme.AFN.txt"
FILE_AFNOR_2 = "181017151004_2119332-Anonyme.AFN_JJMM_commande.txt"

functions.recuperation(FILE_AFNOR, "temp1.csv")
functions.translate("temp1.csv", "temp2.csv")
functions.analysis("temp2.csv", "prescription.obj")

functions.recuperation(FILE_AFNOR_2, "temp1.csv")
functions.translate("temp1.csv", "temp2.csv")
functions.analysis("temp2.csv", "prescription_JJMM_commande.obj")

try:
    os.remove("temp1.csv")
    os.remove("temp2.csv")
except FileNotFoundError:
    pass

OBJ = functions.load_object("prescription.obj")
OBJ2 = functions.load_object("prescription_JJMM_commande.obj")

functions.compare_prescription(OBJ, OBJ2)
