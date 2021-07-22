import matplotlib.pyplot as plt

plt.plot([2587.47,5174.94,7762.40,10349.87],[0.0171,0.0214,0.0361,0.0288],'-o')
plt.plot([3665.58,7331.16,10996.74,14662.32],[0.0360,0.0307,0.0316,0.0260],'-o')
plt.plot([2618.27, 5236.54, 7854.81, 10473.08],[0.1611,0.0443,0.0269,0.0383],'-o')
plt.legend(["Tubo 3","Tubo 4","Tubo 5"])
plt.ylabel('Fator de atrito')
plt.xlabel('Número de Reynolds')
plt.title('Vazões 100-400')
plt.grid()
plt.show()