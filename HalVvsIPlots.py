import matplotlib.pyplot as plt
import numpy as np

datasets = [open("VvsI_15torr.csv", "rb"), open("VvsI_18torr.csv", "rb"), open("VvsI_21torr.csv", "rb"), open("VvsI_24torr.csv", "rb"), open("VvsI_27torr.csv", "rb"), open("VvsI_30torr.csv", "rb")]

pressures = [15.2, 18.25, 21, 24.2, 27, 30]
pressure_errors = [.1, .05, .1, .1, .1, .1]

i = 0
for z in datasets:
	data = np.loadtxt(z, delimiter=",", skiprows=0)

	pressure = pressures[i]
	pressure_error = pressure_errors[i]

	high_V = data[:,0]
	I = data[:,1]
	yerr1 = data[:,2]
	discharge_V = 250*data[:,3]
	yerr2 = 250*data[:,4]

	fig, ax2 = plt.subplots()

	ax1 = ax2.twinx()
	ax2.errorbar(high_V, discharge_V, yerr=yerr2, ecolor='green', fmt='*')
	ax2.legend('Voltage')
	ax2.set_ylabel("Discharge Voltage in Volts")

	ax1.errorbar(high_V, I, yerr=yerr1, ecolor='red', fmt='o')
	ax1.legend('Current')

	ax1.set_xlabel("High Voltage in kiloVolts")
	ax1.set_ylabel("Current in milliAmps")
	plt.show()
	break

	i += 1
