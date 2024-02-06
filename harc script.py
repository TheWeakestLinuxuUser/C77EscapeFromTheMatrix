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
realhp=élet-7
valami=1
prot=0
while fight!=0:
    if valami==1:
        print("Valami megtámadott")
    valami=0
    print("                                     életereje:"+str(re))
    os.system('color 2')
    dmge=random.randint(1,realhp)
    print("Sebzett rád "+str(dmge)+"-t")
    dmge=dmge-prot
    élet=élet-dmge
    if élet<1:
        os.system('cls')
        print("             Meghaltál")
        print("Ne feledd az óceán veszélyesebb, mint hinnéd!")
        os.system('color 4')
        élet=realhp+7
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
