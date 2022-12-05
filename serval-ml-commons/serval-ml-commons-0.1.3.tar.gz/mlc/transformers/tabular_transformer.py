import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from mlc.transformers.transformer import Transformer


class TabPreprocessor(Transformer):
    def __init__(self, feature_type, scale, one_hot_encode, **kwargs):
        super().__init__(
            name="tab_preprocessor",
            feature_type=feature_type,
            scale=scale,
            one_hot_encode=one_hot_encode,
            **kwargs,
        )
        self.scale = scale
        self.one_hot_encode = one_hot_encode
        cat = feature_type == "cat"
        self.cat_idx = np.where(cat)[0]
        self.num_idx = np.where(~cat)[0]
        self.std_scaler = StandardScaler()
        self.cat_encoder = OneHotEncoder(
            sparse=False, handle_unknown="ignore", drop="if_binary"
        )
        self.do_scale = (len(self.num_idx) > 0) and scale
        self.do_one_hot_encode = (len(self.cat_idx) > 0) and one_hot_encode

    def fit(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        if self.do_scale:
            self.std_scaler.fit(X[:, self.num_idx])
        if self.do_one_hot_encode:
            self.cat_encoder.fit(X[:, self.cat_idx])

        return self

    def transform(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        X = X.copy()
        if self.do_scale:
            X[:, self.num_idx] = self.std_scaler.transform(X[:, self.num_idx])
        if self.do_one_hot_encode:
            new_x1 = X[:, self.num_idx]
            new_x2 = self.cat_encoder.fit_transform(X[:, self.cat_idx])
            X = np.concatenate([new_x1, new_x2], axis=1)

        return X

    def inverse_transform(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        X = X.copy()
        if self.do_one_hot_encode:
            cat_x = X[:, len(self.num_idx) :]
            cat_x = self.cat_encoder.inverse_transform(cat_x)

            new_x = np.empty((len(X), len(self.num_idx) + len(self.cat_idx)))
            new_x[:, self.num_idx] = X[:, : len(self.num_idx)]
            new_x[:, self.cat_idx] = cat_x
            X = new_x

        if self.do_scale:
            X[:, self.num_idx] = self.std_scaler.inverse_transform(
                X[:, self.num_idx]
            )

        return X

    def load(self, path):
        raise NotImplementedError

    def save(self, path):
        raise NotImplementedError


def get_tab_transformer(metadata, scale, one_hot_encode):
    cat_index = metadata["type"] == "cat"
    cat_features = metadata[cat_index]["feature"]
    num_features = metadata[~cat_index]["feature"]

    transformers = []
    if scale:
        transformers.append(("num", StandardScaler(), num_features))
    if one_hot_encode:
        transformers.append(
            (
                "cat",
                OneHotEncoder(
                    sparse=False, handle_unknown="ignore", drop="if_binary"
                ),
                cat_features,
            )
        )

    return ColumnTransformer(
        transformers=transformers,
        sparse_threshold=0,
        remainder="passthrough",
        n_jobs=-1,
    )


class TabTransformer(Transformer):
    def __init__(self, metadata, scale, one_hot_encode, **kwargs):
        super().__init__(
            name="tab_transformer",
            metadata=metadata,
            scale=scale,
            one_hot_encode=one_hot_encode,
            **kwargs,
        )
        cat_index = metadata["type"] == "cat"
        cat_features = metadata[cat_index]["feature"]
        num_features = metadata[~cat_index]["feature"]

        cat_min = metadata[cat_index]["min"].to_list()
        cat_max = metadata[cat_index]["max"].to_list()
        cat_range = [
            np.arange(int(cat_min[i]), int(cat_max[i]) + 1)
            for i in range(len(cat_min))
        ]
        transformers = []
        if scale:
            transformers.append(("num", StandardScaler(), num_features))
        if one_hot_encode:
            transformers.append(
                (
                    "cat",
                    OneHotEncoder(
                        sparse=False,
                        handle_unknown="ignore",
                        drop="if_binary",
                        categories=cat_range,
                    ),
                    cat_features,
                )
            )
        self.transformer = ColumnTransformer(
            transformers=transformers,
            sparse_threshold=0,
            remainder="passthrough",
            n_jobs=-1,
        )

    def fit(self, X, y=None):
        return self.transformer.fit(X, y)

    def transform(self, X):
        return self.transformer.transform(X)

    def load(self, path):
        self.transformer = joblib.load(path)

    def save(self, path):
        joblib.dump(self.transformer, path)
