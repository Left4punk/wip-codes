import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

## Loading Results
#df = pd.read_csv('xp_final_results_1000_runs.csv')

df = pd.read_csv('bit_emissions_results_1000_runs.csv')

#df['XP per Hour'] = df['Total XP'] / df['Total Play Time']

df['BIT per Hour'] = df['Total Bits'] / df['Total Play Time']

plt.figure(figsize=(10, 6))
#sns.boxplot(x=df['XP per Hour'], color="lightblue")

sns.boxplot(x=df['BIT per Hour'], color="lightblue")

# Calculating mean & standard dev

#mean_xp_per_hour = df['XP per Hour'].mean()
#std_xp_per_hour = df['XP per Hour'].std()

mean_Bit_per_hour = df['BIT per Hour'].mean()
std_Bit_per_hour = df['BIT per Hour'].std()


# Adding Legend con w Mean and Std
plt.legend([f'Mean: {mean_Bit_per_hour:.2f}, Standard Deviation: {std_Bit_per_hour:.2f}'], loc='upper right')

plt.xlabel('BIT Emission per hour')
plt.title('Distribution of $BIT/Hour after 1000 simulations')
plt.grid(False)

plt.savefig('Bit_per_hour.png')