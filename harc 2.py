fight1=1
import os
import time
import random
élet=20
erő=20
reflex=20
rreflex=20-(reflex-1)
bazdemg=0
realhp=élet
re=400
prot=10
dmg=7

while fight1!=0:
    print("                                     életereje:"+str(re))
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
        re=400
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
                print("Nyertél!")
                fight1=0
