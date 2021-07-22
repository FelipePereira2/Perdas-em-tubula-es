import matplotlib.pyplot as plt

plt.plot([100,200,300,400],[9.76, 48.79, 185.64, 263.81],'-o')
plt.plot([100,200,300,400],[117.09, 400.07, 927.00, 1356.34],'-o')
plt.plot([100,200,300,400],[97.71,107.48,146.56,371.28],'-o')
plt.legend(["Tubo 3","Tubo 4", "Tubo 5"])
plt.ylabel('Queda de Pressão (Pa)')
plt.xlabel('Vazão volumétrica L/h')
plt.title('Queda de Pressão em função da Vazão')
plt.grid()
plt.show()