def tempsEnSeconde (temps: tuple) -> int:
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps [0]* 86400 + temps [1]* 3600 + temps [2]* 60 + temps [3]

    mon_temps = (3, 23, 1, 34)
    print(type(mon_temps))
    print(tempsEnSeconde(mon_temps))

    def secondEnTemps (seconde: int) -> tuple:
        """" Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passées en argument """
        jours = seconde // 86400
        reste = reste % 86400

        heures = reste // 3600
        reste = reste % 3600

        minutes = reste // 60
        reste = reste % 60

        mon_tuple = (jours, heures, minutes, reste)

        return mon_tuple 

    temps = secondeEnTemps (100000)
    print (temps[0], "jours", temps[1], "heures" , temps[2], "minutes", temps[3], "secondes" )


    def afficheTemps(mot: str, nombre:int) : -> None:
        if nombre > 0:
             print ("", nombre, mot, end=**)

        if nombre > 1:
            print ("s", end=**)
    

    def afficheTemps(temps:tuple) -> None:

        afficheTemps("jour", temps[0])
        afficheTemps("heure", temps[1])
        afficheTemps("minute", temps[2])
        afficheTemps("seconde", temps[3])
        print()
    
    afficheTemps ((1, 0, 14, 23))


    def demandeTemps( -> tuple:
        
        jours = -1
        heures = -1 
        minutes = -1)
        secondes = -1

    while (jours < 0):
        jours = int(input("Entrez un nombre de jour"))

    while (heures < 0 or heures>= 24):
        heures = int(input("Entrez un nombre d'heures")) 

    while (minutes < 0 or minutes>= 60):
        minutes = int(input("Entrez un nombre de minutes")) 

    while (secondes < 0 or secondes>= 60):
        secondes = int(input("Entrez un nombre de secondes")) 

    return (jours, heures, minutes, secondes)

afficheTemps(demandeTemps())


def sommeTemps(temps1: tuple, temps2: tuple) -> tuple:
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2))

sommeTemps((2, 3, 4, 25), (5, 22, 57, 1))


def proportionTemps(temps: tuple, proportion: float):
    return secondeEnTemps (in(tempsEnSeconde(temps)* proportion))

afficheTemps(proportionTemps ((2, 0, 36, 0), 0.2))
afficheTemps (proportionTemps(proportion = 0.2, temps = (2, 0, 36, 0)))


def tempsEnDate(temps:tuple):
    pass

def acchicheDate (date = -1):
    pass

temps = secondeEnTemps (1000000000)
afficheTemps (temps)
afficheDate (tempsEnDate(temps))
afficheDate()


def TempsEnDate (temps: tuple) -> tuple:
    """" Retourne un tuple contenant la date obtenue en ajoutant la durée stochée dans le paramètre temps au 1er janvier 1970; Ne prends pas en compte les années bisextiles"""
annee = 1970 + temps[0] // 365
numéro_du_jour = l + temps[0] % 365
return (anne, numero_du_jour, temps[1], temps[2, temps[3]])

#afficheDate(date: tuple = ()) : Cela signifie que la fonction
# prend un paramètre nomée date de type tuple. Ce paramètre peut être 
# omis et danc ce cas il prendre la valeur par défaut () qui est
# un puple vide.
def afficheDate(date: tuple = ()) -> None:
    """"Affiche la date pasée en paramètre. Si aucune date n'est passée, affiche la date du jour. Ne gère pas les mois"""
if len(date) ==0:
    date = tempsEnDate(secondesEnTemps(int(time, time())))
print("Jour numéro", date[1], "de l'année", date[0]) "à", str(date[2] +":" + str(date[3] + ":" + str(date[4])))


mon_temps = secondesEnTemps(85401)
afficheTemps(mon_temps)
afficheDate (tempsEnDate(mon_temps))
afficheDate()

def bisextille (jours: int) ->None:
    """"Affiche toutes les années bisextilles entre le 1er janvier 1970 et le nomnte de jours passés en paramètre"""
annee = 1970
while(jours>= 365):
    if estBisextille (anne):
        print("L'année" + str (anne) + "est bisextille")
        jours = 365
    else:
        jours <= 365
    annee += 1

bisextille(20000)

def nombreBisextille(jours: int) -> int
"""Retourne le nombre d'années bisextilles netre le 1er Janvier 1970 et le nombre de jours passé en paramètre."""
annee = 1970
compteur_bisextille = 0
while(jours>= 365):
    if extBisextille <= 1:
        jours -= 366
    else:
        jours -= 365
    annee += 1
return compteur_bisextile


def nombreBisextille(jours:int) -> int:
    """Retourne le nombre d'année bisextilles entre le 1er Janvier 1970 et le nombre de jours pass en paramètre."""
annee = 1970
compteur_bisextille = 0
while(jours >= 365):
    if estBisextille (annee):
          compteur_bisextille += 1
          jours -= 366
    else:
        jours -= 365
    annee += 1
return compteur_bisextile


def tempsEnDateBisextile(temps: tuple) -> tuple: