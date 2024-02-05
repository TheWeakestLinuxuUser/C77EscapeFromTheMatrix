import random
import os
dmg=1
élet=20
erő=20
luck=random.randint(1,20)
es=1
kut=1
fight=1
re=40
if es==1:
    print("Valami megtámadott")
    while fight!=0:
        print("                                     életereje:"+str(re))
        dmge=random.randint(1,élet-5)
        print("sebzett rád "+str(dmge)+"-t")
        élet=élet-dmge
        print("Támadj                               életerőd:"+str(élet))
        print("(Támadás!)")
        t=input()
        os.system('cls')
        if élet<1:
            print("Meghaltál!")
            kut=0
            print("             Meghaltál")
            print("Ne feledd az óceán veszélyesebb, mint hinnéd!")
            os.system('color 4')
        if t=="Támadás" and kut==1:
            seb=random.randint(1,erő*dmg)
            print("Sebeztél "+str(seb)+"-t")
            re=re-seb
            if re<1:
                print("Nyertél!")
                fight=0
