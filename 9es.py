
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
    if (int(N) ==1 or int(M) ==1) or int(N)*int(M) % 2 !=0:
        print("No")
    else:
        print("Yes")
    szam+=1

