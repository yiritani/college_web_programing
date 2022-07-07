from matplotlib import pyplot as plt
from sklearn import datasets, preprocessing
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# datasetの読み込み
wine_data = datasets.load_wine()
# DataFrameに変換
df = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
print(df.head())
# データの整形
X = df[["alcohol", "color_intensity"]]
print(X)
sc = preprocessing.StandardScaler()
sc.fit(X)
X_norm = sc.transform(X)

# クラスタリング
cls = KMeans(n_clusters=3)
result = cls.fit(X_norm)
# 結果を出力
plt.scatter(X_norm[:, 0], X_norm[:, 1], c=result.labels_)
plt.scatter(result.cluster_centers_[:, 0], result.cluster_centers_[:, 1], s=250, marker='*', c='red')
plt.show()
