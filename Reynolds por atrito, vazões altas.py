import matplotlib.pyplot as plt

plt.plot([7744.18, 15488.36, 19360.45, 23232.54],[0.1424,0.0133, 0.1751, 0.1355],'-o')
plt.plot([9818.52, 19637.03, 24546.29, 29455.55],[0.2091, 0.1725, 0.1960, 0.2297],'-o')
plt.plot([13091.35, 26182.71, 32728.38, 39274.06],[0.0348,0.0143,0.0188,0.0228],'-o')
plt.legend(["Tubo 1","Tubo 2", "Tubo 5"])
plt.ylabel('Fator de atrito')
plt.xlabel('Número de Reynolds')
plt.title('Vazões 500-1500')
plt.grid()
plt.show()