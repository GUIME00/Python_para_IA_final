import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)

# Usando o método de seno no Numpy
y_line = np.sin(x)
categorias = ['Ação','Comédia','Drama','Terror']
valores = [20,40,50,30]

# Dados por gráfico de dispersão
x_scatter = np.random.rand(50)
y_scatter = x_scatter + np.random.randn(50)*0.1

# Histograma
hist_data = np.random.randn(1000)
fig, axs = plt.subplots(2,2, figsize=(10,8))
axs[0,0].plot(x,y_line, color='Blue', linestyle='--', label='sin(x)')

axs[0,0].set_title('Gráfico de Linha')
axs[0,0].legend()

axs[0,1].bar(categorias, valores, color=['Green','Red','Orange','Purple'])
axs[0,1].set_title('Gráfico de Barras')

axs[1,0].scatter(x_scatter,y_scatter, alpha=0.6,color='Black')
axs[1,0].set_title('Gráfico de Dispersão')

axs[1,1].hist(hist_data,bins=30, color='Yellow', edgecolor='White')
axs[1,1].set_title('Histograma')

fig.tight_layout()

plt.show()