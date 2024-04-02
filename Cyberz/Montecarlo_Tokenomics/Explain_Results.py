import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargando el archivo CSV
df = pd.read_csv('xp_final_results_1000_runs.csv')
df['XP per Hour'] = df['Total XP'] / df['Total Play Time']


plt.figure(figsize=(10, 6))
sns.boxplot(x=df['XP per Hour'], color="lightblue")

# Calculando la media y la desviación estándar de la experiencia por hora
mean_xp_per_hour = df['XP per Hour'].mean()
std_xp_per_hour = df['XP per Hour'].std()

# Añadiendo leyenda con la media y desviación estándar
plt.legend([f'Mean: {mean_xp_per_hour:.2f}, Standard Deviation: {std_xp_per_hour:.2f}'], loc='upper right')

plt.xlabel('Experience per hour')
plt.title('Distribution of XP/Hour after 1000 simulations')
plt.grid(False)

plt.savefig('xp_per_hour.png')