import json
import csv

def sp():
    """
    Funkcija sp() skraceno od studenti profesori, koristimo je za
    dobavljanje fajlova i podataka iz fajlova profesori.csv i studenti.json
    """
    profesori={}
    br_prof=0
    br_stud=0

    sfile=open('data/studenti.json','r', encoding="utf-8")
    sfilej=sfile.read()
    studenti=json.loads(sfilej) # ovde pamtimo u student json objekat

    for i in studenti: # ovde brojimo koliko ima studenata
        br_stud+=1

    with open('data/profesori.csv', newline='', encoding="utf-8") as csvfile:
        writer = csv.reader(csvfile, delimiter ="-",quoting=csv.QUOTE_MINIMAL)

        for i in writer:
            profesori[br_prof]=i # ovde pamtimo profesore u objektu
            br_prof+=1 # ovde brojimo koliko ima profesora

    return [profesori,studenti,br_prof, br_stud] # kao rezultat funkcije vracamo listu

lista=sp()
profesori=lista[0]
studenti=lista[1]
br_prof=int(lista[2])
br_stud=int(lista[3])

def registracija_profesora(profesori, studenti, br_prof, br_stud):
    x=0
    while x==0:
        try:
            l=0
            sifra=int(input("Unesite šifru profesora: "))
            for i in profesori:
                if not int(i)==0:
                    if int(profesori[i][0])==sifra:
                        print("Vec postoji korisnik sa datom šifrom\n")
                        l=1
            for i in studenti:
                if int(i["broj indeksa"])==sifra:
                    print("Već postoji korisnik sa datom šifrom\n")
                    l=1
            if l==0:
                x=1
        except ValueError:
            print("Niste uneli broj\n")

    lozinka=input("Unesite lozinku profesora: ")
    ime=input("Unesite ime profesora: ")
    prezime=input("Unesite prezime profesora: ")
    email=input("Unesite email profesora: ")
    j=0
    termin=""
    while j==0:
        termin=input("Unesite novi termin u formatu npr.(sreda, 10-11): ")
        if len(termin)<9:
            print("Vaš novi termin ima ",len(termin)," karaktera, niste pravilno uneli novi termin, ima premalo karaktera\n")
        else:
            j=1
            print("\n")
        
    with open('data/profesori.csv', 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter ="-",quoting=csv.QUOTE_MINIMAL)
        writer.writerow([sifra, lozinka, ime, prezime, email, termin])
    return 1

def registracija_studenta(profesori, studenti, br_prof, br_stud):
    x=0
    while x==0:
        try:
            l=0
            br_indeksa=int(input("Unesite broj indeksa: "))
            for i in studenti:
                if int(i["broj indeksa"])==br_indeksa:
                    print("Već postoji korisnik sa datim indeksom\n")
                    l=1
            for i in profesori:
                if not i==0:
                    if int(profesori[i][0])==br_indeksa:
                        print("Već postoji korisnik sa datim indeksom\n")
                        l=1
            if l==0:
                x=1
        except ValueError:
            print("Niste uneli broj\n")
                    
    lozinka=input("Unesite lozinku: ")
    ime=input("Unesite ime: ")
    prezime=input("Unesite prezime: ")
    email=input("Unesite email: ")
    print("\n")

    studenti.append({"broj indeksa":br_indeksa, "lozinka":lozinka, "ime":ime, "prezime":prezime, "email":email, "ocene":[]})
    
    with open("data/studenti.json", "w", encoding='utf-8') as studneti_json:
        json.dump(studenti,studneti_json)

    return 1

def registracija(profesori, studenti, br_prof, br_stud):
    rs=0
    while rs==0:
        x=0
        while x==0:
            try:
                izbor=int(input("1.Profesora\n2.Studenta\n"))
                x=1
            except ValueError:
                print("Niste uneli broj\n")

        if izbor==1:
            rez=registracija_profesora(profesori, studenti, br_prof, br_stud)
            if rez==1:
                br_prof+=1
                rs=1

        elif izbor==2:
            rez=registracija_studenta(profesori, studenti, br_prof, br_stud)
            if rez==1:
                rs=1
                br_prof+=1
                
        else:
            print("Izabrali ste nepostojeću opciju\n")

def prijava_na_sistem(profesori, studenti, br_prof, br_stud):
    j=0
    nadjen=0
    while j==0:
        try:
            korisnicko_ime=int(input("Unesite korisničko ime: "))
            j=1
            lozinka=input("Unesite lozinku: ")
            print("\n")

            for i in range(br_prof): # proveravamo da li korisnicko ime i lozinka postoji kod profesora
                try:
                    if int(profesori[i][0])==int(korisnicko_ime) and str(profesori[i][1])==lozinka:
                        tip="profesor"
                        print("Dobrodošli profesore\n")
                        x=1
                        nadjen=1
                        rezultat=[korisnicko_ime,lozinka, tip]
                        return rezultat # i kao rezultat vracamo listu

                except ValueError:
                    pass

            for i in range(br_stud): # proveravamo da li korisnicko ime i lozinka postoji kod studenata
                try:
                    if int(studenti[i]["broj indeksa"])==int(korisnicko_ime) and str(studenti[i]["lozinka"])==lozinka:
                        tip="student"
                        print("Dobrodošli studente\n")
                        x=1
                        nadjen=1
                        rezultat=[korisnicko_ime,lozinka, tip]
                        return rezultat # i kao rezultat vracamo listu

                except ValueError:
                    pass

            if nadjen==0: # u slucaju da korisnik nije nadjem obavestavamo ga da nije registrovan u sistemu
                print("Niste registrovani u sistemu\n")
                izadji=2
                return izadji

        except ValueError:
            print("Uneli ste slovo, a treba samo brojevi!\n")

def glavni_meni(): # glavni meni
        x=0
        while x==0:
            try:
                lista=sp()
                profesori=lista[0]
                studenti=lista[1]
                br_prof=int(lista[2])
                br_stud=int(lista[3])

                izbor=int(input("1.Prijava na sistem\n2.Registracija\n3.Izlazak iz aplikacije\n"))
                print("\n")

                if izbor==1:
                    rez=prijava_na_sistem(profesori, studenti, br_prof, br_stud)
                    if not rez==2:
                        return rez

                elif izbor==2:
                    registracija(profesori, studenti, br_prof, br_stud)

                elif izbor==3:
                    print("Pozdrav\n")
                    x=1
                    izadji=1
                    return izadji

                else:
                    print("Izabrali ste nepostojeću opciju\n")
                    
            except ValueError:
                print("Niste uneli broj\n")
        