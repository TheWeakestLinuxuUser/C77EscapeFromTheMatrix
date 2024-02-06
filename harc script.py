import random
import os
import time
dmg=20
élet=20
erő=20
luck=random.randint(1,20)
es=1
fight=1
re=40
realhp=élet-5
valami=1
reflex=20
rreflex=20-(reflex-1)
while fight!=0:
    if valami==1:
        print("Valami megtámadott")
    valami=0
    print("                                     életereje:"+str(re))
    os.system('color 2')
    dmge=random.randint(1,realhp)
    esé=random.randint(-3,rreflex)
    if esé==1:
        print("Kitrétél az ütés elől!")
    else:
        élet=élet-dmge
        print("Sebzett rád "+str(dmge)+"-t")
    if élet<1:
        os.system('cls')
        print("             Meghaltál")
        print("Ne feledd az óceán veszélyesebb, mint hinnéd!")
        os.system('color 4')
        élet=realhp+5
        re=40
        valami=1
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
                fight=0
