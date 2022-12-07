from abc import ABC, abstractmethod
from scipy import sparse as sp
import pandas as pd


class Parser(ABC):

    @abstractmethod
    def to_csr(self, ratings, items, user_col='userId', item_col='movieId', rating_col='rating'):

        for col in ratings.columns:
            if col not in [user_col, 'title', rating_col, item_col]:
                ratings.drop([col], axis=1, inplace=True)

        for col in items.columns:
            if col not in [user_col, 'title', rating_col, item_col]:
                items.drop([col], axis=1, inplace=True)

        user_item_matrix = ratings.pivot_table(
            index=item_col, columns=user_col, values=rating_col)
        user_item_matrix.fillna(0, inplace=True)

        user_votes = ratings.groupby(user_col)[rating_col].agg('count')
        item_votes = ratings.groupby(item_col)[rating_col].agg('count')

        user_mask = user_votes[user_votes > 50].index
        item_mask = item_votes[item_votes > 50].index

        user_item_matrix = user_item_matrix.loc[item_mask, :]
        user_item_matrix = user_item_matrix.loc[:, user_mask]

        return sp.csr_matrix(user_item_matrix.values), ratings, items, user_item_matrix


class CSV(Parser):
    def __init__(self, ratings, items):
        self.ratings = ratings
        self.items = items

    def to_csr(self, user_col='userId', item_col='movieId', rating_col='rating'):
        ratings_file = pd.read_csv(self.ratings)
        items_file = pd.read_csv(self.items)
        return super().to_csr(ratings_file, items_file, user_col, item_col, rating_col)


class Exel(Parser):
    def __init__(self, ratings, items):
        self.ratings = ratings
        self.items = items

    def to_csr(self, user_col='userId', item_col='movieId', rating_col='rating'):
        ratings_file = pd.read_exel(self.ratings)
        items_file = pd.read_exel(self.items)
        return super().to_csr(ratings_file, items_file, user_col, item_col, rating_col)


class Dat(Parser):
    def __init__(self, ratings, items):
        self.ratings = ratings
        self.items = items

    def to_csr(self, user_col='userId', item_col='movieId', rating_col='rating', separator=':'):
        ratings_file = pd.read_csv(self.ratings)
        for c in ratings_file.columns.values:
            ratings_file[c] = ratings_file[c].apply(
                lambda x: float(str(x).split(separator)[1]))

        items_file = pd.read_csv(self.items)
        for c in items_file.columns.values:
            items_file[c] = items_file[c].apply(
                lambda x: float(str(x).split(separator)[1]))
        return super().to_csr(ratings_file, items_file, user_col, item_col, rating_col)
