#import numpy
#import string
import math
import random

#######################################################################################################
# Menysystemet er samme som i forrige oppgave, ingenting nytt her, scroll ned til stor kommentarblokk #
# for selve oppgaven!                                                                                 #
#######################################################################################################

def Meny (menyTekst, maksValg) :

    print("Copywritten Leif Egil Eidsvang Tønnesen, 2019")
    print("*********** Haxxorsoft industries ***********")
    print(menyTekst)
    print("*********************************************")
    print("0 - Avslutt programmet!\n")
    while (True) :
        valg = int(input("Velg et tall fra 0 til %s: " % maksValg))
        if valg >= 0 and valg <= maksValg :
            return valg
def PrintRiktigTall (a, hemme1ig) :
    print("Riktig tall var: '%d'!" % hemme1ig)
    
###############################################################################
# Oppgave 1: Gjett tallet på 5 forsøk eller mindre!
#
# Dette programmet er skrevet av Leif Egil Eidsvang Tønnesen. Han jobber hos
# Haxxorsoft Industries og er en av senior-programmererne. Leif Egil er en
# notorisk gambler og har spilt bort hus, gård, kone, bærbar pc og selvtilliten.
# Han bor nå i en container utenfor arbeidsplassen.
#
# Målet med dette programmet er å gamble litt med de andre ansatte. Om han
# vinner nok veddemål med dette så vil han ha råd til lett bedre mat. Han er
# nemlig veldig lei av måke og selvfiska bryggestinter.
#
# Tør du som ung programmerer å spille spillet til Leif Egil i håp om å vinne
# pengene?
#
# Reglene er enkle. Du får 5 forsøk og du må minst _1_ gang i løpet av 20 runder
# komme frem til det riktige tallet. Siden det er 100 tall og du har totalt sett
# 5 * 20 forsøk burde du jo få rett ca en gang hevder Leif Egil.
#
# Det koster 100 kroner å spille, og vinner du, så vinner du 200 kroner! Dvs at
# du går 100 kroner i pluss når du vinner og 100 i minus når du taper.
#
# Du har fått tak i kildekoden, og kan selv evaluere om dette er lurt å gjøre
# eller ei. Siden man i snitt får rett tall en gang per 100 kroner og vinner
# 200 så ser jo dette forlokkende ut, men har gambleren Leif Egil noe opp i ermet?
#
# NB: Programmet foretar ikke noen sjekk at du skriver inn tall, se bort i fra
# denslags tekniske småting.
#
# Send meg en epost med svarene, kimroarhauge hos gmail, har telefonvarsling på
# den adressa.
#
# Oppgavene er som følger:
# 1. Stemmer denne antagelsen om hvor ofte man vinner? Kan man slå "huset" her?
# 2. Spill 20 runder med spillet, hvor ofte vant du?
# 3. Evaluer programmet og sjekk at det gjør det som det hevdes, på riktig måte.
# 4. Hvorfor er det lurt å evaluere kode fra kilder som i utgangspunktet jobber
#    i lag med deg?

def GjettTall () :

    print("Her skal du gjette et tilfeldig tall fra 1 til og med 99.")
    print("Du har kun fem forsøk på å gjette rett!")
    print("Du får vite om det er for høyt eller for lavt!")

    u = 100 # øvre grense (upper)
    l = 1 # nedre grense (lower)
    
    hemmelig = random.randint(l, u) # et tilfeldig tall
    gjetting = -1 # vi begynner med denne verdien slik at løkka kjører
    forsok = 0
    maksForsok = 5

    while (gjetting != hemmelig and maksForsok > forsok) : 
        # Endret til g fra gjetting fordi det ellers blir så lange uttrykk!
        g = int(input("Gjett tallet"))

        # Litt logikk for å si fra om du gjettet for høyt eller lavt
        gjettetHoyt = u - g
        gjettetLavt = g - l

        # Det kan hende personen gjetter lavere selv om spilleren gjettet for lavt,
        # da er man garantert å tape!
     
        if (gjettetHoyt > gjettetLavt) :
            # Sjekk om noen gjetter lavere enn tidligere som var alt for lav
            if (g < l) :
                print("Du gjetter jo enda lavere!")
            l = g
            print("Du gjettet for lavt, dessverre!")
        else :
            if (u < g) :
                print("Du gjetter jo enda høyere!")
            u = g
            print("Du gjettet for høyt, dessverre!")
        
        forsok += 1

    # Siden forsøkene ikke er brukt opp, så må svaret være rett!
    if (forsok < maksForsok):
        print("Gratulerer, du vant 300 kroner!")
    else :
        print("Det gikk ikke så bra, du skylder meg 100 kroner din lømmel!")
    # Sender med hemmelig for å vise det hemmelige tallet!
    PrintRiktigTall(hemmelig, random.randint(l, u))

# Selve programmet, kaller bare menyssystemet

oppgave = 1337

while (oppgave != 0) :
    oppgave = Meny("1 - Lett-tjente penger, gjett tall!", 1)
    if oppgave == 1 :
        GjettTall()
    elif oppgave == 2 :
        GjettTall() 
    

