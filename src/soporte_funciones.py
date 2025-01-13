# En este documento nos encontramos con las funciones creadas para trabajar en el archivo de análisis de presupuestos de Brasil
<<<<<<< HEAD

import pandas as pd
import numpy as np
from pandas.api.types import is_datetime64_any_dtype as is_datetime
import seaborn as sns
import matplotlib.pyplot as plt

# Funcion para convertir una columna a tipo numerico
def convert_to_numeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df
# Funcion para contar valores unicos
def count_unique_values(df, column):
    return df[column].nunique()


=======

import pandas as pd
import numpy as np
from pandas.api.types import is_datetime64_any_dtype as is_datetime
import seaborn as sns
import matplotlib.pyplot as plt

# src/visualization.py
import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()



# src/data_cleaning.py
import pandas as pd

def clean_data(df):
    df = df.dropna()  # Eliminar filas con valores nulos
    return df


# src/analysis.py
import pandas as pd

def descriptive_stats(df):
    return df.describe()  # Devuelve estadísticas descriptivas del dataframe



>>>>>>> 41ca162979f59af72d6769f60e8c8c6d5745328c


    
 


