import pandas as pd
import seaborn as sns

# Crear el DataFrame con los datos proporcionados
data = {
    'Mes': ['Ene 2023', 'Feb 2023', 'Mar 2023', 'Abr 2023', 'May 2023', 'Jun 2023',
            'Jul 2023', 'Ago 2023', 'Sep 2023', 'Oct 2023', 'Nov 2023', 'Dic 2023'],
    'Cantidad': [2324, 3230, 4588, 18731, 4021, 14687, 4837, 19100, 13725, 22368, 10574, 14449]
}
df = pd.DataFrame(data)

# Configurar el estilo y el contexto de Seaborn
sns.set_style("whitegrid")
sns.set_context("talk")

# Visualización: Gráfico de barras para mostrar la cantidad por mes
plt.figure(figsize=(10, 6))
sns.barplot(x='Mes', y='Cantidad', data=df, palette='viridis')
plt.title('Cantidad por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
