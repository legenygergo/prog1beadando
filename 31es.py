import numpy as np
import matplotlib.pyplot as plt

matrixmeret=input("Adja meg a mátrix méreteit, illetve a választott szin nevét vesszőkkel és egy space-el elválasztva: ")
n, m, szin = matrixmeret.split(", ")

piros = np.zeros([int(n), int(m), 3], dtype=np.uint8)
piros[:,:] = [255, 0, 0]
kek = np.zeros([int(n), int(m), 3], dtype=np.uint8)
kek[:,:] = [0, 0, 255]
sarga= np.zeros([int(n), int(m), 3], dtype=np.uint8)
sarga[:,:] = [255, 255, 0]

dict={"matrix":np.zeros([int(n), int(m), 3], dtype=np.uint8), "piros":piros[:,:], "kek": kek[:,:], "sarga":sarga[:,]}

if szin=="lila":
    lila=dict.get("matrix")
    lila[:,:]=dict.get("piros")+dict.get("kek")
    plt.imshow(lila)
    plt.show()

elif szin=="fehér":
    feher=dict.get("matrix")
    feher[:,:]=dict.get("sarga")+dict.get("kek")
    plt.imshow(feher)
    plt.show()

elif szin=="zöld":
    zold = dict.get("matrix")
    zold[:, :] = dict.get("sarga") - dict.get("piros")
    plt.imshow(zold)
    plt.show()
else:
    s=dict.get("matrix")
    s[:,:]=dict.get("sarga")
    plt.imshow(s)
    plt.show()