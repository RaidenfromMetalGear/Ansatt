#skrevet av Arne fra KVN, 2IT

#json = poop
import os
import time
import json

#selve listen ikke glem det
#r = Read
with open("data.json", "r") as f:
    ansattliste = json.load(f)

#main
def main():
    #loop
    mn = True
    while mn:
        print("Velkommen til arnes meny!")
        valg = input("1. for legg til ansatt, 2. slett ansatt, 3. rediger ansatt, 4. print ut ansatt, 5. Avslutt: ")

    #valg
        if valg == "1":
            leggtilansatt()
        
        elif valg == "2":
            slettansatt()

        elif valg == "3":
            redigeransatt()
        
        elif valg == "4":
            printansatte()
        
        elif valg == "5":
            mn = False
            
            #lagre data
            #w står for write.
            with open("data.json", "w") as f:
                json.dump(ansattliste, f)

#ansatt.
def leggtilansatt():
    print("Legg til ansatt valgt.")
    leggansatt = input("Skriv fornavn på ansatt du vil legge til: ").upper()
    leggansatt2 = input("Skriv etternavn på ansatt du vil legge til: ").upper()
    print("er" , leggansatt, leggansatt2, "riktig?")
    #TypeError: input expected at most 1 argument, got 3, derfor seperat print og var.
    ja = input("Y/N: ")
    #det blir enklere sånn
    ja.lower()

    #join
    navn = leggansatt + leggansatt2
    print(navn)

    #y yes
    if ja in ["y", "Y", "yes", "YES"]:
        stilling = input("hva er stillingen til ansatt?: ")
        avdeling = input("hvilken avdeling jobber ansatt i?: ")

        #legg til i dict med navn som key
        #enkelt og simpelt.
        ansattliste[navn] = [leggansatt, leggansatt2, stilling, avdeling]
        print("Ferdig.")
        print("")

    elif ja in ["n", "N", "no", "NO"]:
        print("Ok.")
        print("")
        leggtilansatt()
    else:
        print("Feil input, vennligst prøv på nytt..")
        print("if this is a bug please contact arne.")
        print("")
        leggtilansatt()

#print ut 
def printansatte():
    print(ansattliste)
    #antall 
    print(len(ansattliste))

#slett
def slettansatt():
    fornavn = input("skriv inn Fornavn på ansatt du vil slette: ").upper()
    etternavn = input("skriv in etternavn på ansatt: ").upper()

    navn2 = fornavn + etternavn

    print("Er", navn2 , "riktig?")
    valg = input("Y/N: ")

    
    if valg in ["y", "Y", "yes", "YES"]:
        print("Ok, sjekker database om ansatte fins.")
        #vet ikke helt hvorfor jeg la til sleep? sikkert fordi det er kult
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        #sjekk om i dict
        if navn2 in ansattliste:
            print("Fant ansatt, sletter nå.")
            #slett
            del ansattliste[navn2]
            print("")
            main()
        #fant ikke
        else:
            print("fant ikke ansatt.")
            print("")
            main()

    elif valg in ["n", "N", "no", "NO"]:
        print("Ok.")
        print("")
        leggtilansatt()
    else:
        print("Feil input, vennligst prøv på nytt..")
        print("if this is a bug please contact arne.")
        print("")
        leggtilansatt()

#rediger ansatt.
#redigerer listen i dict men redigerer ikke selve key.
#par problemer med det, hvis man vil redigere key må man slette keyen, og da blir selve ansatt slettet
#eller så lages det en helt ny key med ny liste og sånt
#kanskje finne ut hvordan få pos i list? (altså [X] X= pos i dict.)
#https://stackoverflow.com/questions/44390818/how-to-insert-key-value-pair-into-dictionary-at-a-specified-position
#skal prøve det jeg fant
#okei problemer, det ser ut som at den ene syntaxen jeg trenger .keys ikke fungerer på ansattliste fordi jeg har importert den ifra json.

def redigeransatt():
    fornavn = input("skriv inn Fornavn på ansatt du vil redigere: ").upper()
    etternavn = input("skriv in etternavn på ansatt: ").upper()
    navn2 = fornavn + etternavn

    print("Er", navn2 , "riktig?")
    valg = input("Y/N: ")

    #standard
    if valg in ["y", "Y", "yes", "YES"]:
        print("Ok, sjekker database om ansatte fins.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        if navn2 in ansattliste:
            print("Fant ansatt.")
            print("Advarsel: Hvis du redigerer blir tidligere info slettet.")
            print("vil du fortsette?")
            valg2 = input("Y/N: ")
            
            if valg2 in ["y", "Y", "yes", "YES"]:
                print("Redigering begynt.")
                stilling = input("hva er stillingen til ansatt?: ")
                avdeling = input("hvilken avdeling jobber ansatt i?: ")
                print("vil du redigere navn?")
                valg3 = input("Y/N: ")

                if valg3 in ["y", "Y", "yes", "YES"]:
                    fornavn = input("skriv inn Fornavn på ansatt du vil redigere: ").upper()
                    etternavn = input("skriv in etternavn på ansatt: ").upper()
                    #samme som å legge til ansatt, bare at vi forandrer ikke keyen sånn at det "redigerer" bare lista.
                    ansattliste[navn2] = [fornavn, etternavn, stilling, avdeling]
                    print("Redigering fullført.")
                    print("")
                
                elif valg3 in ["n", "N", "no", "NO"]:
                    ansattliste[navn2] = [fornavn, etternavn, stilling, avdeling]
                    print("Redigering fullført.")
                    print("")

            elif valg2 in ["n", "N", "no", "NO"]:
                print("Returnerer til meny.")
                print("")
                main()

        else:
            print("fant ikke ansatt.")
            print("")
            main()

    elif valg in ["n", "N", "no", "NO"]:
        print("Ok.")
        print("")
        main()
    else:
        print("Feil input, vennligst prøv på nytt..")
        print("if this is a bug please contact arne.")
        print("")
        main()


#kall på main.
main()

#muligens gjøre om til .exe?