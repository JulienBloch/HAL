import matplotlib.pyplot as plt
import numpy as np

datasets = [open("EvsB15.csv", "rb"), open("EvsB20.csv", "rb"), open("EvsB25.csv", "rb"), open("EvsB28.csv", "rb")]





for z in datasets:
	data = np.loadtxt(z, delimiter=",", skiprows=0)

	pressure = data[0, 0]
	pressure_error = data[0, 1]

	B = data[:,2]
	xerr = data[:,3]
	E = 25*data[:,4]
	yerr = 25*data[:,5]

	plt.errorbar(B, E, yerr=yerr, xerr=xerr, ecolor='red', fmt='o')
	plt.xlabel("Magnetic Field in milliTesla")
	plt.ylabel("Hall Voltage in Volts")
	plt.title("Hall Voltage as a Function of Magnetic Field, at " + str(pressure) + " +/- " + (str(pressure_error)))
	plt.show()
