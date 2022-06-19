import pandas as pd
import requests
import io
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 読み込み
url_red = 'knn.csv'
data_red = pd.read_csv(url_red,
                       header=None, skiprows=1, delimiter=";")
# 赤を0, 白を1とする
data_red['type'] = [0] * data_red.shape[0]
data_red.columns = ['x', 'y']

data_white = pd.read_csv(url_red, header=None, skiprows=1, delimiter=";")
# 赤を0, 白を1とする
data_white['type'] = [1] * data_white.shape[0]
data_white.columns = ['x', 'y']

# 確認
print('データ形式:{}'.format(data_red.shape))
print(data_red.head())
print('データ形式:{}'.format(data_white.shape))
print(data_white.head())
# print(data.dtypes)

# 結合
data = pd.concat([data_red, data_white])
print('データ形式:{}'.format(data.shape))
print(data.head())


# 目的変数、説明変数
X = data[['x', 'y']]
y = data['class']

# 訓練データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

# グラフ描画用
training_accuracy = []
test_accuracy = []
k_range_max = 50

# 学習
for n_neighbors in range(1, k_range_max):
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    training_accuracy.append(model.score(X_train, y_train))
    test_accuracy.append(model.score(X_test, y_test))

# グラフ描画
plt.plot(range(1, k_range_max), training_accuracy, label='Training')
plt.plot(range(1, k_range_max), test_accuracy, label='Test')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.show()