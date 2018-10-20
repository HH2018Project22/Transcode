# -*- coding: utf-8 -*-
"""
@author : Nicolas
"""

class Prescription():
    """docstring for Prescription."""
    def __init__(self, service_distributeur):
        """Initialization for Prescription object"""
        self.nom = []
        self.id_inlog = 0
        self.id_etablissement = 0
        self.service_distributeur = service_distributeur
        self.service_prescripteur = 0
        self.etablissement = 0
        self.bon_commande = 0
        self.sexe = ""
        self.naissance = []
        self.lieu_naissance = ""
        self.poches = dict()

    def __repr__(self):
        """Command Line representation of the prescription"""
        print("""Le nom du patient est {0} {1}.\nSon id inlog est {2}.
Son id etablissement est {3}.\nLe prescripteur est {4}, {5}.
Le service distributeur est {6}.\nLe bon de commande est {7}.
Le sexe est {8}.\nLa date de naissance est {9}/{10}/{11}.
Le lieu de naissance est {12}.\n""".format(self.nom[0],\
self.nom[1], self.id_inlog, self.id_etablissement, self.service_prescripteur,\
self.etablissement, self.service_distributeur, self.bon_commande, self.sexe,\
self.naissance[0], self.naissance[1], self.naissance[2], self.lieu_naissance))
        for val in self.poches.values():
            val.__repr__()

    def __str__(self):
        return ''

    def set_etablissement(self, etablissement):
        """Set the prescription's etablissement"""
        self.etablissement = etablissement

    def set_bon_commande(self, bon_commande):
        """Set the purchase order id"""
        self.bon_commande = bon_commande

    def set_nomf(self, nomf):
        """Set the last name"""
        self.nom.append(nomf)

    def set_pnom(self, pnom):
        """Set the first name"""
        self.nom.append(pnom)

    def set_sexe(self, sexe):
        """Set the sexe"""
        self.sexe = sexe

    def set_naissance(self, naissance):
        """Set the birth date"""
        self.naissance.append(naissance[6:])
        self.naissance.append(naissance[4:6])
        self.naissance.append(naissance[:4])

    def set_lieu_naissance(self, lieu):
        """Set the birth place"""
        self.lieu_naissance = lieu

    def set_id_etablissement(self, id_etablissement):
        """Set the id hospital"""
        self.id_etablissement = id_etablissement

    def set_id_inlog(self, id_inlog):
        """Set the id in inlog"""
        self.id_inlog = id_inlog

    def set_poches(self, poche):
        """Set the poche"""
        self.poches.update(poche)

    def set_service_prescripteur(self, prescripteur):
        """Set prescriptor's service"""
        self.service_prescripteur = prescripteur



    def get_nom(self):
        """Return name"""
        return self.nom

    def get_etablissement(self):
        """Return the etablissment"""
        return self.etablissement

    def get_bon_commande(self):
        """Return the purchase order id"""
        return self.bon_commande

    def get_sexe(self):
        """Return the sexe"""
        return self.sexe

    def get_naissance(self):
        """Return the birth date"""
        return self.naissance

    def get_lieu_naissance(self):
        """Return the birth place"""
        return self.lieu_naissance

    def get_poches(self):
        """Return the poches"""
        return self.poches

    def get_id_inlog(self):
        """Return the id in inlog"""
        return self.id_inlog

    def get_service_prescriveur(self):
        """Return prescriptor's service"""
        return self.service_prescripteur

    def get_service_distributeur(self):
        """Return prescriptor's service"""
        return self.service_distributeur

    def get_id_etablissement(self):
        """Return the id in the etablissement"""
        return self.id_etablissement
