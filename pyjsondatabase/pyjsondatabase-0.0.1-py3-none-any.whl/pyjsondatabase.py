import pickle
import os


class DataBase:

    def __init__(self, db_path: str) -> None:
        """Create object with database instance"""

        self.__db_path = db_path.strip() if db_path.endswith(".jdb") else db_path.strip() + ".jdb"

        # Create database file if it's doesn't exist
        try:

            if not os.path.exists(self.__db_path):

                with open(self.__db_path, "wb") as file:
                    pickle.dump({}, file)

        except Exception:
            print(f"Could not create database file: {self.__db_path}")

    def __getitem__(self, key):
        """Index oprerator overload"""

        with open(self.__db_path, "rb") as file:
            current_db = pickle.load(file)

        return current_db[key]

    def reinit(self, new_db_path: str, remove_previous: bool = False) -> None:
        """Update path to database"""

        new_db_path = new_db_path.strip() if new_db_path.endswith(".jdb") else new_db_path.strip() + ".jdb"

        # Create database file if it's doesn't exist
        try:

            if not os.path.exists(new_db_path):

                with open(self.__db_path, "wb") as file:
                    pickle.dump({}, file)

                # Delete previous database
                os.remove(self.__db_path) if remove_previous else None
                self.__db_path = new_db_path

        except Exception:
            print(f"Could not reinitialize database file: {new_db_path}")

    def get_fields(self) -> list:
        """Get all filds of database"""

        with open(self.__db_path, "rb") as file:
            keys = [key for key in pickle.load(file).keys()]

            return keys

    def set_field(self, field_name: str, **kwargs) -> None:
        """Set database field"""

        with open(self.__db_path, "rb") as file:
            current_db = pickle.load(file)
            current_db[field_name] = kwargs

        with open(self.__db_path, "wb") as file:
            pickle.dump(current_db, file)

    def remove_field(self, field_name: str) -> None:
        """Remove database field"""

        with open(self.__db_path, "rb") as file:
            current_db = pickle.load(file)

        keys = [key for key in current_db.keys()]
        if field_name not in keys:
            raise Exception(f"Field with name \"{field_name}\" not found")

        del current_db[field_name]
        with open(self.__db_path, "wb") as file:
            pickle.dump(current_db, file)
