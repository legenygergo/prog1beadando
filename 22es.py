def legnagyobb_kozos_oszto(a, b):
    while b:
        a, b = b, a%b
    return a

bemenet=input("Adja meg az első tört számait vesszővel elválasztva: ")
bemenet2=input("Adja meg a második tört számait vesszővel elválasztva: ")
a, b = bemenet.split(",")
c, d=bemenet2.split(",")

nevezo=int(b)*int(d)
szamlalo=int(a)*int(d) + int(b)*int(c)
x=legnagyobb_kozos_oszto(nevezo, szamlalo)

ujnevezo=int(nevezo/x)
ujszamlalo=int(szamlalo/x)

print(str(ujszamlalo)+"/"+str(ujnevezo))