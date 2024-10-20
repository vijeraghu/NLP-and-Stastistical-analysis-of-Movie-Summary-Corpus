from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Select relevant features for clustering
features = merged_df[['Box_office_revenue', 'Sentiment_Score']]
features.dropna(inplace=True)  # Drop rows with NaN values

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
merged_df['Cluster'] = kmeans.fit_predict(scaled_features)

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['Box_office_revenue'], merged_df['Sentiment_Score'], c=merged_df['Cluster'], cmap='viridis', marker='o')
plt.title('K-means Clustering of Movies')
plt.xlabel('Box Office Revenue')
plt.ylabel('Sentiment Score')
plt.colorbar(label='Cluster')
plt.grid()
plt.show()
