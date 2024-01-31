import os
import time
import random
os.system('color 2')
print("Mi a neved felfedező?")
nev=input()
if nev=="Napóleon":
    print("There is nothing we can do")
elif nev=="Freddy" or nev=="Freddy Fazbear":
    print("Har Har ha har har har ha har ha har...")
else:
    print(str(nev)+"? Szép neved van")
time.sleep(2)
os.system('cls')
print("Körbe nézel és találkozol egy öreg bácsikával")
os.system('color 3')
print("Szia a nevem Lajos.")
print("[Lajos] Egy öreg régész vagyok aki a segítséged kéri")
print("[Lajos] A feladatod nem lesz egyszerű. Meg kell találnod Atlantist az elveszett várost.")
print("        De persze ez senkinek sem sikerült még, ettől olyan nehéz a feladat. Csak találgatni")
print("        tudunk hogy hol van Atlantis. Felfedezőink találtak egy térképet ami elvezet Atlantisba.")
print("        Az Atlanti-óceán partján fogsz kezdeni és onnan kell kihajóznod a térkép és az írásos források alapján.")
print("        A feladatod nem lesz egyszerű ezért jól válaszd meg a képességeidet.Csak a legokosabb,")
print("        legravaszabb, legerősebb képes megtalálni Atlantist.")
print("")
print("Nyomj entert a folytatáshoz!")
hngzjm=input()
os.system('cls')
print("Akkor ismertesd képességeid!")
élet=0
while 0==élet:
    print("Add meg az életerőd számát 1 és 20 között")
    élet=int(input())
    if élet>20:
        print("Nana nem csalunk!")
        élet=0
    elif élet<1:
        print("Nem lehetsz halott már most!")
        élet=0
iq=0
while 0==iq:
    print("Add meg az intelligencia szinted 1 és 20 között")
    iq=int(input())
    if iq>20:
        print("Ilyen okos nem lehetsz!")
        iq=0
    elif iq<1:
        print("Enyire nem lehetsz buta!")
        iq=0
erő=0
while 0==erő:
    print("Add meg a fizika erőd 1 és 20 között")
    erő=int(input())
    if erő>20:
        print("Nem lehetsz ennyire kipattintva!")
        erő=0
    elif erő<1:
        print("Ez ide kevés lesz!")
        erő=0
reflex=0
while 0==reflex:
    print("Add meg a reflexeid gyorsaságát 1 és 20 között")
    reflex=int(input())
    if reflex>20:
        print("Neonak sincsenek ilyen reflexei!")
        reflex=0
    elif reflex<1:
        print("Ezt a küldetést egy lajhár nem élné túl")
        reflex=0
luck=0
print("Add meg a szerencséd számát 1 és 20 között")
luck=int(input())
print("Azt hitted a szerencsédet befolyásolhatod?")
luck=random.randrange(1,21)
time.sleep(3)
os.system('cls')
print("Akkor a statisztikáid:-életerő:"+str(élet))
print("                      -intelligenciád:"+str(iq))
print("                      -fizikai erőd:"+str(erő))
print("                      -reflexeid:"+str(reflex))
print("                      -szerencséd:"+str(luck))
time.sleep(4)
os.system('cls')
print("Megérkeztél az Atlanti-óceán partjára.")
os.system('color 2')
time.sleep(5)
os.system('cls')
print("[Lajos]Innentől egyedül kell folytatnod utadat. Ha vissza térnél én itt leszek.A saját érdekedben mondom legyél körültekintő.")
print("")
print("Nyomj entert a folytatáshoz!")
os.system('color 3')
hngzjm=input()
os.system('color 2')
os.system('cls')
print("A parton állsz mit teszel?")
print("körbenéz")
k=0
nez=input()
os.system('cls')
if nez=="lelépek":
    print("Hova mész ezt nem lenne szabad!")
    print("Szimuláció leállítása...")
    print("[Háttérben]Hozd a következőt ez nem akarja megpróbálni!")
    os.system('color 6')
    time.sleep(3)
    os.system('cls')
    exit()
if nez=="körbenéz":
    print("Megtaláltad a hajót amivel kihajózhatsz és még két utat.")
    k=1
os.system('color 2')
o2=0
map=0
while k!=0:
    print("Mit teszel?")
    print("(A zárójelben lévő szavak különböző lehetőségeket jelölnek)")
    print("(Jobbra megyek/Balra megyek/Kihajózok)")
    megy=input()
    if megy=="Balra megyek" or megy=="balra megyek":
        os.system('cls')
        print("Balra mentél és találtál egy oxigén palackot!")
        print("Mit teszel?")
        print("(elmegyek vele/nélküle megyek)")
        tett=input()
        if tett=="elmegyek vele":
            print("Van egy oxigén palackod!")
            o2=1
            time.sleep(3)          
        k=1
        os.system('cls')
        print("Visszatértél a hajóhoz.")
    elif megy=="Jobbra megyek" or megy=="jobbra megyek":
        os.system('cls')
        print("Jobbra mentél és találtál egy térképet!")
        print("Mit teszel vele?")
        print("(elmegyek vele/nélküle megyek)")
        tett2=input()
        if tett2=="elmegyek vele":
            print("Szereztél egy térképet")
            map=1
            time.sleep(3)
        k=1
        os.system('cls')
        print("Visszatértél a hajóhoz.")
    elif megy=="Kihajózok" or megy=="kihajózok":
        os.system('cls')
        print("Kihajóztál az óceánra!")
        k=0
    else:
        print("Valamit elírtál.")
        os.system('cls')
time.sleep(2)
dmg=0
prot=0
ghj=1
os.system('cls')
print("Használd az eszköztárad az eszköztár szóval!")
print("eszköztár")
print("")
print("Megjegyzés:Az eszköztárad csak csata és puzzle estén tudod használni!")
inv=input()
os.system('cls')
if inv=="eszköztár" or inv=="Eszköztár":
    print("Nagyszerű. Itt láthatod hogy milyen dolgaid vannak.")
    print("Ha beírod a nevüket akkor tudod használni őket.")
    print("Ha beírod hogy statisztika láhatod a statisztikáid.")
    print("A kilép szóval pedig kiléphetsz az eszköztárból.")
    time.sleep(6)
    os.system('cls')
while ghj!=0:
    print("STATISZTIKA")
    if map==1:
        print("térkép")
    if o2==1:
        print("oxigén palack")
    vál=input()
    if vál=="térkép" or vál=="Térkép":
        os.system('cls')
        print("A térképen látsz egy útvonalat és egy háromágú szigonyt a víz alatt.")
        time.sleep(3)
        print("Jaj, ne! A térképet elvitte a szél!")
        time.sleep(3)
        os.system('cls')
        map=0
        ghj=1
    elif vál=="oxigén palack" or vál=="Oxigén palack" or vál=="oxigénplack" or vál=="Oxigénpalack":
        os.system('cls')
        print("Felvetted az oxigén palackot.")
        time.sleep(3)
        os.system('cls')
        o2=0
        ghj=1
    elif vál=="Statisztika" or vál=="statisztika":
        print("        Statisztikáid:-életerő:"+str(élet))
        print("                      -intelligenciád:"+str(iq))
        print("                      -fizikai erőd:"+str(erő))
        print("                      -reflexeid:"+str(reflex))
        print("                      -szerencséd:"+str(luck))
        print("                      -sebzésed:"+str(dmg))
        print("                      -védelmed:"+str(prot))
        time.sleep(5)
        os.system('cls')
    elif vál=="Kilép" or vál=="kilép":
        print("Kiléptél az eszköztáradból.")
        ghj=0
        os.system('cls')
    else:
        print("Valamit elírtál!")
        os.system('cls')
print("[Gondolat]:A hajón van szonár az segít felderíteni a tengerfeneket.")
os.system('color 1')
print("(Szonár)")
sz=input()
if sz=="szonár" or sz=="Szonár":
    print("")