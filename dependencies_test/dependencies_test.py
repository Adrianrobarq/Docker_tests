# Vamos a probar a montar una imagen con varias dependencias
# y a ver si se instalan correctamente
# Importamos las librerías necesarias

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Vasmoa a crear un array de numpy
x = np.arange(1, 11)
y = np.random.randint(1, 10, size=10)

# Vamos a crear un dataframe de pandas
df = pd.DataFrame({'x': x, 'y': y})

# Vamos a crear un gráfico de dispersión con seaborn
sns.scatterplot(data=df, x='x', y='y')
plt.title('Gráfico de dispersión')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfico de dispersión con seaborn')
plt.show()