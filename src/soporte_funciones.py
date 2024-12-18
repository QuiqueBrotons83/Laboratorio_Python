import pandas as pd

def abrir_csv(ruta, separador=';', codificacion='latin1'):
    return pd.read_csv(ruta,sep=separador,encoding=codificacion)

    

    
 


