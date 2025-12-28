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
# We attempt to reflect 'users' from both. In a real scenario, schemas might differ.
users_tables = {}

def init_reflection():
    """Reflect tables from both databases."""
    global users_tables
    for alias, engine in [('xb', xb_engine), ('snap', snap_engine)]:
        try:
            with engine.connect():
                # We assume 'users' exists in both for simplicity of this template
                # You might want separate metadata or table names per DB
                t = Table('users', metadata, autoload_with=engine, extend_existing=True)
                users_tables[alias] = t
        except Exception as e:
            print(f"Warning: Could not reflect 'users' from {alias}: {e}")
            print(f"Warning: Could not reflect 'users' from {alias}: {e}")
            users_tables[alias] = None

# Specific reflection for payout_transactions (XB only)
payout_table = None
try:
    with xb_engine.connect():
        payout_table = Table('payout_transactions', metadata, autoload_with=xb_engine)
except Exception as e:
    print(f"Warning: Could not reflect 'payout_transactions' from xb: {e}")
    payout_table = None

# Run reflection immediately (module load time)
init_reflection()

def get_db_connection(alias: str = 'xb'):
    """Get connection for specific database."""
    if alias == 'snap':
        return snap_engine.connect()
    return xb_engine.connect()

def get_user_table(alias: str = 'xb'):
    """Get the reflected table for the specific database."""
    return users_tables.get(alias)
