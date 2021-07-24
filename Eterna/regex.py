import re 


regex = re.compile("[0-9]+\.[0-9]+")

resultat = regex.findall("pi vaut 3.14 et  vaut 2.72")

print(resultat)