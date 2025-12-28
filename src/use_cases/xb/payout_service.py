from src.infrastructure.xb.database import get_db_connection, payout_transactions_table
from src.domain.xb.models import PayoutTransactionRead
from sqlalchemy import select

def find_transaction_by_uuid(uuid: str) -> PayoutTransactionRead | None:
    """Finds a payout transaction by its UUID."""
    if payout_transactions_table is None:
        raise RuntimeError("Payout transactions table not available (XB database issue)")
    
    # Verify we are on the correct DB context if needed, but here we just use the reflected table
    # We explicitly use the XB connection since this table is only on XB
    with get_db_connection('xb') as conn:
        stmt = select(payout_transactions_table).where(payout_transactions_table.c.uuid == uuid)
        result = conn.execute(stmt).fetchone()
        
        if result:
            return PayoutTransactionRead.model_validate(result)
        return None

def find_transaction_by_client_id(client_transaction_id: str) -> PayoutTransactionRead | None:
    """Finds a payout transaction by its Client Transaction ID."""
    if payout_transactions_table is None:
        raise RuntimeError("Payout transactions table not available (XB database issue)")
    
    with get_db_connection('xb') as conn:
        stmt = select(payout_transactions_table).where(payout_transactions_table.c.client_transaction_id == client_transaction_id)
        result = conn.execute(stmt).fetchone()
        
        if result:
            return PayoutTransactionRead.model_validate(result)
        return None

def list_payout_transactions(limit: int = 10) -> list[PayoutTransactionRead]:
    """Lists recent payout transactions."""
    if payout_transactions_table is None:
        raise RuntimeError("Payout transactions table not available (XB database issue)")
    
    with get_db_connection('xb') as conn:
        stmt = select(payout_transactions_table).order_by(payout_transactions_table.c.created_at.desc()).limit(limit)
        result = conn.execute(stmt).fetchall()
        
        return [PayoutTransactionRead.model_validate(row) for row in result]
