import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.inspection import PartialDependenceDisplay

data = pd.read_csv('data/dataset_inquilinos.csv', index_col = 'id_inquilino')
#print(data.head())

#CONVERTING THE COLUMNS NAMES IN ORDER TO BE MORE DESCRIPTIVE
data.columns = ['schedule', 'biorythm', 'studies_level', 'read', 'animation_series', 
'cinema', 'pets', 'cook', 'sport', 'diet', 'smoker',
'visits', 'orderliness', 'musica_genre', 'high_volume_music', 'perfect_plan', 'play_instrument'
]
'''
Input:
*   id_inquilinos: list with tenants requested
    topn: number of tenants to search

    
'''
def tenant_compatibility(tenant_id,topn):
    for tenant in tenant_id:
        if tenant not in new_similarity_matrix.index:
            return "One of the tenants was not found"
    
    #BUILDING A NEW MATRIX WITH SIMILARITY FOR THE REQUESTED TENANTS
    requested_tenants_lines = new_similarity_matrix.loc[tenant_id]
    
    #print(filas_inquilinos)

    #CALCULATING SIMILARITY AVERAGE FOR EACH TENANTS
    average_similarity = requested_tenants_lines.mean(axis = 0)
    #print(similitud_promedio.tail(5)) 

    #SORTING TENANTS BY THEIR SIMILARITY AVERAGE
    most_compatible = average_similarity.sort_values(ascending = False)
    #print(most_compatible.head(5))

    #EXCLUDE REQUESTED TENANTS
    most_compatible = most_compatible.drop(tenant_id)
    #print(most_compatible)

    
    #TOPN TENANTS MOST COMPATIBLE
    most_compatible = most_compatible.head(topn)
    #print(most_compatible)

    #OBTAIN REGISTERS FROM MOST COMPATIBLE TENANTS
    registers_top_tenants = data.loc[most_compatible.index]
    #print(regsitros_del_top)

    #OBTAIN REGISTER OF REQUESTED TENANTS
    requested_tenants_registers = data.loc[tenant_id]
    #print(inquilinos_pedidos)

    #CONCATENATE LOS REGISTROS BUSCADOS CON LOS REGISTROS SIMILARES
    #CONCATENATE REQUESTED REGISTERS WITH SIMILARITY ONE'S
    registers = pd.concat([requested_tenants_registers.T, registers_top_tenants.T], axis = 1)
    #print(registros)

    #CREATING A PANDA SERIES WITH THE MOST COMPATIBLES

    similarity_series = pd.Series(data = most_compatible.values, index = most_compatible.index, name = "Similarity")
    #print(similarity_series)

#def dependancedisplay(onehot_model, val_X, [feat_name]):
    #PartialDependenceDisplay.from_estimator()

    
#APPLYING ONEHOTENCODER IN ORDER TO REPRESENT DATASET ATTRIBUTES AS 0/1 VALUES
encoder = OneHotEncoder(sparse_output=False)
data_encoded = encoder.fit_transform(data)

#WATCH EVERY ATTRIBUTES WE TURNED
encoded_feature_names = encoder.get_feature_names_out()

#CALCULATING SIMILARITY MATRIX
matriz_s = np.dot(data_encoded,data_encoded.T)
#print(matriz_s)
#ESTABLISHING MIN AND MAX RANGE
rango_min = -100
rango_max = 100
 
#MAX AND MINS OF MATRIX
min_original = np.min(matriz_s)
max_original = np.max(matriz_s)

#REESCALING THE MATRIX, SO WE HAVE VALUES IN NORMAL % RANGES
matriz_reescalada = ((matriz_s-min_original) / (max_original - min_original))*(rango_max - rango_min) + rango_min
print(matriz_reescalada)

#BUILDING NEW DATAFRAME WITH EACH PERCENTAGES
new_similarity_matrix = pd.DataFrame(matriz_reescalada, index = data.index, columns = data.index)
#print(new_similarity_matrix)

tenants_list = np.random.randint(1,12000,7)
tenant_compatibility(tenants_list,7)
dependancedisplay(matriz_reescalada)



 



    
    

