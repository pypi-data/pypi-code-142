import logging
import os
from uuid import UUID

import pandas as pd

from motor.models import FileMapModel
from motor.models import FileType
from motor.models import RawFileModel
from motor.models import RecommendationsModel
from motor.models import UserRating
from server.config import basedir
from server.database import db


logger = logging.getLogger(__name__)


def load_file(organization_id: UUID, file_type: str):
    raw_file = RawFileModel.query.filter_by(
        organization_id=organization_id, file_type=file_type
    ).first()
    with open(
        os.path.join(basedir + f"uploads/{organization_id}", raw_file.filename), "r"
    ) as file:
        return (
            pd.read_csv(file),
            FileMapModel.query.filter_by(file_id=raw_file.id).first(),
        )


def load_ratings(user_uid: UUID):
    ratings = UserRating.query.filter_by(user_id=user_uid).all()
    ratings_list = [i.__dict__ for i in ratings]
    return pd.DataFrame.from_dict(ratings_list)


def process_main_file(organization_id: UUID):
    file_data_frame, file_map = load_file(
        organization_id=organization_id, file_type=FileType.DATA.value
    )

    # for this example we will remove the extra spaces
    file_data_frame[file_map.title_column] = file_data_frame[
        file_map.title_column
    ].apply(lambda x: x.strip())
    # this 'for' runs only one hardcoded column but was kept here in order to work when this will be dynamic
    for column in file_map.data_columns:
        file_data_frame[column] = file_data_frame.loc[:, column].str.split(
            file_map.data_separator
        )

    # from now on will work in a copy of the df
    df_splitted_columns = file_data_frame.copy()

    # Para cada fila del marco de datos, iterar la lista de géneros y colocar un 1 en la columna que corresponda
    for index, row in file_data_frame.iterrows():
        for data_column in file_map.data_columns:
            for column in row[data_column]:
                df_splitted_columns.at[index, column] = 1

    # Completar los valores NaN con 0 para mostrar que una película no tiene el género de la columna
    return df_splitted_columns.fillna(0), file_data_frame, file_map


def main(user_uid: UUID, organization_id: UUID):
    # file_uid = UUID("26012b8d-544a-4b1b-b23d-5af825d6a8a8")
    df_splitted_columns, file_data_frame, file_map = process_main_file(
        organization_id=organization_id
    )

    # Guardando la información del usuario dentro del marco de datos pandas
    ratings_df, _ = load_file(
        organization_id=organization_id, file_type=FileType.RATINGS.value
    )
    # La sentencia Drop elimina la fila o columna señalada del marco de datos
    ratings_df = ratings_df.drop(labels="timestamp", axis=1)

    # user_uid = UUID("26012b8d-544a-4b1b-b23d-5af825d6a8a9")
    inputMovies = load_ratings(user_uid=user_uid)

    # Filtrar las películas por título
    inputId = df_splitted_columns[
        df_splitted_columns[file_map.title_column].isin(
            inputMovies[file_map.title_column].tolist()
        )
    ]

    # Luego juntarlas para obtener el movieId. Implícitamente, lo está uniendo por título.
    inputMovies = pd.merge(inputId, inputMovies)

    # Eliminando información que no utilizaremos del dataframe de entrada
    inputMovies = inputMovies.drop(
        labels=["user_id", "_sa_instance_state", "id"], axis=1
    )
    for column in file_map.data_columns:
        inputMovies = inputMovies.drop(labels=column, axis=1)

    # Dataframe de entrada final
    # Si una película que se agregó no se encuentra, entonces podría no estar en el dataframe
    # original o podría estar escrito de otra forma, por favor revisar mayúscula o minúscula.
    # Descartando las películas de la entrada de datos
    userMovies = df_splitted_columns[
        df_splitted_columns[file_map.id_column].isin(
            inputMovies[file_map.id_column].tolist()
        )
    ]
    # Inicializando el índice para evitar problemas a futuro
    userMovies = userMovies.reset_index(drop=True)
    # Eliminando problemas innecesarios para ahorrar memoria y evitar conflictos
    userGenreTable = userMovies.drop(labels=file_map.id_column, axis=1).drop(
        labels=file_map.title_column, axis=1
    )
    for column in file_map.data_columns:
        userGenreTable = userGenreTable.drop(labels=column, axis=1)

    try:
        userProfile = userGenreTable.transpose().dot(inputMovies["rating"])
    except ValueError as exception:
        logger.error(
            f"error processing data: user data is malformed. {user_uid=}, {exception=} "
        )
        return
    # Ahora llevemos los géneros de cada película al marco de datos original
    genreTable = df_splitted_columns.set_index(df_splitted_columns[file_map.id_column])
    # Y eliminemos información innecesaria
    genreTable = genreTable.drop(labels=file_map.id_column, axis=1).drop(
        labels=file_map.title_column, axis=1
    )
    for column in file_map.data_columns:
        genreTable = genreTable.drop(labels=column, axis=1)
    # Multiplicando los géneros por los pesos para luego calcular el peso promedio # porque? como funciona?
    recommendationTable_df = ((genreTable * userProfile).sum(axis=1)) / (
        userProfile.sum()
    )
    # Ordena nuestra recomendación en orden descendente
    recommendationTable_df = recommendationTable_df.sort_values(ascending=False)
    # Tabla de recomendaciones final
    recommendations = file_data_frame.loc[
        file_data_frame[file_map.id_column].isin(recommendationTable_df.head(10).keys())
    ]
    recommendations = RecommendationsModel(
        user_id=user_uid,
        organization_id=organization_id,
        recommendations=recommendations.to_json(orient="records"),
    )
    db.session.add(recommendations)
    db.session.commit()
