import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/Users/luizscheuer/Library/CloudStorage/Dropbox/Projects/FIFA Ultimate Team Analysis/joined_data.csv')
# print(df)

# Selected columns to calculate correlation upon
selected_columns = df.iloc[:, 6:52]  # Columns from index 6 to 52 (exclusive of 6)

# Correlation Matrix
corr_matrix = selected_columns.corr()

# Correlation Matrix Scatter
pd.plotting.scatter_matrix(corr_matrix, figsize=(25,25))

# Generate Image
plt.figure(figsize=(25,25))
plt.show()

# Correlation Matrix heatmap
sns.heatmap(corr_matrix, vmin=-1, vmax=1, square=True)

# Save figure
#plt.savefig('/Users/luizscheuer/Library/CloudStorage/Dropbox/Projects/FIFA Ultimate Team Analysis/correlation_matrix_all_data.png', dpi=300, bbox_inches='tight')

