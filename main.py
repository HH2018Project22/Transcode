import os

import functions

FILE_AFNOR = "181017151004_2119332-Anonyme.AFN.txt"

functions.recuperation(FILE_AFNOR, "temp1.csv")
functions.translate("temp1.csv", "temp2.csv")
functions.analysis("temp2.csv", "prescription.obj")

try:
    os.remove("temp1.csv")
    os.remove("temp2.csv")
except FileNotFoundError:
    pass
