# T=int(input("Adja meg a tesztesetek számát (1-től 5000-ig): "))
# szam=0
# mehet=True
# if T == szam or -1>=T or T>5000:
#     print("T nem esik bele a megadott tartományba.")
#     mehet=False
#
# while szam != T and mehet:
#     szm=input("Adja meg az N sorok és M oszlopok számát elválasztva (1-től 50-ig): ")
#     N, M=szm.split(" ")
#     if int(N)>50 or 1>int(N) or int(M)>50 or 1>int(M):
#         print("N vagy M nem esik bele a megadott tartományba.")
#         break
#     if (int(N) ==1 or int(M) ==1) or int(N)*int(M) % 2 !=0:
#         print("No")
#     else:
#         print("Yes")
#     szam+=1

# A feladatból nem volt egyértelmű, hogy lehet-e cserélni az elemeket, úgy vettem hogy nem. Igy akkor tér vissza
# Yes-sel, ha megfelel azoknak a kritériumoknak, hogy az M és N szorzata páros, illetve egyik sem lehet egyenlő
# 1-el. Ha mégis lehetne cserélni, a különbség annyi lenne, hogy egy egysoros vagy egy oszlopos mátrixnál is
# visszatérhetne Yes-el, amennyiben az egyik paraméter páros. Akkor a következőképpen néz ki a megoldás:


T=int(input("Adja meg a tesztesetek számát (1-től 5000-ig): "))
szam=0
mehet=True
if T == szam or -1>=T or T>5000:
    print("T nem esik bele a megadott tartományba.")
    mehet=False

while szam != T and mehet:
    szm=input("Adja meg az N sorok és M oszlopok számát elválasztva (1-től 50-ig): ")
    N, M=szm.split(" ")
    if int(N)>50 or 1>int(N) or int(M)>50 or 1>int(M):
        print("N vagy M nem esik bele a megadott tartományba.")
        break
    if int(N)*int(M) % 2 !=0:
        print("No")
    else:
        print("Yes")
    szam+=1
