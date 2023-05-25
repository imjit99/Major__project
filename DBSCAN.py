import numpy as np
from sklearn.cluster import DBSCAN
from Constant.constant import *
from sklearn.preprocessing import StandardScaler

# Convert list_1 to a numpy array
data = np.array(list_1)

# Scale the data for better clustering performance
scaler = StandardScaler()
data = scaler.fit_transform(data)

# Set the DBSCAN parameters
epsilon = 5  # Adjust the value as needed
min_samples = 5  # Adjust the value as needed

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
labels = dbscan.fit_predict(data)

# Print the cluster labels
print(labels)