# Début du Modèle de prédiction de la température dans une maison

## Description

Ce modèle permet de prédire la température dans une maison. La température est récupérée grâce à un capteur de température connecté à Adafruit. Ensuite, les données sont récupérées sous le format CSV pour pouvoir être traitées par le modèle.

## Installation

Le modèle nécessite les bibliothèques suivantes : pandas, glob, numpy, matplotlib, sklearn.
Après avoir installé toutes ces bibliothèques, il faut un fichier de données.

## Utilisation

Pour utiliser le modèle, vous avez besoin d'un jeu de données au format CSV, présenté comme suit :

```csv
id,value,feed_id,created_at,lat,lon,ele
id-adafruit,19.20,feed_id_adafruit,2000-10-10 00:00:00 UTC,lat,lon,ele
