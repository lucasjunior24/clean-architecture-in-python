from sqlalchemy import create_engine

class DbConnectionHandler:
    """Sqlalchemy  """

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
            return connection Engine
        """
        engine = create_engine(self.__connection_string)
        return engine
