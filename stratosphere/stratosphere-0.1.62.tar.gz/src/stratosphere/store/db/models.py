from sqlalchemy import Column, LargeBinary, String, BigInteger
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types.uuid import UUIDType
from stratosphere import config

# Construct a base class for declarative class definitions.
Base = declarative_base()

# UUID type, to be used in model definitions. By passing binary=False, we fall back
# to the string representation of UUIDs if there's no native type  (as in SQLite).
uuid_type = UUIDType(binary=False)


class Experiment(Base):
    """Model representing the index record of an experiment in the database."""

    __tablename__ = config.db.experiments_table
    id_experiment = Column(uuid_type, primary_key=True, default=None)
    name = Column(String, nullable=False, unique=True)
    run_count = Column(BigInteger, nullable=False, default=None)
    run_columns = Column(LargeBinary, nullable=True, default=None)
    fields = Column(LargeBinary, nullable=False, default=None)
    properties = Column(LargeBinary, nullable=False, default=None)
    pickle = Column(LargeBinary, nullable=True, default=None)
