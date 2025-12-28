from src.infrastructure.database.xb import xb_engine
from src.infrastructure.database.snap_core import snap_engine

def get_db_connection(alias: str = 'xb'):
    """Get connection for specific database."""
    if alias == 'snap':
        return snap_engine.connect()
    return xb_engine.connect()