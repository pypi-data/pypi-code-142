import pandas as pd
import recmetrics
import numpy as np
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
import implicit
from tqdm.notebook import tqdm
from sklearn.neighbors import NearestNeighbors
from mydata import CSV, Exel, Dat


def apk(actual, predicted, k=10):
    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    if not actual:
        return 0.0

    return score / min(len(actual), k)


def mapk(actual, predicted, k=10):
    return np.mean([apk(a, p, k) for a, p in zip(actual, predicted)])


def get_users_predictions(user_id, n, model):
    recommended_items = pd.DataFrame(model.loc[user_id])
    recommended_items.columns = ["predicted_rating"]
    recommended_items = recommended_items.sort_values('predicted_rating', ascending=False)
    recommended_items = recommended_items.head(n)
    return recommended_items.index.tolist()


def recommend_system(user_data, item_data, user_col='userId', item_col='movieId', rating_col='rating',
                     search_word='Matrix', count_recom=10,
                     type_of_data='csv', user_id=14):
    if type_of_data == 'csv':
        csr_matrix, ratings_, items_, user_item_matrix = CSV(user_data, item_data).to_csr(
            user_col='userId', item_col='movieId', rating_col='rating')

    elif type_of_data == 'exel':
        csr_matrix, ratings_, items_, user_item_matrix = Exel(
            user_data, item_data).to_csr(user_col='userId', item_col='movieId', rating_col='rating')

    elif type_of_data == 'dat':
        csr_matrix, ratings_, items_, user_item_matrix = Dat(user_data, item_data).to_csr(
            user_col='userId', item_col='movieId', rating_col='rating', separator=':')

    print('---------------------------------------------NearestNeighbors---------------------------------------------')
    knn = NearestNeighbors(metric='cosine', algorithm='brute',
                           n_neighbors=20, n_jobs=-1)

    knn.fit(csr_matrix)

    user_item_matrix = user_item_matrix.rename_axis(None, axis=1).reset_index()

    item_search = items_[items_['title'].str.contains(search_word)]
    item_id = item_search.iloc[0][item_col]
    item_id = user_item_matrix[user_item_matrix[item_col] == item_id].index[0]

    distances, indices = knn.kneighbors(
        csr_matrix[item_id], n_neighbors=count_recom + 1)

    indices_list = indices.squeeze().tolist()
    distances_list = distances.squeeze().tolist()

    indices_distances = list(zip(indices_list, distances_list))

    indices_distances_sort = sorted(
        indices_distances, key=lambda x: x[1], reverse=True)
    indices_distances_sort = indices_distances_sort[:-1]

    rec_list = []

    for ind_dist in tqdm(indices_distances_sort):
        matrix_movie_id = user_item_matrix.iloc[ind_dist[0]][item_col]
        id = items_[items_[item_col] == matrix_movie_id].index
        title = items_.iloc[id]['title'].values[0]
        dist = ind_dist[1]
        rec_list.append({'Title': title, 'Distance': dist})

    rec_df = pd.DataFrame(rec_list, index=range(1, count_recom + 1))
    print(rec_df.head(10))

    # Als
    print('---------------------------------------------ALS---------------------------------------------------------')
    model = implicit.als.AlternatingLeastSquares(
        factors=30, regularization=0.1, iterations=16)

    model.fit(csr_matrix)

    recommended = model.recommend(user_id,
                                  csr_matrix[user_id],
                                  N=count_recom,
                                  filter_already_liked_items=False,
                                  recalculate_user=True)

    rec_list_ALS = []
    index = 0

    for ind_dist in tqdm(recommended[0]):
        matrix_movie_id = user_item_matrix.iloc[ind_dist][item_col]
        id = items_[items_[item_col] == matrix_movie_id].index
        title = items_.iloc[id]['title'].values[0]
        rec = round(recommended[1][index] * 100, 2)
        index += 1
        rec_list_ALS.append({'Title': title, 'Rec (%)': rec})

    rec_df_ALS = pd.DataFrame(rec_list_ALS)
    print(rec_df_ALS.head(10))

    id_movie_user = ratings_[ratings_[user_col] == user_id].index.to_list()
    mov = [int(ratings_.iloc[i][item_col]) for i in id_movie_user][:count_recom]
    k1 = []
    for K in np.arange(1, count_recom + 1):
        k1.extend([recmetrics.mark([mov], [recommended[0]], k=K)])
    print('MARK: ', np.mean(k1))

    k2 = []
    for K in np.arange(1, count_recom + 1):
        k2.extend([mapk([mov], [recommended[0]], k=K)])
    print('MAP: ', np.mean(k2))

    # SVD
    print('---------------------------------------------SVD---------------------------------------------------------')
    reader = Reader(rating_scale=(0, 5))
    data = Dataset.load_from_df(ratings_[[user_col, item_col, rating_col]], reader)
    trainset, testset = train_test_split(data, test_size=0.25)

    algo = SVD()
    algo.fit(trainset)

    test = algo.test(testset)
    test = pd.DataFrame(test)
    test.drop('details', inplace=True, axis=1)
    test.columns = [user_col, item_col, 'actual', 'cf_predictions']

    print(f'MSE: {recmetrics.mse(test.actual / 5, test.cf_predictions / 5)}')
    print(f'RMSE: {recmetrics.rmse(test.actual / 5, test.cf_predictions / 5)}')

    cf_model = test.pivot_table(index=user_col, columns=item_col, values='cf_predictions').fillna(0)

    get_users_predictions(user_id, count_recom, cf_model)

    test = test.copy().groupby(user_col, as_index=False)[item_col].agg({'actual': (lambda x: list(set(x)))})
    test = test.set_index(user_col)
    cf_recs = [] = []
    for user in test.index:
        cf_predictions = get_users_predictions(user, 10, cf_model)
        cf_recs.append(cf_predictions)

    test['cf_predictions'] = cf_recs
    actual = test.actual.values.tolist()
    cf_predictions = test.cf_predictions.values.tolist()

    cf_mark = []
    for K in np.arange(1, 11):
        cf_mark.extend([recmetrics.mark(actual, cf_predictions, k=K)])
    print('MARK: ', np.mean(cf_mark))

    cf_map = []
    for K in np.arange(1, 11):
        cf_mark.extend([mapk(actual, cf_predictions, k=K)])
    print('MAP: ', np.mean(cf_mark))


file_item = 'movies.csv'
file_user = 'ratings.csv'
recommend_system(file_user, file_item)
