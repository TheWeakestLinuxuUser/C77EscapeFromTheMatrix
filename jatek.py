from itertools import permutations
import os
from re import S, T
import time
import random
from traceback import print_tb
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
o2=-1
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
dmg=1
prot=0
ghj=1
os.system('cls')
print("Használd az eszköztárad az eszköztár szóval!")
print("eszköztár")
print("")
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
z=0
s=0
u=1
ut=1
while u!=0:
    if sz=="szonár" or sz=="Szonár":
        os.system('cls')
        print("A szonár képén látsz egy T-alakú dolgot.")
        print("Mit teszel?")
        print("(leúszok/tovább megyek)")
        ht=input()
        if ht=="leúszok" or ht=="Leúszok":
            os.system('cls')
            print("Leúsztál és megnézted kiderült hogy az egy korall,")
            print("de mikor felúsztál belegabajodtál egy portugál gálya csápjaiba és")
            print("a mérgétől meghaltál.")
            time.sleep(6)
            os.system('color 2')
            os.system('cls')
            print("             Meghaltál")
            print("Ne feledd az óceán veszélyesebb, mint hinnéd!")
            os.system('color 4')
            time.sleep(3)
            os.system('cls')
            ut=0
        elif ht=="tovább megyek" or ht=="Tovább megyek":
            os.system('cls')
            print("Tovább mentél.")
            time.sleep(2)
            os.system('cls')
            ut=1
            print("(Szonár)")
            sz=0
            z=input()
    elif z=="szonár" or z=="Szonár":
        print("A szonár képén látsz egy három ágú szigonyt.")
        print("Mit teszel?")
        print("(Leúszok/Tovább megyek)")
        ht=input()
        if ht=="leúszok" or ht=="Leúszok":
            if o2==0:
                print("Leúsztál és megtaláltad Atlantiszt!")
                u=0
            else:
                print("Hiába találtad meg Atlantiszt nem tudtál leúszni.")
                time.sleep(6)
                os.system('color 2')
                os.system('cls')
                print("             Meghaltál")
                print("Ne feledd az óceán veszélyesebb, mint hinnéd!")
                os.system('color 4')
                time.sleep(3)
                os.system('cls')
                ut=0
        elif ht=="tovább megyek" or ht=="Tovább megyek":
            print("Tovább mentél és nem találtad meg Atlantiszt!")
            s=0
            ut=0
print("Leértél Atlantiszba.")
key=0
time.sleep(3)
os.system('cls')
print("A feladatod megtalálni Atlantisz főtemplomát.")
print("(körbenéz)")
fi=input()
if fi=="körbenéz" or fi=="Körbenéz":
    print("Körbenéztél és észre vetted hogy van egy út balra és jobra")
    print("[Gondolat]:Mindig azt mondják néz először jobbra utána balra.")
    os.system('cls')
    os.system('color 1')
    gg=1
    while gg!=0:
        print("Merre mész?")
        print("(jobbra/balra)")
        cig=input()
        if cig=="balra" or cig=="Balra":
            os.system('cls')
            print("Elmentél balra és megtaláltad Atlantisz főterét ahol látod a templomot és 5 darab házat.")
            god=1
            while god>0:
                time.sleep(4)
                os.system('cls')
                print("Ittvagy a főtéren.")
                print("Merre mész?")
                print("(1.ház/2.ház/3.ház/4.ház/5.ház/templom)")
                fogyi=input()
                if fogyi=="1.ház":
                    os.system('cls')
                    print("Bementél az első házba és találtál egy papírt az asztalon.")
                    print("(felveszem/itthagyom)")
                    hjk=input()
                    if hjk=="felveszem" or hjk=="Felveszem":
                        os.system('cls')
                        print("A paíron a következő szöveg áll:")
                        print("[Karakter 1]:Hihetlen nem volt semmi ami ledönthette volna Atlantiszt.Fejlettebbek voltunk mindenkinél de,")
                        print("             az embernek ha a büszkeség a fejébe száll nem gondol semmi rosszra.")
                        print("             Atlantisz is ezért merült alá mert nem gondoltunk a természet erejére...")
                        print("")
                        print("                                                             Nyomj entert a folytatáshoz.")
                        edfglgh=input()
                        os.system('cls')
                        print("Kimentél a házból.")
                        time.sleep(2)
                        os.system('cls') 
                elif fogyi=="2.ház":
                    os.system('cls')
                    print("A házban találtál egy kardot és egy páncélt.")
                    print("(felvesz kard/felvesz páncél/kimegyek a házból)")
                    imre=input()
                    nba=1
                    while nba!=0:
                        print("(kard/páncél/kimegyek)")
                        imre=input()
                        if imre=="kard" or imre=="Kard":
                            print("Felvetted a kardot")
                            sword=1
                            time.sleep(2)
                            os.system('cls')
                        elif imre=="páncél" or imre=="Páncél":
                            os.system('cls')
                            print("Felvetted a páncélt.")
                            armor=1
                            time.sleep(2)
                            os.system('cls')
                        elif imre=="kimegyek" or imre=="Kimegyek":
                            nba=0
                elif fogyi=="3.ház":
                    os.system('cls')
                    zunk=1
                    while zunk!=0:
                        print("Találtál a házban egy papírt az asztalon és egy kardot.")
                        print("(papír/kard/kimegyek)")
                        negroczki=input()
                        if negroczki=="kard" or negroczki=="Kard":
                            os.system('cls')
                            print("Felvetted a kardot.")
                            sword1=1
                            time.sleep(2)
                            os.system('cls')
                        elif negroczki=="papír" or negroczki=="Papír":
                            os.system('cls')
                            print("A paíron ez olvasható:")
                            print("[Karakter2]:Az fentiek megrohamoztak itt lent minket.Teljesen boldogan tudtunk élni de,")
                            print("            lejöttek és lemészárolnak minket.Pár emberünket elrabolták és elvitték őket.Azóta")
                            print("            nem hallotunk felőlük.")
                            print("")
                            print("                                                             Nyomj entert a folytatáshoz.")
                            asycfvgbhnj=input()
                            os.system('cls')
                        elif negroczki=="kimegyek" or negroczki=="Kimegyek":
                            print("Kimentél")
                            time.sleep(1)
                            os.system('cls')
                            zunk=0
                elif fogyi=="4.ház":
                    os.system('cls')
                    print("Megláttál egy páncélt a fogason.")
                    print("(elviszem/itthagyom)")
                    scrap=input()
                    hunk=1
                    while hunk!=0:
                        os.system('cls')
                        if scrap=="elviszem" or scrap=="Elviszem":
                            print("Elvitted a páncélt")
                            armor1=1
                            time.sleep(1)
                            hunk=0
                            os.system('cls')
                        elif scrap=="itthagyom" or scrap=="Itthagyom":
                            print("Kimentél")
                            time.sleep(1)
                            os.system('cls')
                            hunk=0
                elif fogyi=="5.ház":
                    os.system('cls')
                    print("Találtál egy papírt az asztalon.")
                    print("(olvas)")
                    mechanic=input()
                    if mechanic=="olvas" or mechanic=="olvas":
                        os.system('cls')
                        print("A papíron a következő áll:")
                        print("[Karakter3]:A végzet után azt hittük nincs tovább, de nem így lett.")
                        print("            Atlantisznak külső védelme a föld alá nem terjed ezért volt képes elsüllyedni, de")
                        print("            a fenti védelem olyan erős, hogy élhető helyet csinált Atlantiszból a víz alatt is.")
                        print("            Tehát itt éltünk tovább...")
                        print("")
                        print("                                                                        Nyomj entert a folytatáshoz")
                        fsuigfoijgwer=input()
                elif fogyi=="6.ház":
                    os.system('cls')
                    print("Hé ide nem lett volna szabad bejönnöd!")
                    print("[Háttérben]:Gyorsan állítds le a szimulációt")
                    os.system('color 6')
                    time.sleep(2)
                    os.system('cls')
                    exit(0)
                elif fogyi=="templom":
                    os.system('cls')
                    god=-1
                    if key==1:
                        print("A talált kulccsal kitudod nyitni az ajtót.")
                        print("[Gondolat]:Jobb ha átnézem mit is gyűjtöttem össze ide lent!")
                        ghj=1
                        time.sleep(6)
                        os.system('cls')
                        while ghj!=0:
                            print("STATISZTIKA")
                            if sword==1:
                                print("Kard sebzése:5")
                                print("Neve:Filéző kard")
                                dmg=5
                            if sword1==1:
                                print("Kard sebzése:7")
                                print("Neve:Cápa vágó")
                                dmg=7
                            if armor==1:
                                print("Páncél egy furcsa varázslattal ami arra képessé teszi hogy kis sbezés esetén életerőt tölt! védelme:5")
                                print("Neve:Teknős páncél")
                                prot=5
                            if armor1==1:
                                print("Páncél egy furcsa varázslattal ami arra képessé teszi hogy kis sbezés esetén életerőt tölt! védelme:10")
                                print("Neve:Gyöngy páncél")
                                prot=10
                            vál=input()
                            if vál=="filéző kard" or vál=="Filéző kard":
                                os.system('cls')
                                print("Magadhoz vetted a kardot")
                                time.sleep(3)
                                os.system('cls')
                                sword=0
                                ghj=1
                            elif vál=="cápa vágó" or vál=="Cápa vágó":
                                os.system('cls')
                                print("Magadhoz vetted a kardot!")
                                time.sleep(3)
                                os.system('cls')
                                sword1=0
                                ghj=1
                            elif vál=="Teknős páncél" or vál=="teknős páncél":
                                print("Felvetted a páncélt!")
                                time.sleep(3)
                                os.system('cls')
                                armor=0
                            elif vál=="Gyöngy páncél" or vál=="gyöngy páncél":
                                print("Felvetted a páncélt!")
                                time.sleep(3)
                                os.system('cls')
                                armor1=0
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
                        print("Bementél a templomba és meg láttál valamit de nem tudod mi az.")
                        re=100
                        fight=1
                        realhp=élet-5
                        valami=1
                        rreflex=20-(reflex-1)
                        while fight!=0:
                            if valami==1:
                                print("Egy hatalmas szörny megtámadott!")
                                valami=0
                            print("                                     életereje:"+str(re))
                            os.system('color 2')
                            dmge=random.randint(1,realhp)
                            dmge=dmge-prot
                            esé=random.randint(-3,rreflex)
                            if esé==1:
                                print("Kitrétél az ütés elől!")
                            else:
                                élet=élet-dmge
                                print("Sebzett rád "+str(dmge)+"-t")
                            if élet<1:
                                os.system('cls')
                                print("             Meghaltál")
                                print("Ez a szörny nem foghat kirajtad!")
                                print("        Szedd össze magad!")
                                os.system('color 4')
                                élet=realhp+5
                                re=100
                                time.sleep(2)
                                os.system('cls')
                            elif élet>1:
                                print("Támadj                               életerőd:"+str(élet))
                                print("(Támadás)")
                                t=input()
                                os.system('cls')
                                if t=="Támadás" or t=="támadás":
                                    seb=random.randint(1,erő)
                                    seb=seb*dmg
                                    print("Sebeztél "+str(seb)+"-t")
                                    re=re-seb
                                    os.system('color 2')
                                    if re<1:
                                        fight=0
                                        print("Érdemes meggyógyítanod magad!")
                                        print("(Gyógyítás)")
                                        print("[Gondolat]:Milyen szerencse hogy hoztam magammal elsősegély készeltet!")
                                        htz=input()
                                        if htz=="Gyógyítás" or htz=="gyógyítás":
                                            élet=realhp
                                            print("Meggyógyítottad magad életerőd:"+str(élet))              
                        fight1=1
                        gitr=1
                        re1=400
                        os.system('cls')
                        while fight1!=0:
                            if gitr==1:
                                print("A szörny megsebesült emiatt még agresszívabb lett!")
                                gitr=0
                            print("                                     életereje:"+str(re1))
                            os.system('color 2')
                            dmge=élet
                            dmge=dmge-prot
                            click=random.randint(1,8)
                            if click==1:
                                    print("A")
                                    bazdemg="a"
                            elif click==2:
                                    print("S")
                                    bazdemg="s"
                            elif click==3:
                                    print("D")
                                    bazdemg="d"
                            elif click==4:
                                    print("F")
                                    bazdemg="f"
                            elif click==5:
                                    print("Q")
                                    bazdemg="q"
                            elif click==6:
                                    print("W")
                                    bazdemg="w"
                            elif click==7:
                                    print("E")
                                    bazdemg="e"
                            elif click==8:
                                    print("R")
                                    bazdemg="r"
                            print("Védekezz a megfelelő betű lenyomásával!")
                            hogy=input()
                            os.system('cls')
                            if bazdemg!=hogy:
                                    élet=élet-dmge
                                    dmge=dmge-prot
                                    esé=random.randint(-3,rreflex)
                                    if esé==1:
                                        élet=élet+dmge
                                        print("Kitrétél az ütés elől!")
                            if élet<1:
                                os.system('cls')
                                print("             Meghaltál")
                                print("Ez a szörny nem foghat kirajtad!")
                                print("        Szedd össze magad!")
                                os.system('color 4')
                                élet=realhp
                                re1=400
                                time.sleep(2)
                                os.system('cls')
                            elif élet>1:
                                print("Támadj                               életerőd:"+str(élet))
                                print("(Támadás)")
                                t=input()
                                os.system('cls')
                                if t=="Támadás" or t=="támadás":
                                    seb=random.randint(1,erő)
                                    seb=seb*dmg
                                    print("Sebeztél "+str(seb)+"-t")
                                    re1=re1-seb
                                    os.system('color 2')
                                    if re1<1:
                                        print("Nyertél!")
                                        fight1=0
                                    gg=0
                    elif key==0:
                        print("Mikor a kaput megnézed látod kulcs nyitja ezért körbe nézel és látod hogy ahonnan jöttél valami csillog ezért vissza mész.")
                    cig=0               
        elif cig=="jobbra" or cig=="Jobbra":
            print("Mikor jobbra indultál észre vettél valami csillogót. Felvetted és észre vetted hogy  az egy kulcs volt.")
            key=1
            cig=0
            time.sleep(5)
            os.system('cls')
time.sleep(5)
os.system('cls')
print("Mivel legyőzted a szörnyet megszerezted a fegyverét egy mágikus szigony amivel hiper gyorsan tudsz a vizben közlekedni.")
print("A szigonnyal vissza mentél a szigetre Lajoshoz aki mint ígérte ott várt rád.")
time.sleep(5)
os.system('cls')
print("[Lajos]:Hát vissza tértél el se hiszem a többieknek nem sikerült legyőzni a szörnyet.")
print("        Tedd le a szigonyt és gyere velem most próbáljuk meg élesben...")
time.sleep(6)
os.system('color 3')
exit(0)