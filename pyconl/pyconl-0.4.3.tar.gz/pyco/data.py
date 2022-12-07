import pandas as pd
import numpy as np

import pyco.basis
import pyco.waarde
import pyco.lijst

class pc:
    BasisObject = pyco.basis.BasisObject
    Waarde = pyco.waarde.Waarde
    Lijst = pyco.lijst.Lijst

class Data(pc.BasisObject):
    """
    Een Pandas DataFrame waarbij eigenschappen een eenheid kunnen hebben.

    AANMAKEN DATA  
        d = Data({'eigenschap1': 'eenheid1',           als eenheid dimensieloos:
                  'eigenschap2': 'eenheid2'})                  '-', '' of None
                  
    EIGENSCHAPPEN
        d.eigenschappen           lijst met aanwezige kolomnamen
        d.eenheden                lijst met eenheden die bij kolommen horen
        d.df                      Pandas DataFrame object     
        
    TOEVOEGEN DATA REGEL    in onderstaande gevallen: 4 eigenschappen (kolommen)
        d.toevoegen([7,5,3,1])             een Python list object
        d.toevoegen(4,5,6,7)               losse argumenten
        d.toevoegen(pc.Lijst(4,9,6,70))    een Lijst object
        d.toevoegen((14,15,16,17))         een Python tuple object

    OPHALEN DATA EIGENSCHAP       
        d['eigenschap1']          een Lijst object
        d.eigenschap1             indien naam eigenschap ook valide Python name
        d[0]                      Python list met waardes van 1e invoer (rij)
        d[3:8]                    Python list met waardes (ook Python list)
                                                    van 4e t/m 8e invoer (rijen)
        d[::2]                    Python list met alle oneven rijnummers
        d[:, 1:3]                 Python list met 2e en 3e kolom
                                                  (alleen waarden, geen eenheid)          
    """

    def __init__(self, lijst_dict):
        super().__init__()
        
        if not isinstance(lijst_dict, dict):
            raise TypeError("type argument 1 is GEEN dict: {}".format(type(lijst_dict)))
            
        lijst_dict = {k:(v if isinstance(v, str) and len(v) > 0 else '-') for k, v in lijst_dict.items()}
        self._dataframe = pd.DataFrame([], columns=pd.MultiIndex.from_tuples(
                [(gh, eh) for gh, eh in lijst_dict.items()]))
        
    @property
    def eigenschappen(self):
        """Lijst met aanwezige kolomnamen."""
        return [es for es, _ in self.df.columns]
    
    @property
    def eenheden(self):
        """Lijst met eenheden die bij eigenschappen (kolommen) horen"""
        return [eh for _, eh in self.df.columns]

        
    def toevoegen(self, *args):
        """Een nieuwe record toevoegen."""
        if len(args) == 1:
            if isinstance(args[0], list) or isinstance(args[0], tuple):
                args = args[0]
            elif isinstance(args[0], pc.Lijst):
                args = args[0].array
            else:
                args = [args[0]]
                
        if len(args) != len(self.eigenschappen):
            raise ValueError('aantal waardes ({}) is niet gelijk aan aantal kolomnamen ({}: {})'.format(len(args), len(self.eigenschappen), ', '.join(["'{}'".format(e) for e in self.eigenschappen])))
    
        tmp_df = pd.DataFrame([args], columns=pd.MultiIndex.from_tuples(
                [(es, eh) for es, eh in zip(self.eigenschappen, self.eenheden)]))
        self._dataframe = pd.concat([self._dataframe, tmp_df], ignore_index=True)
        
    @property    
    def df(self):
        """Een Pandas DataFrame object retourneren."""
        return self._dataframe
    
    def __getitem__(self, eigenschap_bereik):
        """Retourneert een eigenschap als Lijst (tekst invoer) of een aantal rijen van DataFrame (getal/bereik invoer)."""
        if isinstance(eigenschap_bereik, str):
            eigenschap = eigenschap_bereik
            if not eigenschap in self.eigenschappen:
                raise ValueError('Eigenschap \'{}\' is geen geldige eigenschap ({}).'.format(
                        eigenschap,
                        ', '.join(self.eigenschappen)))
            eenheid = self.eenheden[self.eigenschappen.index(eigenschap)]
            return pc.Lijst(self.df[eigenschap][eenheid].values.tolist()).gebruik_eenheid(eenheid)
        else:
            bereik = eigenschap_bereik
            rijen_lijst = self.df.iloc[bereik].values.tolist()
            return rijen_lijst
        
    def __getattr__(self, name):
        """Retourneert een eigenschap (zie __getitem__) ook als attribuut van object."""
        if name in self.eigenschappen:
            return self.__getitem__(name)
    
    def __repr__(self):
        object_str = self.__str__()
        return 'pyco.Data object:\n' + len(object_str.split('\n')[0])*'-' + '\n' + object_str
    
    def __str__(self):
        return str(self.df)


