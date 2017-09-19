import matplotlib.pyplot as plt
import numpy as np

EvsB = np.loadtxt(open("EvsB.csv", "rb"), delimiter=",", skiprows=0)

P = EvsB[:,0]
B = EvsB[:,2]
V = 25*EvsB[:,4]

bins = np.array([np.linspace(14, 29, num=5), np.linspace(-71, 71, num=30)])

h = plt.hist2d(P, B, weights=V, bins=bins)
plt.xlabel("Pressure in Torr")
plt.ylabel("Magnetic Field in milliTesla")
plt.title("Hall Voltage as Function of Pressure and Magnetic Field")
plt.colorbar(h[3])
plt.show()