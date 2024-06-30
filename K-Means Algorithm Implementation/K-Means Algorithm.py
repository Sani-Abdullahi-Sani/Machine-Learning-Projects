import numpy as np

dataset = np.array([
    [0.22, 0.33], [0.45, 0.76], [0.73, 0.39], [0.25, 0.35], [0.51, 0.69], 
    [0.69, 0.42], [0.41, 0.49], [0.15, 0.29], [0.81, 0.32], [0.50, 0.88], 
    [0.23, 0.31], [0.77, 0.30], [0.56, 0.75], [0.11, 0.38], [0.81, 0.33], 
    [0.59, 0.77], [0.10, 0.89], [0.55, 0.09], [0.75, 0.35], [0.44, 0.55]
])

number_of_cluster_k = 3

initial_centers = []
for i in range(3): 
    x = float(input())
    y = float(input())
    initial_centers.append([x, y])

centers = np.array(initial_centers)

cluster_assignments = np.zeros(len(dataset))

def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

#initial_centers = [
#   (0.45, 0.55),  # Initial center for cluster 1
#   (0.70, 0.71),  # Initial center for cluster 2
#   (0.11, 0.67)   # Initial center for cluster 3
#]

while True:
    # Here, we assign each data point to the nearest cluster center.
    distances = np.sqrt(np.sum((dataset - centers[:, np.newaxis]) ** 2, axis=2))
    cluster_assignments = np.argmin(distances, axis=0)

    # this is where the update of cluster centers happen
    cluster_sums = np.array([dataset[cluster_assignments == j].sum(axis=0) for j in range(number_of_cluster_k)])
    cluster_counts = np.array([np.sum(cluster_assignments == j) for j in range(number_of_cluster_k)])
    new_centers = cluster_sums / cluster_counts[:, np.newaxis]

    if np.allclose(new_centers, centers):
        break

    # Here, we try removing empty clusters after the update.
    non_empty_clusters = [i for i in range(number_of_cluster_k) if cluster_counts[i] > 0]
    centers = new_centers[non_empty_clusters]
    number_of_cluster_k = len(centers)

# sum-of-squares error
error = 0
for j in range(number_of_cluster_k):
    cluster_points = dataset[cluster_assignments == j]
    error += np.sum([distance(point, centers[j]) ** 2 for point in cluster_points])

print(round(error, 4))