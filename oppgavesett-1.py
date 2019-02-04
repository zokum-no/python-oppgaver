#import numpy
#import string
import math


# Her er et par metoder, klarer du å finne feilene?
# Når du har funnet feilen(e), kan du rette opp i dem?

# Det er kjekt om du reflekterer litt over hva som gikk galt og hvorfor det gikk galt!

#menysystem

def Meny (menyTekst, maksValg) :

    print("Copywritten Nils Olav Olsbukk Bøe, 2019")
    print("******** Haxxorsoft industries ********")
    print(menyTekst)
    print("***************************************")
    print("0 - Avslutt programmet!\n")
    while (True) :
        valg = int(input("Velg et tall fra 0 til %s: " % maksValg))
        if valg >= 0 and valg <= maksValg :
            return valg
    

# Oppgave 1: Sjekk passordlengden er 8!
# I denne bedriften har man krav om at passordlengden skal være på 8 tegn. Firmaets nye superkoder
# rett fra videregående, Nils Ole Olsbukk Bøe har derfor implementert denne rutina til å sjekke at
# passordene som skal beskytte pasientjournal, nettbankdetaljer og wow-login er gode nok.
# Passordhashinga som brukes er et blokkalgoritme som jobber på 8 og 8 bytes.
# Nils Olav har derfor oppgradert den gamle som hadde _10_ sjekker for om passordet var 8, 16, 24, 32
# osv til en som støtter alle mulig passordlengder

def Passordlengde () :
    dittPass = input("Passord på 8 tegn: ")

    # Lur måte å sjekke på, kjemperask!
    # Del på 8 og sjekk at det ikke er noe til overs!
    if ((len(dittPass) % 8) == 0) :
        print("Passordet ditt er på 8 tegn, og sikkert nok!")
    else :
        print("Passordet ditt er ikke bra nok, må være på _8_ tegn din fjott!")
        Passordlengde()

# Oppgave 2: Programmet konverterer tall til tekst'
# Nils Ole har fått som jobb i å gjøre dataprogrammene litt mer brukervennlige og har derfor bestemt
# seg for at alle tall skal konverteres til tekst. Dvs at det skal stå hundre-og-fem i stedet for 105.
# Det viser seg at programmet har noen småfeil som de oppdager når sjefen plutselig bruker den nye
# versjonen i produksjon når han har besøk av statsministeren. Hva gikk galt?

def TallSkriv(tall) :
    if tall == 1:
        print("en", end ="")
    elif tall == 2:
        print("to", end ="")
    elif tall == 4 :
        print("fire", end ="")
    elif tall == 5 :
        print("fem", end ="")
    elif tall == 6 :
        print("6", end ="")
    elif tall == 7 :
        print("sju", end ="")
    elif tall == 8 :
        print("aatte", end ="")
    elif (tall == 9) :
        print("ni", end ="")
    else :
        print("tre", end ="")

def TallTilTekst () :
    # Int gjør om til int, ellers feil
    innTall = int(input("Et tall takk: "))

    # Denne løkken går helt til inntall er 0, eller kanskje ikke om det er tall igjen og vi returnerer
    # et annet sted pga optimalisering
    while(innTall > 0) :

        if (innTall > 100) : # Viktig
            haxx = math.floor(innTall / 100)
            innTall -= 100 * haxx
            TallSkriv(haxx) # Kaller tallskriv med rett verdi
            print("-hundre", end ="")
        elif (innTall > 1000) :
            # samme som hundre, bare at vi skriver tusen!
            print("-tusen")
    
        # Her er den slutt vi håpet på!
        elif (innTall < 10) :
            TallSkriv(innTall)
            return

        print("-og-", end ="")
        
    print(" var tallet, pent hva!!\n")



# Selve programmet, kaller bare menyssystemet

oppgave = 1337

while (oppgave != 0) :
    oppgave = Meny("1 - Sjekk av passordlengde\n2 - Tall til tekst testrom (test suite)", 2)
    if oppgave == 1 :
        Passordlengde()
    elif oppgave == 2 :
        TallTilTekst() 
    

