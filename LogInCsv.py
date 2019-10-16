import csv

def getId():
    i = 0
    with open("images/log.csv", "r") as read:
        reader = csv.reader(read)
        i = i + 1

    return i
def add(file):
    #   parsing of the name of the file
    nom = file[7:24]

    jour = nom[0:2]
    mois = nom[3: 5]
    annee = nom[6: 10]
    heure = nom[10: 12]
    minutes = nom[12: 14]
    secondes = nom[14: 16]

    temps = jour + "/" + mois + "/" + annee + "||" + heure + "::" + minutes + "::" + secondes
    row = [getId(),temps]
    with open('images/log.csv', "a") as add:
        writer = csv.writer(add)
        writer.writerow(row)
