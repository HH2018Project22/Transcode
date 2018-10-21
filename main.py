import os

import functions

FILE_AFNOR = "181017151004_2119332-Anonyme.AFN.txt"
FILE_AFNOR_2 = "181017151004_2119332-Anonyme.AFN_fer.txt"

functions.recuperation(FILE_AFNOR, "temp1.csv")
functions.translate("temp1.csv", "temp2.csv")
functions.analysis("temp2.csv", "prescription.obj")

functions.recuperation(FILE_AFNOR_2, "temp3.csv")
functions.translate("temp3.csv", "temp4.csv")
functions.analysis("temp4.csv", "prescription_fer.obj")

try:
    os.remove("temp1.csv")
    os.remove("temp2.csv")
    os.remove("temp3.csv")
    os.remove("temp4.csv")
except FileNotFoundError:
    pass

OBJ = functions.load_object("prescription.obj")
OBJ2 = functions.load_object("prescription_fer.obj")

functions.compare_prescription(OBJ, OBJ2)
