from sqlalchemy import create_engine, MetaData, Table, select, insert
import os

# 1. Connection
XB_DATABASE_URL = os.getenv("XB_DATABASE_URL", "mysql+pymysql://user:pass@localhost:3306/xb_db")
SNAP_DATABASE_URL = os.getenv("SNAP_DATABASE_URL", "mysql+pymysql://user:pass@localhost:3306/snap_db")

# Create separate engines
xb_engine = create_engine(XB_DATABASE_URL)
snap_engine = create_engine(SNAP_DATABASE_URL)

metadata = MetaData()

# 2. Reflection
# We attempt to reflect 'payout_transactions' from XB.

# Specific reflection for payout_transactions (XB only)
payout_transactions_table = None

def init_reflection():
    """Reflect tables from database."""
    global payout_transactions_table
    try:
        with xb_engine.connect():
            payout_transactions_table = Table('payout_transactions', metadata, autoload_with=xb_engine)
    except Exception as e:
        print(f"Warning: Could not reflect 'payout_transactions' from xb: {e}")
        payout_transactions_table = None

# Run reflection immediately (module load time)
init_reflection()

def get_db_connection(alias: str = 'xb'):
    """Get connection for specific database."""
    if alias == 'snap':
        return snap_engine.connect()
    return xb_engine.connect()
