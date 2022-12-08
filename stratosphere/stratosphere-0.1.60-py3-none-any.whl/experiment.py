import logging
import random
from functools import partial
from typing import Callable, List, Union

import joblib
import pandas as pd
from sqlalchemy.orm import load_only
from stratosphere import config
from stratosphere.job import Job
from stratosphere.run import Run, Runs, normalize_funcs
from stratosphere.store import serialization
from stratosphere.store.db import models
from stratosphere.store.db.database import Database, next_ulid, pandas_query, sanitize_table_name
from stratosphere.store.frames import reorder_columns
from stratosphere.utils import log
from stratosphere.utils.enums import IfExists, enforce_enum
from stratosphere.utils.environment import get_environment


class PickleNotFoundException(Exception):
    def __init__(self):
        self.message = "The pickle blob was not found."
        super().__init__(self.message)


class RunException(Exception):
    """Raised if there's a failure during the execution of functions on runs."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ExperimentAlreadyExists(Exception):
    """Exception to handle the attempt to add one more experiment with the same name."""

    def __init__(self, name):
        self.message = f"Experiment '{name}' already existing, use if_exists=\"replace\" to overwrite it."
        super().__init__(self.message)


class ExperimentNotFoundException(Exception):
    """Exception raised if the experiment is not found."""

    def __init__(self, name):
        self.message = f"Experiment '{name}' not found. List with .ls() the available experiments."
        super().__init__(self.message)


class Experiment:
    """This class represents a new experiment.

    Raises:
        ExperimentNotFoundException: Raised if we try to use a non-existing experiment.
        ExperimentAlreadyExists: Raised if the experiment name is already present.

    Returns:
        Experiment: A defined experiment, ready to be executed, tracked, stored, queried.
    """

    # model_cls is the SQLAlchemy model mapped to this class.
    model_cls = models.Experiment

    def __init__(
        self,
        db: Database = None,
        id_experiment: str = None,
        name: str = None,
        funcs: Union[Callable, List[Callable]] = None,
        kwargs: dict = None,
        fields: dict = None,
        properties: dict = None,
        param_grid: List = None,
        runs: List[Run] = None,
    ):
        """Create a new experiment.

        Args:
            db (Database, optional): Database to link to. Defaults to None.
            id_experiment (str, optional): ID of the experiment to be used. Defaults to None.
            name (str, optional): Name of the experiment. Defaults to None.
            funcs (Union[Callable, List[Callable]], optional): One or more functions to call. Defaults to None.
            kwargs (dict, optional): Fixed parameters passed to the functions. Defaults to None.
            fields (dict, optional): Fixed experiment fields to be tracked. Defaults to None.
            properties (dict, optional): Experiment properties, used to hold meta-attributes. Defaults to None.
            param_grid (List, optional): Grid of parameters, used to generate the run parameters.
            runs (List[Run], optional): List of runs belonging to the experiment. Defaults to None.
        """

        self.db = db
        self.id_experiment = next_ulid() if id_experiment is None else id_experiment
        self.name = name
        self.funcs = normalize_funcs(funcs)
        self.kwargs = {} if kwargs is None else kwargs
        self.fields = {} if fields is None else fields

        # Populate properties
        self.properties = {} if properties is None else properties
        if "env" not in self.properties:
            # If the experiment is loaded, then "env" is already populated and we retain it.
            self.properties["env"] = get_environment()

        # Populate param_grid
        self.param_grid = [{}] if (param_grid is None or param_grid == []) else param_grid
        if isinstance(self.param_grid, dict):
            self.param_grid = [self.param_grid]

        self.runs = Runs(runs)

    def __reduce__(self):
        """
        Make the expriment pickable, avoiding unpickable objects in SQLAlchemy.

        Returns:
            Experiment: An unpickled Experiment object.
        """
        return self.__class__, (
            None,
            self.id_experiment,
            self.name,
            self.funcs,
            self.kwargs,
            self.fields,
            self.properties,
            self.param_grid,
            self.runs,
        )

    def table_name(self) -> str:
        """Return the table name of the experiment

        Returns:
            str: Table name
        """

        return sanitize_table_name(f"{config.db.experiment_table_prefix}{self.name}")

    @log.default_exception_handler
    def query(self, query: str = "SELECT * FROM {table_name}", verbose: bool = False) -> pd.DataFrame:
        """Query the experiment's table

        Args:
            query (str, optional): SQL query. {e} is replaced with the table name of the experiment.,
            {id} with the experiment ID, and {ee} with the experiments table. Defaults to the complete record.
            verbose (bool, optional): If true, print the resulting query. Defaults to False.

        Returns:
            pd.DataFrame: Result of the query.
        """

        df = self.db.pandas(
            query.format(
                id=f"'{self.id_experiment}'",
                table_name=self.table_name(),
                experiments_table=config.db.experiments_table,
                name=f"'{self.name}'",
            ),
            verbose=verbose,
        )

        return df

    def load_runs(self, run_columns):
        logging.info("Loading runs")
        # Retrieve all columns
        df = self.query(f"select * from {self.table_name()}")

        # Take care of deserialization
        for col_name in run_columns["serialized"]:
            df[col_name] = df[col_name].map(serialization.deserialize)

        # Reconstruct fields
        def series_to_run(row: pd.Series):
            fields = row[run_columns["serialized"] + run_columns["non_serialized"]].to_dict()
            run = Run(id_run=row["id_run"], fields=fields)
            return run

        self.runs = Runs(df.apply(lambda row: series_to_run(row), axis=1).values)

    @classmethod
    def load_pickle(cls, db: Database, name: str):
        logging.info(f"Loading experiment '{name}' (pickle)")

        with db.session() as session:
            record = (
                session.query(cls.model_cls)
                .options(load_only(Experiment.model_cls.pickle))
                .filter_by(name=name)
                .first()
            )

            if record is None:
                raise ExperimentNotFoundException(name)
            # Unpicke the serialized object.

            if record.pickle is None:
                raise PickleNotFoundException()

            experiment = serialization.pickle_loads(record.pickle)
            # Set the db of the experiment. Pickled db instances are never re-instantiated
            # completely, this let us reuse the existing database instance. See the Database
            # class for more comments on this.
            #
            # Important: this let us use SQLite memory databases, as only one instance is
            # used on all experiments.
            experiment.db = db
            return experiment

    @classmethod
    def load(cls, db: Database, name: str, pickle=False):
        """Load an experiment from database.

        Args:
            db (Database): Reference to a database.
            name (str): Name of the experiment.

        Raises:
            ExperimentNotFoundException: Raised if the experiment is not found.

        Returns:
            Experiment: Loaded experiment.
        """

        if pickle:
            return cls.load_pickle(db, name)

        logging.info(f"Loading experiment '{name}' (json-serialized)")

        # Create a new session
        columns = [
            Experiment.model_cls.id_experiment,
            Experiment.model_cls.id_experiment,
            Experiment.model_cls.name,
            Experiment.model_cls.run_count,
            Experiment.model_cls.run_columns,
            Experiment.model_cls.fields,
            Experiment.model_cls.properties,
            Experiment.model_cls.id_experiment,
        ]

        with db.session() as session:
            record = session.query(cls.model_cls).options(load_only(*columns)).filter_by(name=name).first()

            # If the record is not found, raise an error.
            if record is None:
                raise ExperimentNotFoundException(name)

            # Load the experiment from the record in "experiments" table.
            experiment = Experiment(
                db=db,
                id_experiment=record.id_experiment,
                name=record.name,
                fields=serialization.deserialize(record.fields),
                properties=serialization.deserialize(record.properties),
            )

            if record.run_count > 0:
                experiment.load_runs(run_columns=serialization.deserialize(record.run_columns))

            return experiment

    @log.default_exception_handler
    def execute(
        self,
        funcs: Union[Callable, List[Callable]] = None,
        backend=joblib.parallel.DEFAULT_BACKEND,
        n_jobs=-1,
    ):
        """Execute the experiment, then retuning it.

        Args:
            funcs (Union[Callable, List[Callable]], optional): Function(s) that will override the defined ones.
            If the value is "all", the re-evaluation of all defined functions is forced. Defaults to None.
            backend (_type_, optional): Joblib baackend. Defaults to joblib.parallel.DEFAULT_BACKEND.
            n_jobs (int, optional): Parallelization degree, defined as in Joblib. Defaults to -1.

        Returns:
            Run: the same experiment, ready for chained operations.
        """

        # Randomize the order of the runs to execute.
        random.shuffle(self.param_grid)

        if not self.runs:
            # First execution: create runs and execute them.
            # If more functions are passed, we append them for execution.
            tasks = [
                partial(
                    lambda run: run.execute(funcs=funcs),
                    Run(kwargs=self.kwargs, params=params, funcs=self.funcs),
                )
                for params in self.param_grid
            ]
        else:
            tasks = [
                partial(
                    lambda run: run.execute(funcs=funcs),
                    run,
                )
                for run in self.runs.values()
            ]

        if len(tasks) > 0:
            self.runs = Runs(Job(tasks, n_jobs=n_jobs, backend=backend).execute())

        # Check for exceptions, and report them if any.
        for run in self.runs.values():
            if run.exception is not None:
                raise RunException(run.exception)

        # If the execution is successful, we update the tracked environment.
        self.properties["env"] = get_environment()

        return self

    def record(
        self,
        run_columns=None,
        store_pickle=config.serialization.store_pickle,
        enable_compression=config.serialization.enable_compression,
    ) -> models.Experiment:
        """Build an SQLAlchemy ORM object from the existing Experiment object.

        Returns:
            models.Experiment: SQLAlchemy ORM object.
        """

        return self.model_cls(
            id_experiment=self.id_experiment,
            name=self.name,
            fields=serialization.serialize(self.fields, enable_compression=enable_compression),
            properties=serialization.serialize(self.properties, enable_compression=enable_compression),
            pickle=serialization.pickle_dumps(self) if store_pickle else None,
            run_count=len(self.runs),
            run_columns=serialization.serialize(run_columns, enable_compression=enable_compression),
        )

    def info(self):
        """Print some stats about the experiment.

        Returns:
            Experiment: self
        """
        logging.info("Experiment info")
        logging.info(f"  id...............: {self.id_experiment}")
        logging.info(f"  name.............: '{self.name}'")
        logging.info(f"  funcs............: {[func.__name__ for func in self.funcs]}")
        logging.info(f"  kwargs...........: {list(self.kwargs.keys())}")

        logging.info(f"  param_grid...: {list(self.param_grid[0].keys())} ({len(self.param_grid)})")

        logging.info(f"  fields...........: {list(self.fields.keys())}")
        logging.info(f"  size (Mb)........: {self.size('mb')} (compressed)")
        logging.info(f"  table name.......: {self.table_name()}")

        return self

    @log.default_exception_handler
    def persist(
        self,
        if_exists: IfExists = IfExists["fail"],
        store_pickle=config.serialization.store_pickle,
        enable_compression=config.serialization.enable_compression,
    ):
        """Persist the experiment.

        Args:
            if_exists (IfExists, optional): Either "replace" or "fail". Defaults to "fail".

        Raises:
            ExperimentReadOnlyException: Experiment loaded in SQL read-only mode.

        Returns:
            _type_: self.
        """

        logging.info(f"Persisting experiment (table name: {self.table_name()})")

        if_exists = enforce_enum(if_exists, IfExists)

        # Delete record and table of experiment, honoring if_exists.
        self.delete(if_exists)

        if self.runs:
            # The experiment has runs, let's find out the columns definition and persist it with the experiment.
            df_runs = self.runs.df(max_level=0)
            df_runs["id_experiment"] = self.id_experiment
            df_runs, run_columns = serialization.serialize_df(
                df_runs, ignore_columns=["id_run", "id_experiment"], enable_compression=enable_compression
            )
            df_runs = reorder_columns(df_runs, ["id_experiment", "id_run"])
        else:
            run_columns = None

        # Insert row in "experiments" table.
        with self.db.session() as session:
            session.add(
                self.record(run_columns=run_columns, store_pickle=store_pickle, enable_compression=enable_compression)
            )
            session.commit()

        if not self.runs:
            # This experiment has no runs, so we're done.
            return self

        dtype = {
            **{"id_run": models.uuid_type},
            **{"id_experiment": models.uuid_type},
            **{col_name: models.LargeBinary for col_name in run_columns["serialized"]},
        }

        # Create the experiment table.
        self.db.pandas_to_sql(df_runs, self.table_name(), if_exists.name, dtype=dtype)

        return self

    @log.default_exception_handler
    def delete(self, if_exists: IfExists = IfExists["fail"]) -> None:
        """Delete the expeirment.

        Args:
            if_exists (IfExists, optional): Either "replace" or "fail". In case
            the experiment exists and the value is "replace", nothing happens.
            If the experiment exists and the value is "fail", it will raise an
            exception. It is designed to work correctly together with insertions.
            Defaults to "fail".

        Raises:
            ExperimentAlreadyExists: Raised if the experiment exists.
        """

        if_exists = enforce_enum(if_exists, IfExists)

        # Create a new session
        with self.db.session() as session:
            # If we find the record ...
            if session.query(self.model_cls).filter_by(name=self.name).count() > 0:
                # And we are fine deleting it, proceed.
                if if_exists == IfExists["replace"]:
                    # We filter on matching experiment names, as these are the ones that might result
                    # in conflicts, since they must be unique.
                    session.query(Experiment.model_cls).filter(Experiment.model_cls.name == self.name).delete()
                else:
                    # Otherwise, raise an exception.
                    raise ExperimentAlreadyExists(self.name)
            session.commit()

        # We also need to drop the experiment table.
        self.db.drop_table(self.table_name())

    def df(self, max_level=None) -> pd.DataFrame:
        """Returns a Pandas dataframe representing the experiment, including
        parameters and fields. The processing does not depend on
        database queries, but the returned dataframe matches the contents
        of the experiment table (which is generated using this method).

        In presence of overlapping column names from the fixed fields
        of the experiment and the run fields, the fields use
        "_run" as suffix.

        Args:
            include_experiment (bool, optional): If False, do not include the
            fixed experiment fields (it will be a constant column).
            Defaults to True.

        Raises:
            ExperimentReadOnlyException: Experiment loaded in SQL read-only mode.

        Returns:
            pd.DataFrame: Pandas dataframe representing the tracked properties.
        """

        df_experiment = pd.json_normalize(
            {
                **self.fields,
                **{"id_experiment": self.id_experiment, "name": self.name},
            },
            max_level=max_level,
        )

        return reorder_columns(df_experiment, ["id_experiment", "name"])

    def size(self, unit: str = "b") -> int:
        """Return the size of the pickled version of the expeirment.

        Args:
            unit (str, optional): Unit of measure: "b" (Bytes), "kb" (KiloBytes), "mb" (MegaBytes). Defaults to "b".

        Returns:
            int: Size of the experiment once pickled.
        """
        return serialization.pickle_size(self, unit=unit)

    @classmethod
    def ls(cls, db: Database, include_properties=False) -> pd.DataFrame:
        """List experiments in a database.

        Args:
            db (Database): Database instance.

        Returns:
            pd.DataFrame: List of experiments.
        """

        # Construct list of columns to retrieve
        if include_properties:
            columns = [Experiment.model_cls.id_experiment, Experiment.model_cls.name, Experiment.model_cls.properties]
        else:
            columns = [Experiment.model_cls.id_experiment, Experiment.model_cls.name]

        with db.session() as session:
            df_experiments = pandas_query(
                session.query(Experiment.model_cls).options(load_only(*columns)),
                session,
            )

            df_experiments["table_name"] = df_experiments["name"].apply(
                lambda name: sanitize_table_name(f"{config.db.experiment_table_prefix}{name}")
            )

            if include_properties:
                df_experiments["properties"] = df_experiments["properties"].map(serialization.deserialize)
                df_experiments = serialization.explode_json_column(df_experiments, col_name="properties")

            return df_experiments
