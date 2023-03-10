import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Liste tous les fichiers CSV dans le dossier "data"
all_files = glob.glob("data/*.csv")

# Lire les fichiers CSV dans des DataFrames Pandas et les concaténer
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Convertir la colonne "created_at" en format de date
df['created_at'] = pd.to_datetime(df['created_at'])

# Trier les données par date
df = df.sort_values(by=['created_at'])

# Supprimer les doubles
df = df.drop_duplicates(subset=['created_at'], keep='first')

# Écrire le DataFrame dans un nouveau fichier CSV "resultat.csv"
df.to_csv("resultat.csv", index=False)

# Afficher un résumé statistique de vos données à l'aide de la méthode .describe()
print(df.describe())

# moyenne des temperature par jour
#moy = df
#moy['value'] = moy['value'].astype(float)
#grouped = moy.groupby(moy['created_at'].dt.date)
#df_moy = grouped['value'].mean().reset_index()
#df_moy['created_at'] = pd.to_datetime(df_moy['created_at'])
#df_moy.to_csv("moyenne_par_jour.csv", index=False)



# Vérifier les valeurs manquantes en utilisant la méthode .isna()
missing_values = df.isna().sum()
print("Nombre de valeurs manquantes pour chaque colonne:\n", missing_values)

# suprinmer les colonnes lat, lon et ele
df = df.drop(columns=['lat', 'lon', 'ele'])

# Vérifier à nouveau le nombre de valeurs manquantes
missing_values = df.isna().sum()
print("Nombre de valeurs manquantes pour chaque colonne après suppression:\n", missing_values)

# convertir la colonne temp en float
df['value'] = df['value'].astype(float)

# Groupby par jour
grouped = df.groupby(df['created_at'].dt.date)

# Appliquer la fonction moyenne à la colonne "temp" pour chaque groupe
df_moy = grouped['value'].mean().reset_index()

# Convertir la colonne "created_at" en format de date
df_moy['created_at'] = pd.to_datetime(df_moy['created_at'])

# Lire les données météorologiques externes
meteo_df = pd.read_csv('dataExterne.csv')

# Convertir la colonne "Date" en format de date
meteo_df['Date'] = pd.to_datetime(meteo_df['Date'])

# Combinaison des deux dataframes
merged_df = pd.merge(df_moy, meteo_df, left_on='created_at', right_on='Date')

# suprime Date
merged_df = merged_df.drop(columns=['Date'])

# Calculer la matrice de corrélation
corr = merged_df.corr()

#print("Matrice de corrélation:\n", corr)

#Dans ce cas, la température (variable "value") est fortement corrélée avec la température maximale (variable "Max") et minimale (variable "Min"). La corrélation est plus faible avec le vent (variable "Vent") et les précipitations (variable "Precip").

# enleve les varaibles avec un corr < 0.2
merged_df = merged_df.drop(columns=['Precip'])

# Afficher les données
corr = merged_df.corr()
#print("Matrice de corrélation apres suppression :\n", corr)

# mise ne place du madele de regression
X = merged_df[['Max', 'Min', 'Vent']]
y = merged_df['value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Comparer les prédictions avec les vraies valeurs
for i in range(len(y_pred)):
    print("Valeur prédite: {:.2f}, vraie valeur: {:.2f}".format(y_pred[i], y_test.values[i]))

from sklearn.metrics import mean_squared_error, r2_score

# Obtenir les prédictions sur les données de test
y_pred = model.predict(X_test)

# Calculer le RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE: {:.2f}".format(rmse))

# Calculer le coefficient de détermination (R²)
r2 = r2_score(y_test, y_pred)
print("R²: {:.2f}".format(r2))

# Afficher les prédictions
plt.figure(figsize=(10, 5))
plt.plot(y_test.values, label='Valeurs réelles')
plt.plot(y_pred, label='Valeurs prédites')
plt.legend()
plt.show()