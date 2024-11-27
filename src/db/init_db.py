from src.db.connection import SQL_ENGINE
from src.db.models import * # pylint: disable=wildcard-import, unused-wildcard-import

def init_sql_db() -> None:
    """
    Init SQL DB
    """
    SQL_Base.metadata.create_all(SQL_ENGINE)
