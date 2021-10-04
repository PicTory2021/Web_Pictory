import pandas as pd
import numpy as np

# sklearn
from sklearn_extra.cluster import KMedoids
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.model_selection import train_test_split

# 시각화 라이브러리
import matplotlib.pyplot as plt

# 클러스터 개수 파악
from yellowbrick.cluster import SilhouetteVisualizer

# 텐서플로우
# import tensorflow as tf
# from tensorflow.keras.layers import *
# from tensorflow.keras.models import Model
# from tensorflow import keras
#
import random
#
#
# # 데이터프레임이 파라미터
# def preprocessing(origin_matrix):
#     origin_matrix = origin_matrix.fillna(0)
#     data = origin_matrix.values
#     train, test = train_test_split(data, test_size=0.3)
#     return train, test
#
#
# class AutoEncoder:
#     def __init__(self):
#         encoder = 0
#         encoder2 = 0
#         decoder = 0
#         decoder2 = 0
#         autoencoder = 0
#
#     # units = 테스트 해서 결정해야함. 일단 13
#     # epochs = 10
#     # lr = 0.05
#     def make_model(self, train_matrix, units, epochs, lr):
#         self.encoder = keras.models.Sequential([keras.layers.Dense(units=128, input_dim=8000)])
#         self.encoder2 = keras.models.Sequential([keras.layers.Dense(units=units, input_dim=128)])
#
#         self.decoder = keras.models.Sequential([keras.layers.Dense(units=128, input_dim=units)])
#         self.decoder2 = keras.models.Sequential([keras.layers.Dense(units=8000, input_dim=128)])
#
#         self.autoencoder = keras.models.Sequential([self.encoder, self.encoder2, self.decoder, self.decoder2])
#
#         self.autoencoder.compile(loss="mse", optimizer=keras.optimizers.Adam(learning_rate=lr))
#         self.autoencoder.summary()
#
#         history = self.autoencoder.fit(train_matrix, train_matrix, epochs=epochs)
#
#     def calc_reconstruction_err(self, train_matrix):
#         de_pred = self.autoencoder.predict(train_matrix)
#
#         # 각 행별 복원 오차
#         print('이미지 별 복원오차')
#         mse = np.power(de_pred - train_matrix, 2).sum(axis=1) / 8000
#         plt.plot(mse)
#         plt.show()
#
#         print('최대 복원오차')
#         print(mse.max())
#         print('최소 복원오차')
#         print(mse.min())
#
#     def dimension_compression(self, origin_matrix):
#         encoded_matrix = self.encoder.predict(origin_matrix)
#         encoded_matrix = self.encoder2.predict(encoded_matrix)
#         return encoded_matrix
#
#
# class Cluster:
#     def __init__(self):
#         model = 0  # 클러스터링을 수행한 모델
#
#     # random_state: 클러스터링 초기 랜덤값에 대한 시드값 - 초기 값으로 인한 값의 변화를 방지
#     def clustring(self, method, matrix, cluster_level, random_state):
#         if (method == 'k_medoids'):
#             self.model = KMedoids(n_clusters=cluster_level)
#         if (method == 'k_means'):
#             self.model = KMeans(n_clusters=cluster_level, random_state=random_state)
#         if (method == 'dbscan'):
#             self.model = DBSCAN(eps=0.5, min_samples=5)
#         self.model.fit(matrix)
#
#     # 실루엣 계수가 낮을수록 클러스터 내부 값들이 넓게 분포했는 거임.
#
#     # 실루엣 계수를 계산하여 클러스터 개수 판단
#     def calc_silhouette_coefficient(self, encoded_matrix):
#         for i in range(2, 19):
#             tmp_model = self.clustring('k_medoids', encoded_matrix, i, 0)
#
#             # 실루엣 계수 전체 평균
#             average_score = silhouette_score(encoded_matrix, tmp_model.labels_)
#             print('전체 클러스터 실루엣 계수 평균')
#             print(average_score)
#
#             encoded_matrix_df = pd.DataFrame(encoded_matrix)
#             encoded_matrix_df['cluster'] = tmp_model.labels_
#
#             score_samples = silhouette_samples(encoded_matrix, encoded_matrix_df['cluster'])
#             encoded_matrix_df['silhoutte_coeff'] = score_samples
#
#             print('클러스터 별 실루엣 계수')
#             print(encoded_matrix_df.groupby('cluster')['silhoutte_coeff'].mean())
#             print('')
#
#             ## 실루엣 계수를 측정해 클러스터링 성능 평가
#             print('실루엣 계수 시각화')
#             visualizer = SilhouetteVisualizer(tmp_model, colors='yellowbrick')
#             visualizer.fit(encoded_matrix)  # 시각화를 위한 클러스터링
#             visualizer.show()  # 실루엣 계수 시각화
#
#     def matrix_to_csv(self, encoded_matrix):
#         encoded_matrix_df = pd.DataFrame(encoded_matrix)


'''
클러스터 목록은 전역변수로 만들어서 사용할 것
'''


# 랜덤 클러스터에서 6장 사진 id 리턴
def init_select_img():
    selected_cluster_list = random.sample(range(0, cluster_level), cluster_level)
    selected_img_id_list = []
    for i in range(0, len(selected_cluster_list)):

        if len(selected_cluster_list) < 5:
            if i == 0 or i == 1:
                selected_img_id_list.extend(
                    clustered_img_id_df[clustered_img_id_df['cluster'] == selected_cluster_list[i]].sample(n=2)[
                        'id'].values.tolist())
            else:
                selected_img_id_list.extend(
                    clustered_img_id_df[clustered_img_id_df['cluster'] == selected_cluster_list[i]].sample(n=1)[
                        'id'].values.tolist())
        elif len(selected_cluster_list) < 6:
            if i == 0:
                selected_img_id_list.extend(
                    clustered_img_id_df[clustered_img_id_df['cluster'] == selected_cluster_list[i]].sample(n=2)[
                        'id'].values.tolist())
            else:
                selected_img_id_list.extend(
                    clustered_img_id_df[clustered_img_id_df['cluster'] == selected_cluster_list[i]].sample(n=1)[
                        'id'].values.tolist())
        else:
            selected_img_id_list.extend(
                clustered_img_id_df[clustered_img_id_df['cluster'] == selected_cluster_list[i]].sample(n=1)[
                    'id'].values.tolist())
    print(selected_img_id_list)
    return selected_img_id_list


# 1장, 2장 img가 오면 알맞은 6장 추천
def select_img(img_id_list):
    cluster_list = []
    for i in img_id_list:
        cluster_list.append(clustered_img_id_df.loc[i]['cluster'])

    if len(cluster_list) == 1:
        id_list = clustered_img_id_df[
            clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=5)[
            'id'].values.tolist()
        id_list.extend(clustered_img_id_df[clustered_img_id_df['cluster'] != clustered_img_id_df.loc[cluster_list[0]][
            'cluster']].sample(n=1)['id'].values.tolist())
    elif len(cluster_list) == 2:
        if cluster_list[0] == cluster_list[1]:
            id_list = clustered_img_id_df[
                clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=5)[
                'id'].values.tolist()
            id_list.extend(clustered_img_id_df[
                               clustered_img_id_df['cluster'] != clustered_img_id_df.loc[cluster_list[0]][
                                   'cluster']].sample(n=1)['id'].values.tolist())
        else:
            id_list = clustered_img_id_df[
                clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=4)[
                'id'].values.tolist()
            id_list.extend(clustered_img_id_df[
                               clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[1]][
                                   'cluster']].sample(n=1)['id'].values.tolist())
            id_list.extend(clustered_img_id_df.loc[clustered_img_id_df['cluster'].isin(
                set(clustered_img_id_df['cluster'].unique()) - set([cluster_list[0], cluster_list[1]]))].sample(n=1)[
                               'id'].values.tolist())
    return id_list


# 3장 img오면 3장 추천
def recommendation(img_id_list):
    cluster_list = []

    for i in img_id_list:
        cluster_list.append(clustered_img_id_df.loc[i]['cluster'])

    if cluster_list[0] == cluster_list[1] and cluster_list[0] == cluster_list[2] and cluster_list[1] == cluster_list[2]:
        print('all')
        recommendation_id_list = clustered_img_id_df[
            clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=3)[
            'id'].values.tolist()
    elif cluster_list[0] == cluster_list[1] and cluster_list[0] != cluster_list[2]:
        print(2)
        print(cluster_list)
        recommendation_id_list = clustered_img_id_df[
            clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=2)[
            'id'].values.tolist()
        recommendation_id_list.extend(clustered_img_id_df[
                                          clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[2]][
                                              'cluster']].sample(n=1)['id'].values.tolist())
    elif cluster_list[0] == cluster_list[2] and cluster_list[0] != cluster_list[1]:
        print(3)
        print(cluster_list)
        recommendation_id_list = clustered_img_id_df[
            clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=2)[
            'id'].values.tolist()
        recommendation_id_list.extend(clustered_img_id_df[
                                          clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[1]][
                                              'cluster']].sample(n=1)['id'].values.tolist())
    elif cluster_list[1] == cluster_list[2] and cluster_list[1] != cluster_list[0]:
        print(4)
        print(cluster_list)
        recommendation_id_list = clustered_img_id_df[
            clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[1]]['cluster']].sample(n=2)[
            'id'].values.tolist()
        recommendation_id_list.extend(clustered_img_id_df[
                                          clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]][
                                              'cluster']].sample(n=1)['id'].values.tolist())
    else:
        print(5)
        print(cluster_list)
        recommendation_id_list = clustered_img_id_df[
            clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[0]]['cluster']].sample(n=1)[
            'id'].values.tolist()
        recommendation_id_list.extend(clustered_img_id_df[
                                          clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[1]][
                                              'cluster']].sample(n=1)['id'].values.tolist())
        recommendation_id_list.extend(clustered_img_id_df[
                                          clustered_img_id_df['cluster'] == clustered_img_id_df.loc[cluster_list[2]][
                                              'cluster']].sample(n=1)['id'].values.tolist())

    return recommendation_id_list


## 테스트용 코드 ##

# df_list = np.random.rand(20000, 8000)
# df_list = pd.DataFrame(df_list)
# df_list = df_list[df_list<0.3]
#
#
# train_matrix, test_matrix = preprocessing(df_list)
# print(train_matrix.shape)
# print(test_matrix.shape)
# ae = AutoEncoder()
# clt = Cluster()
# ae.make_model(train_matrix, 3, 10, 0.05)
# ae.calc_reconstruction_err(train_matrix)
# encoded_matrix = ae.dimension_compression(test_matrix)
# print(encoded_matrix)
# clt.clustring('k_medoids', encoded_matrix, 5, 21)
#
# encoded_matrix_df = pd.DataFrame(encoded_matrix)
# encoded_matrix_df['cluster'] = clt.model.labels_
# encoded_matrix_df['id'] = range(0,6000)
# matrix_df_csv = encoded_matrix_df[['cluster','id']]
# matrix_df_csv.to_csv('clustered_img_id.csv',index = False)

clustered_img_id_df = pd.read_csv('./clustered_img_id.csv')
cluster_level = 5