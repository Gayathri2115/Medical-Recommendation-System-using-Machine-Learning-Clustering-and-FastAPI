from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


def train_clustering(X_scaled, n_clusters=3):

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    clusters = kmeans.fit_predict(X_scaled)

    nn = NearestNeighbors(n_neighbors=3)

    nn.fit(X_scaled)

    return kmeans, nn, clusters