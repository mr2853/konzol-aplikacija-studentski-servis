from glavni_meni import sp
import csv
import json

predmeti=[]

def racunanje_globalne_prosecne_ocene(profesori, studenti, br_prof, br_stud, indeks_stud):

    s_v=0.0
    suma=0.0
    br_ocena=0.0
    for i in studenti[indeks_stud]["ocene"]: # sabiramo sve ocene studenta
        suma+=i["ocena"]
        br_ocena+=1.0 # brojimo broj ocena

    try:
        s_v=suma/br_ocena # i izracunavamo prosecnu ocenu
        print("Vaša prosečna ocena je: ")
        print(s_v,"\n") # obavestavamo studenta o njegovoj prosecnoj oceni

    except ZeroDivisionError:
        print("Trenutno nemate unetih ocena za predmete\n") # u slucaju da student nema unesenih ocena
                                                                            # obavestavamo ga o tome

def polozeni_nepolozeni_ispiti(ocene, profesori, studenti, br_prof, br_stud):
    polozeni_pred=[]
    nepolozeni_pred=[]
    for i in range(12): # ovde proveravamo koji su predmeti polozeni a koji nisu
        try:
            for j in ocene:

                if int(predmeti[i][0])==int(j["sifra_predmeta"]): # ako ih ima ocenama studenta, znaci da je polozen
                    polozeni_pred.append(predmeti[i][1]) # polozen predmet ubacujemo u listu polozeni_pred

            if int(predmeti[i][0]) not in polozeni_pred: # a ako ga nema, znaci da nije polozen
                nepolozeni_pred.append(predmeti[i][1]) # nepolozen predmet ubacujemo u listu nepolozeni_pred

        except ValueError:
            pass
    x=0
    while x==0: # ponavljamo ovaj deo koda sve dok korisnik ne izabere neku od opcija,
        # kada izabere, vrednost promenljive x stavljamo da je 1
        try:
            izaberi=int(input("1.Položeni\n2.Nepoloženi\n"))
            print("\n")
            # ovde pitamo studenta koje predmete zeli da mu se prikazu

            if izaberi==1:
                print("Položeni predmeti: \n")
                # u slucaju da student nema polozene predmete obavestavamo ga ih nema

                if len(polozeni_pred)==0:
                    print("Trenutno nemate položene predmete\n")
                    x=1
                else:
                    for i in polozeni_pred:
                        print(i)
                    print("\n")
                    x=1

            elif izaberi==2:
                print("Nepoloženi predmeti: \n")
                
                if len(nepolozeni_pred)==0: 
                    # u slucaju da student nema nepolozene predmete obavestavamo ga ih nema
                    print("Trenutno nemate nepoložene predmete\n")
                    x=1
                else:
                    for i in nepolozeni_pred:
                        print(i)
                    print("\n")
                    x=1
            else:
                    print("Niste izabrali nijednu od ponuđenih opcija!\n")

        except ValueError:
            print("Niste uneli broj!\n")

def podaci_o_profesoru(profesori, studenti, br_prof, br_stud):

    for i in predmeti: # ovde ispisujemo sve predmete
        print(i[0],i[1])
    print("\n")
    x=0
    while x==0:# ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1
        try:
            # korisnik bira predmet unosenjem njegove sifre
            izbor=int(input("Izaberite predmet unošenjem šifre predmeta: "))
            print("\n")
            x=1

        except ValueError:
            print("Niste uneli broj!\n")

    sifre_prof_stud=[]
    lista_profesora=[]

    # ovde proveravamo koji profesori predaju odabrani predmet
    for i in range(br_stud):
        for j in studenti[i]["ocene"]:
            if int(j["sifra_predmeta"])==izbor:
                sifre_prof_stud.append(j["sifra_profesora"])

    for i in profesori:
        try:
            for j in sifre_prof_stud:

                if int(j)==int(profesori[i][0]):
                    # ovde sastavljamo ime i prezime profesora
                    lista_profesora.append(str(profesori[i][2])+" "+str(profesori[i][3]))

        except ValueError:
            continue

    if not int(len(lista_profesora))==0: # ovde ispisujemo koji profori predaju izabrani predmet
        print("Lista profesora koji predaju izabrani predmet: \n")

        for i in lista_profesora:
            print(i)
            print("\n")

    else:
        # u slucaju da nema profesora koji predaju izabrani predmet obavestavamo studenta o tome
        print("Ni jedan profesor ne predaje izabrani predmet\n")

def studentski_meni(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud):
    
    for i in range(br_stud): # pronalazimo indeks ulogovanog studenta
        if int(korisnicko_ime)==int(studenti[i]["broj indeksa"]):
            indeks_stud=i 

    ocene=studenti[indeks_stud]["ocene"]
    y=0
    while y==0:# ponavljamo ovaj deo koda sve dok korisnik ne izabere neku od opcija,
        # kada izabere, vrednost promenljive y stavljamo da je 1
            x=0
            while x==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1

                try: # ispisujemo meni za studenta
                    izbor=int(input("1.Računanje globalne prosečne ocene\n2.Prikaz položenih ili nepoloženih predmeta po izboru studenata\n3.Prikaz podataka o profesoru koji predaje predmet\n4.Povratak na glavni meni\n"))
                    print("\n")
                    x+=1
                except ValueError:
                    print("Niste uneli broj!\n")

            if izbor==1:
                racunanje_globalne_prosecne_ocene(profesori, studenti, br_prof, br_stud, indeks_stud)

            elif izbor==2:
                polozeni_nepolozeni_ispiti(ocene, profesori, studenti, br_prof, br_stud)

            elif izbor==3:
                podaci_o_profesoru(profesori, studenti, br_prof, br_stud)

            elif izbor==4:
                y=1
                return y

            else:
                print("Niste odabrali nijednu od mogućih opcija!\n")

def trazenje_stud(profesori, studenti, br_prof, br_stud):

    z=0
    while z==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive z stavljamo da je 1
        ime_stud=input("Unesite ime studenta: ")
        print("\n")
        ime_stud=ime_stud.upper()
        imena_studenata=[]
        indeks_stud=[]
        lista_stud=studenti

        for i in range(br_stud): # ovde pronalazimo studenta prema imenu
            if str(lista_stud[i]["ime"]).upper()==ime_stud:
                imena_studenata.append(str(lista_stud[i]["ime"]))
                indeks_stud.append(i)

        if len(imena_studenata)==0:
            print("Nije pronađen nijedan student sa datim imenom\n")
            return "nije nadjen"

        else:
            brojac=0

        for i in imena_studenata: # ovde ispisujemo sve studente sa trazenim imenom
            print(lista_stud[indeks_stud[brojac]]["broj indeksa"], imena_studenata[brojac], lista_stud[indeks_stud[brojac]]["prezime"])
            brojac+=1
        print("\n")

        u=0
        while u==0: # ponavljamo ovaj deo koda sve dok korisnik ne izabere neku od opcija,
        # kada izabere, vrednost promenljive u stavljamo da je 1
            try:
                # od pronadjenih studenata prema imenu, biramo prema broju indeksa kojeg zelimo
                izbor_studenta=int(input("Unesite indeks studenta: "))
                print("\n")
                indeks=0

                for i in range(br_stud):
                    # proveravamo da li je indeks tacno unesen
                    if izbor_studenta==int(studenti[i]["broj indeksa"]):
                        indeks=i
                        u=1

                if u==0:
                    print("Niste tačno uneli indeks\n")
                    continue

                z=1
                return indeks

            except ValueError:
                print("Niste uneli broj!\n")

def dodavanje_ocene_studentu(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud):

    indeks=trazenje_stud(profesori, studenti, br_prof, br_stud) # trazimo studenta uz pomoc funkcije
    if indeks=="nije nadjen":
        return

    brojac=0
    for i in predmeti: # ovde ispisujemo sve predmete

        if brojac==0:
            pass
        else:
            print(predmeti[brojac][0], predmeti[brojac][1])

        brojac+=1

    u=0
    while u==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive u stavljamo da je 1
        try:
            # biramo predmet prema sifri predmeta
            izbor_predmeta=int(input("Izaberite predmet unošenjem šifre predmeta: "))
            u=1

        except ValueError:
            print("Niste uneli broj!\n")

    x=0
    while x==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1
        try:
            # unosimo ocenu predmeta
            ocena=int(input("Unesite ocenu u opsegu(5-10): "))
            print("\n")

            if ocena<5 or ocena>10: # proveravamo da li je u potrebnom opsegu
                print("Ocena nije u datom opsegu!\n")
            else:
                x+=1

        except ValueError:
            print("Niste uneli broj!\n")

    # pamtimo ocenu kao objekat
    konacna_ocena={"sifra_predmeta":izbor_predmeta,"sifra_profesora":korisnicko_ime, "ocena":ocena}
    lista_ocena=list(studenti[indeks]["ocene"])

    # dodajemo listi ocena
    lista_ocena.append(konacna_ocena)
    studenti[indeks]["ocene"]=lista_ocena

    with open("data/studenti.json", "w", encoding='utf-8') as studneti_json:
        json.dump(studenti,studneti_json) # i zapisujemo u json fajl     

def brisanje_ocene(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud):

    indeks=trazenje_stud(profesori, studenti, br_prof, br_stud)
    brojac=0
    brojac_pred=0
    obj_pred={}

    # ovde ispisujemo upisane ocene studenta od ulogovanog profesora
    for i in studenti[indeks]["ocene"]:

        if int(i["sifra_profesora"])==int(korisnicko_ime):
            print(brojac, i["sifra_predmeta"], i["sifra_profesora"])
            obj_pred[brojac]=brojac_pred
            brojac+=1
            brojac_pred+=1

    print("\n")

    if len(obj_pred)==0:
        print("Student trenutno nema upisanih ocena od strane vas\n")
    else:
        x=0
        while x==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1
            try: 
                # ovde profesor prema rednom broju predmeta bira koju ocenu zeli da obrise
                obrisati=int(input("Unesite redni broj predmeta koji želite da obrišete: "))
                print("\n")

                if brojac<obrisati: # u slucaju da je unet broj veci od broja predmeta, ponavljamo proces
                    print("Uneli ste veći broj nego što ima predmeta\n")
                else:
                    x+=1

            except ValueError:
                print("Niste uneli broj!\n")

        for i in range(brojac):
            if i==obrisati:
                br=int(obj_pred[obrisati])
                del studenti[indeks]["ocene"][br] # i ovde brisemo izabranu ocenu za predmet

                with open("data/studenti.json", "w", encoding='utf-8') as studneti_json:
                    json.dump(studenti,studneti_json) # i promene zapisujemo u json fajl  

def prosecna_ocena_za_predmet(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud):

    brojac=0
    s_v=0.00

    for i in range(12):
        if not brojac==0: # ovde ispisujemo sve predmete sa rednim brojem
            print(brojac, predmeti[i][0], predmeti[i][1])
        else:
            print("")
        brojac+=1
    print("\n")

    x=0
    while x==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1
        try: 
            # profesor bira predmet unosenjem rednog broja predmeta
            izbor_pred=int(input("Unesite redni broj predmeta: "))
            print("\n")

            if izbor_pred>brojac: # u slucaju da je unet broj veci od broja predmeta, ponavljamo proces
                print("Uneli ste veći broj nego sto ima predmeta\n")
            else:
                sifra_pred=int(predmeti[izbor_pred][0]) # dobavljamo sifru izabranog predmeta
                brojac=0.00
                suma=0.00
                try:
                    # ovde trazimo u ocenama studenata trazenu sifru predmeta
                    # i sifru profesora koju proveravamo da li se slaze sa sifrom trenutno ulogovanog profesora
                    for i in studenti:
                        for j in i["ocene"]:

                            if int(j["sifra_predmeta"])==sifra_pred and int(j["sifra_profesora"])==int(korisnicko_ime):
                                suma+=int(j["ocena"])
                                brojac+=1
                    s_v=suma/brojac

                    # ovde ispisujemo srednju ocenu za trazeni predmet, od ocena koje je dao ulogovani profesor
                    print("Srednja ocena za izabrani predmet je: ",s_v,"\n")
                    x=1

                except ZeroDivisionError:
                    print("Za izabrani predmet trenutno nema unešenih ocena\n")
                    x=1

        except ValueError:
            print("Niste uneli broj!\n")

def promena_termina_konsultacija(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud):

    indeks_prof=0
    for i in profesori:
        if i==0:
            pass
        else:
            # ovde ispisujemo trenutni termin za konsultacije profesora
            if int(profesori[i][0])==int(korisnicko_ime):
                print(profesori[i][5])
                indeks_prof=i
    print("\n")

    x=0
    while x==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1
        # ovde unosimo novi termin za konsultacije
        novi_termin=input("Unesite novi termin u formatu npr.(sreda, 10-11): ")
        print("\n")
        # ovde sam uzeo najkraci termin se moze zapisati kao npr. sreda,1-2 to je 9 karaktera
        # i prema tome proveravamo duzinu novog termina za konsultacije
        if len(novi_termin)>0 and len(novi_termin)<9:
            print("Vaš novi termin ima ",len(novi_termin)," karaktera, niste pravilno uneli novi termin, ima premalo karaktera\n")
        else:
            x+=1
        # ovde u slucaju da se ne unese novi termin obavestavamo profesora da nije uneo novi termin
        # i vracamo ga na meni za profesora
        if len(novi_termin)==0: 
            print("Niste uneli novi termin\n")
        else:
            r = csv.reader(open('data/profesori.csv', encoding='utf-8'), delimiter="-") # ovde dobavljamo fajl profesori
            lines = list(r)
            lines[indeks_prof][5]=novi_termin

            with open('data/profesori.csv', 'a', newline='', encoding='utf-8') as csv_file: # ovde zapisujemo u njega novi termin
                writer = csv.writer(csv_file, delimiter ="-",quoting=csv.QUOTE_MINIMAL)

                with open('data/profesori.csv', 'w', encoding='utf-8') as csv_dodatno:
                    ispisi=csv.writer(csv_dodatno)
                    ispisi.writerows("")

                writer.writerows(lines)

def profesorski_meni(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud):

    y=0
    while y==0: # ponavljamo ovaj deo koda sve dok korisnik ne izabere neku od opcija,
        # kada izabere, vrednost promenljive y stavljamo da je 1
        x=0
        while x==0: # ponavljamo ovaj deo koda sve dok korisnik tacno ne unese ono sto mu se trazi,
        # kada tacno unese, vrednost promenljive x stavljamo da je 1

            try:
                izbor=int(input("1.Dodavanje ocene studentu\n2.Brisanje ocene studentu\n3.Računanje prosečne ocene za predmet\n4.Promena termina konsultacija\n5.Povratak na glavni meni\n"))
                print("\n")
                x+=1
            except ValueError:
                print("Niste uneli broj!\n")
            
        if izbor==1:
            dodavanje_ocene_studentu(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud)

        elif izbor==2:
            brisanje_ocene(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud)

        elif izbor==3:
            prosecna_ocena_za_predmet(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud)

        elif izbor==4:
            promena_termina_konsultacija(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud)

        elif izbor==5:
            y=1
            return y

        else:
            print("Niste odabrali nijednu od mogućih opcija!\n")
                    

def meni(korisnicko_ime,lozinka, tip):
    
    lista=sp()
    profesori=lista[0]
    studenti=lista[1]
    br_prof=int(lista[2])
    br_stud=int(lista[3])
    stop=0
    while stop==0: # ponavljamo ovaj deo koda sve dok korisnik ne izabere opciju da izadje,
        # kada je izabere, vrednost promenljive stop je 1
        br_pred=0

        with open('data/predmeti.csv', newline='', encoding="utf-8") as csvfile: # dobavljamo tekst iz fajla
                        fajl = csv.reader(csvfile, quotechar='|')

                        for i in fajl:
                            predmeti.append(i)
                            br_pred+=1 # brojimo koliko ima predmeta

        if tip=="student": # ako je tip ulogovanog korisnika student, prikazujemo meni za studenta
            stop=int(studentski_meni(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud))

        elif tip=="profesor": # ako je tip ulogovanog korisnika profesor, prikazujemo meni za profesor
            stop=int(profesorski_meni(korisnicko_ime,lozinka, tip, profesori, studenti, br_prof, br_stud))
            
        else:
            print("Morate biti ulogovani da bi pristupili meniju\n")