"""
import numpy as np
from tslearn.clustering import TimeSeriesKMeans
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from dataset import list_1

# Set the random seed for reproducibility
np.random.seed(42)

# Define your time series data
data = list_1

# Convert your data to a numpy array
X = np.array(data)

# Scale your data using TimeSeriesScalerMeanVariance
X_scaled = TimeSeriesScalerMeanVariance().fit_transform(X)

# Define the number of clusters and initialize the TimeSeriesSoftKMeans object
n_clusters = 5
soft_kmeans = TimeSeriesKMeans(n_clusters=n_clusters, metric="softdtw", max_iter=552, verbose=0)
# soft_kmeans = TimeSeriesKMeans(n_clusters=n_clusters, metric="dtw", max_iter=552, verbose=0)


# Fit the model to the scaled data
soft_kmeans.fit(X_scaled)

# Get the cluster labels and cluster centroids
labels = soft_kmeans.labels_
centroids = soft_kmeans.cluster_centers_

# print("labels=",labels)
# print(len(labels))


import numpy as np
from tslearn.clustering import TimeSeriesKMeans
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
from tslearn.metrics import dtw
from sklearn.metrics import silhouette_score
from tslearn.metrics import dtw
from tslearn.metrics import soft_dtw

# Set the random seed for reproducibility
np.random.seed(42)

# Define your time series data
data = list_1

# Convert your data to a numpy array
X = np.array(data)



# Scale your data using TimeSeriesScalerMeanVariance
X_scaled = TimeSeriesScalerMeanVariance().fit_transform(X)

# Define the number of clusters and initialize the TimeSeriesKMeans object
n_clusters =8
kmeans = TimeSeriesKMeans(n_clusters=n_clusters, metric="softdtw", max_iter=55, verbose=0)

# Compute the pairwise DTW distance matrix
D = np.zeros((X.shape[0], X.shape[0]))
for i in range(X.shape[0]):
    for j in range(i+1, X.shape[0]):
        D[i,j] = dtw(X[i], X[j])
        D[j,i] = D[i,j]

# Fit the model to the distance matrix
kmeans.fit(D)

# Get the cluster labels and cluster centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print(f"cluster={n_clusters},labels=,{labels}")

for index, item in enumerate(labels):
    print(f"dataset number{index}= {item}")

# silhouette_avg = silhouette_score(D, labels, metric=dtw)
silhouette_avg = silhouette_score(D, labels, metric=soft_dtw)

print("Silhouette score:", silhouette_avg)

"""



# import numpy as np
# from tslearn.clustering import TimeSeriesKMeans
# from tslearn.preprocessing import TimeSeriesScalerMeanVariance
# from tslearn.metrics import dtw
# from sklearn.metrics import silhouette_score
# from tslearn.metrics import dtw
# from tslearn.metrics import soft_dtw

# # Set the random seed for reproducibility
# np.random.seed(42)

# # Define your time series data
# data = list_1

# # Convert your data to a numpy array
# X = np.array(data)



# # Scale your data using TimeSeriesScalerMeanVariance
# X_scaled = TimeSeriesScalerMeanVariance().fit_transform(X)

# # Define the number of clusters and initialize the TimeSeriesKMeans object
# n_clusters =8
# kmeans = TimeSeriesKMeans(n_clusters=n_clusters, metric="softdtw", max_iter=55, verbose=0)

# # Compute the pairwise DTW distance matrix
# D = np.zeros((X.shape[0], X.shape[0]))
# for i in range(X.shape[0]):
#     for j in range(i+1, X.shape[0]):
#         D[i,j] = dtw(X[i], X[j])
#         D[j,i] = D[i,j]

# # Fit the model to the distance matrix
# kmeans.fit(D)

# # Get the cluster labels and cluster centroids
# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_

# print(f"cluster={n_clusters},labels=,{labels}")

# for index, item in enumerate(labels):
#     print(f"dataset number{index}= {item}")

# # silhouette_avg = silhouette_score(D, labels, metric=dtw)
# silhouette_avg = silhouette_score(D, labels, metric=soft_dtw)

# print("Silhouette score:", silhouette_avg)
