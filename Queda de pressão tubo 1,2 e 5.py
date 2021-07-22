import matplotlib.pyplot as plt

plt.plot([500,1000,1250,1500],[156.33,58.62,1201.78,1338.57],'-o')
plt.plot([500,1000,1250,1500],[752.34,2481.73,4406.54,7435.43],'-o')
plt.plot([500,1000,1250,1500],[527.61,869.58,1778.25,3107.05],'-o')
plt.legend(["Tubo 1","Tubo 2", "Tubo 5"])
plt.ylabel('Queda de Pressão (Pa)')
plt.xlabel('Vazão volumétrica L/h')
plt.title('Queda de Pressão em função da Vazão')
plt.grid()
plt.show()