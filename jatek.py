import os
import time
import random
os.system('color 2')
print("Mi a neved felfedező?")
nev=input()
if nev=="Napóleon":
    print("There is nothing we can do")
elif nev=="Fredy" or nev=="Fredy Fazbear":
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
    os.system('exit')
if nez=="körbenéz":
    print("Megtaláltad a hajót amivel kihajózhatsz és még két utat.")
    k=1
os.system('color 2')
while k!=0:
    print("Mit teszel?")
    print("Jobbra megyek,Balra megyek, Kihajózok")
    megy=input()
    if megy=="Balra megyek":
        os.system('cls')
        print("Balra mentél és találtál egy oxigén palackot!")
        print("Mit teszel?")
        print("elmegyek vele,nélküle megyek")
        tett=input()
        if tett=="elmegyek vele":
            print("Van egy oxigén palackod!")
            time.sleep(3)
            o2=1
        k=1
        os.system('cls')
        print("Visszatértél a hajóhoz.")
    elif megy=="Jobbra megyek":
        os.system('cls')
        print("Jobbra mentél és találtál egy térképet!")
        print("Mit teszel vele?")
        print("elmegyek vele, nélküle megyek")
        tett2=input()
        if tett2=="elmegyek vele":
            print("Szereztél egy térképet")
            time.sleep(3)
        k=1
        os.system('cls')
        print("Visszatértél a hajóhoz.")
    elif megy=="Kihajózok":
        os.system('cls')
        print("Kihajóztál az óceánra!")
        k=0
