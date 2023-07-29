# debut Modele de prediction de temperature dans une maison

# Description

Calcul de prédiction de température dans une maison. La température est récupérée grâce à un capteur de température connecté à Adafruit. Ensuite, elle est récupérée sous le format CSV pour pouvoir être traitée par le modèle.

# installation 

necessite des librairie pandas, glob, numpy, matplotlib, sklearn
apres avoir installer tout c'est librairie il faut un fichier

# utilisation 

pour utiliser le modele il faut un jeu de donne sous le format csv
sous cette forme : 
```csv
id,value,feed_id,created_at,lat,lon,ele
id-adafruit,19.20,feed_id_adafruit,2000-10-10 00:00:00 UTC,lat,lon,ele
```

ensuite vous pouvez executer le fichier modele.py
