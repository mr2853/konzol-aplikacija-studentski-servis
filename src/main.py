from glavni_meni import glavni_meni, sp
from meni import meni
import csv
import json
korisnicko_ime=" "
lozinka=" "
tip=" "
izadji=0
while izadji==0 or izadji==2: # izadji je 0 na pocetku, ako korisnik nije pronadjen (izadji je 2) 
    # pa se ponavlja postupak glavnog menija dok se korisnik ne prijavi ili registruje ili izadje
    x=0
    while x==0:
        lista=sp()
        profesori=lista[0]
        studenti=lista[1]
        br_prof=int(lista[2])
        br_stud=int(lista[3])

        rezultat=glavni_meni()
        if type(rezultat)==int:

            if rezultat==2:
                izadji=2

            elif rezultat==1:
                izadji=1 
                x=1
        else:
            x=1
            izadji=0

    if izadji==0:
        indeks_stud=0
        suma=0.0
        s_v=0.0
        br_ocena=0.0
        br_pred=0

        predmeti=[]
        polozeni_pred=[]
        nepolozeni_pred=[]

        korisnicko_ime=int(rezultat[0])
        lozinka=str(rezultat[1])
        tip=str(rezultat[2])
        meni(korisnicko_ime,lozinka, tip) # ovde pozivamo funkciju meni sa 3 parametara
        # prema parametru tip, odredjuje se da li ce se prikazati meni za studenta ili profesora