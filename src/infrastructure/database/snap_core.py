from sqlalchemy import create_engine, MetaData, Table, select, insert
import os

SNAP_DATABASE_URL = os.getenv("SNAP_DATABASE_URL", "mysql+pymysql://user:pass@localhost:3306/snap_db")

snap_engine = create_engine(SNAP_DATABASE_URL)

metadata = MetaData()

bank_transfer_table = None

def init_reflection():
    """Reflect tables from database."""
    global bank_transfer_table
    try:
        with snap_engine.connect():
            bank_transfer_table = Table('bank_transfer', metadata, autoload_with=snap_engine)
    except Exception as e:
        print(f"Warning: Could not reflect 'bank_transfer' from snap: {e}")
        bank_transfer_table = None

init_reflection()