import numpy as np
import pandas as pd
numeros_aleatorios = np.random.randint(1,11, size=5)
df_numeros = pd.DataFrame(numeros_aleatorios, columns=['numeros'])

df_numeros['Dobles'] = df_numeros['numeros']*2

print(df_numeros)