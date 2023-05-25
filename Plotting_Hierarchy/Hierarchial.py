import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from Constant.constant import *
from sklearn.metrics import silhouette_score

datas = list_1

# Performing the hierarchical clustering
hierarchical_clustering = linkage(datas, method='single')

# Plot the clusters
plt.figure(figsize=(10, 5))
dendrogram(hierarchical_clustering)
plt.xlabel('Number of Dataset')
plt.ylabel('Frequencies')
# plt.show()

from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean',linkage='single')
cluster = cluster.fit_predict(datas)
print(cluster)

from sklearn.metrics import silhouette_score

# Calculate the silhouette score
silhouette_avg = silhouette_score(datas, cluster, metric='euclidean')
# silhouette_avg = silhouette_score(D, labels, metric=soft_dtw)

print(f"Silhouette Score: {silhouette_avg}")