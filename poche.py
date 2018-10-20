# -*- coding: utf-8 -*-
"""
@author : Nicolas
"""
class Poche():
    """docstring for Poche."""
    def __init__(self, contenu):
        """Initialization of the blood pocket"""
        self.contenu = contenu
        self.phenotype = False
        self.irradier = False
        self.code_identification = 0

    def __repr__(self):
        """Command Line representation of the pocket"""
        print("""La poche contient : {0}\nElle est irradiée ? {1}
Elle est phénotypé ? {2}\nSon code d'identification est : {3}""".format(\
self.contenu, self.phenotype, self.irradier, self.code_identification) )

    def __str__(self):
        return ''

    def set_code_identification(self, code_identification):
        """Set code identifier of the blood pocket"""
        self.code_identification = code_identification

    def set_irradier(self, boolean):
        """Set the irradiation caracteristic of the blood pocket"""
        self.irradier = boolean

    def set_phenotype(self, boolean):
        """Set the phenotype caracteristic of the blood pocket"""
        self.phenotype = boolean

    def get_code_identification(self):
        """Get code identifier of the blood pocket"""
        return self.code_identification

    def get_irradier(self):
        """Get the irradiation caracteristic of the blood pocket"""
        return self.irradier

    def get_phenotype(self):
        """Get the phenotype caracteristic of the blood pocket"""
        return self.phenotype

    def get_contenu(self):
        """Get the contain of the blood pocket"""
        return self.contenu
