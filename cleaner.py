import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

#filepath of my csv
file_data2017 = './full_2017.csv'
file_data2018 = './full_2018.csv'
file_data2019 = './full_2019.csv'
file_data2020 = './full_2020.csv'

columns_to_remove = ['id_mutation','adresse_numero','adresse_suffixe','adresse_nom_voie',
                    'adresse_code_voie','code_commune','ancien_code_commune','ancien_nom_commune',
                    'id_parcelle','ancien_id_parcelle','numero_volume','lot1_numero','lot1_surface_carrez',
                    'lot2_numero','lot2_surface_carrez','lot3_numero','lot3_surface_carrez',
                    'lot4_numero','lot4_surface_carrez','lot5_numero','lot5_surface_carrez',
                    'nombre_lots','code_type_local','code_nature_culture','code_nature_culture_speciale',
                    'nature_culture','nature_culture_speciale']


def cleaner_csv(file_path) : 
    #big clean thanks to pandas profiling
    df = pd.read_csv(file_path,delimiter = ',')
    df = df.drop(columns=columns_to_remove)
    df = df.dropna()
    #just keep the unabridged values
    quantil_25=df["valeur_fonciere"].quantile(q=0.25)
    quantil_75=df["valeur_fonciere"].quantile(q=0.75)
    #IQR = quantil_75 - quantil_25
    df= df[df["valeur_fonciere"]<quantil_75]
    df=df[df["valeur_fonciere"]>quantil_25]
    #df=df.astype(DataFrame)
    df = df.sample(frac = 0.2)
    return df



cleaner_csv(file_data2020).to_csv(r'/home/emilefaramond/Documents/PROJET_FINAL_DATAVIZ/CSVclean/clean_2020.csv', index = False)
cleaner_csv(file_data2017).to_csv(r'/home/emilefaramond/Documents/PROJET_FINAL_DATAVIZ/CSVclean/clean_2017.csv', index = False)
cleaner_csv(file_data2018).to_csv(r'/home/emilefaramond/Documents/PROJET_FINAL_DATAVIZ/CSVclean/clean_2018.csv', index = False)
cleaner_csv(file_data2019).to_csv(r'/home/emilefaramond/Documents/PROJET_FINAL_DATAVIZ/CSVclean/clean_2019.csv', index = False)


print(cleaner_csv(file_data2020)['nature_mutation']).values()
#On calcule la borne inférieure à l'aide du Q1 et de l'écart interquartile
#borne_inf = 20000
#print(borne_inf)
#On calcule la borne supérieure à l'aide du Q3 et de l'écart interquartile
#borne_sup = q3 +1.5*IQR
#print(borne_sup)
#On sélectionne une partie représentative du dataset
#On créé un nouveau fichier csv
#compression_opts = dict(method='zip', archive_name='2017new.csv')  
#dfpropre.to_csv('2017.zip', index=False, compression=compression_opts)