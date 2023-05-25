import numpy as np
from dtw import dtw
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from Constant.constant import list_1


""""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.."""""""""
# The data
X = list_1

# Initialize variables
distortions = []
K = range(1, 21)

# Calculate distortions for each value of K
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X)
    distortions.append(kmeanModel.inertia_)

# Plotting the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal K')
plt.show()