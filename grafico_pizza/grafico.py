import matplotlib.pyplot as plt
import numpy as np

# Valores do Gráfico #
y = np.array([10, 20, 25, 22, 23])

# Itens do Gráfico #
lb = ['Carros', 'Motos', 'ônibus', 'Trem', 'Metro']

# Espaço entre as "fatias" do gráfico #
exp = [0, 0, 0.2, 0, 0]

# Monta o Gráfico e depois o mostra na tela #
plt.pie(y, labels=lb, explode=exp, shadow=True)
plt.show()
