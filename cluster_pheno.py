import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

def log_norm(df):
    return np.log2(df+0.001)

data = pd.read_csv("/screen/D_plate_phenotype/data.csv",index_col=0, header=0)
print(data.describe())
print(data.head())
#data = data[~data.index.duplicated()]
#More than 75% of the data multiples are below 2, but there are still cases where the data is 0, so log2(n+1) is used to process the data


spe = data.pop('group')
gene = data.pop('gene')
ann = data.pop('annotation')
df_log_norm = data.apply(zscore)


print('after scaler:\n',df_log_norm.describe())
print(df_log_norm.head(5))

colors = pd.Series(sns.color_palette("deep", 20).as_hex())
lut = dict(zip(spe.unique(),colors))
row_colors = spe.map(lut)

clab = ['G3V2']

#Draw
g = sns.clustermap(
    data=df_log_norm,
    row_colors=row_colors,
    #row_cluster=False,
    #col_cluster=False,
    #z_score=1,
    cmap='bwr',
    vmax=1.28,
    vmin=-1.28,
    xticklabels=1,
)

g.figure.set_size_inches(12,20)

reordered_labels = df_log_norm.index[g.dendrogram_row.reordered_ind].tolist()
use_labels = clab
use_ticks = [reordered_labels.index(label) + .5 for label in use_labels]
#Obtain the reset ticks data
g.ax_heatmap.set(yticks=use_ticks, yticklabels=use_labels)

#Figure legend
for lable in spe.unique():
    g.ax_row_dendrogram.bar(0, 0, color=lut[lable],
                            label=lable, linewidth=0
   )
g.ax_row_dendrogram.legend(loc="center", ncol=1)

use_labels = clab
use_ticks = [reordered_labels.index(label) + .5 for label in use_labels]
#Obtain the reset ticks data

g.ax_heatmap.set(yticks=use_ticks, yticklabels=use_labels)
#Reset the y-label of the cluster

re_lab = df_log_norm.columns[g.dendrogram_col.reordered_ind].tolist()

newfile = df_log_norm.reindex(reordered_labels)
newfile1 = newfile.reindex(re_lab, axis=1)
newfile1['gene'] = gene.to_frame()['gene']
newfile1['annotation'] = ann.to_frame()['annotation']
newfile1['group'] = spe.to_frame()['group']

newfile1.to_excel('/screen/D_plate_phenotype/240620.xlsx')
plt.savefig('/screen/D_plate_phenotype/240620.pdf',dpi=200)

plt.show()
