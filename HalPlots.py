import matplotlib.pyplot as plt
import numpy as np

z = open("BvsI.csv", "rb")
BvsI = np.loadtxt(z, delimiter=",", skiprows=0)

print(BvsI)
print(BvsI[:,0])
print(np.transpose((BvsI[:,0])))

B = BvsI[:,0]
I = BvsI[:,2]

print(B)
print(I)

plt.scatter(B, I)
plt.xlabel("Current in Amperes")
plt.ylabel("Magnetic Field in milliTesla")
plt.title("Magnetic Field as a Function of Current, at 16 +/- .1 Torr")
plt.errorbars
plt.show()