import pandas as pd
import numpy as np
from enr_fra.map.Ld_map.Load_map import Load_map_dep
from enr_fra.map.Ld_map.Load_map import Load_map_reg




class ConsumptionBy:

    """
    This class create a dataframe which provide
    the French electricity consumption from 2019 to 2021
    by department or regions.
    
    It uses two data from the following websites:
    
    INSEE data:
    https://www.insee.fr/fr/information/5057840

    ENEDIS data:
    https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/information/
    
    """

    def getDataFast(COL):

        """
        Take the data that is already created and stored in the ./DataSet repository.
        Please prefer this attribute to get the data.
        
        :param str collectivity: 'DEP' or 'REG'
        
        :returns: csv file with the consumption by collectivity
        :rtype: pandas.Series
        
        """

        if COL == 'DEP':
            data = pd.read_csv('./DataSet/departements_consumption.csv', sep = ',')

        elif COL == 'REG':
            data = pd.read_csv('./DataSet/regions_consumption.csv', sep = ',')

        else: raise Exception("please give any of the following values as arguments : 'DEP' or 'REG' ")

        return data


    def getDataSlow(COL):

        """
        Create the data using those from the website specified above.
        
        .. WARNING::
            Be Careful! It takes around 8 minutes to create it,
            but the data will be up to date.
        
        :param str collectivity: 'DEP' or 'REG'
        
        :returns: csv file with the consumption by collectivity
        :rtype: pandas.Series
            
        """

        url_cons = 'https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        selected = ['Code INSEE de la commune', 'Consommation annuelle moyenne de la commune (MWh)']
        df_cons = pd.read_csv(url_cons, usecols = selected, sep = ";", float_precision = 'legacy')
        df_cons = df_cons.drop_duplicates().reset_index(drop = True)
        df_cons.rename(columns = {'Code INSEE de la commune':'COM', 'Consommation annuelle moyenne de la commune (MWh)':'Conso'}, inplace = True)
        
        url_com = 'https://www.insee.fr/fr/statistiques/fichier/5057840/commune2021-csv.zip'

        selected2 = ['COM', COL]
        df_2 = pd.read_csv(url_com, compression='zip', usecols = selected2, sep = ",")

        df_cons[['COM']] = df_cons[['COM']].astype(str)

        conso_col = pd.merge(df_cons, df_2, on='COM')
        conso_col = conso_col[['Conso', COL]]
        conso_col = conso_col.dropna()
        conso_col.round({'Conso': 2})
        conso_col = conso_col.groupby([COL])['Conso'].mean().reset_index()
        conso_col[COL] = conso_col[COL].astype(int)
        conso_col[COL] = conso_col[COL].astype(str)

        return conso_col
