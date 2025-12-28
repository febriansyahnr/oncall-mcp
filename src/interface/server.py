from mcp.server.fastmcp import FastMCP
from pydantic import ValidationError

# Initialize FastMCP
mcp = FastMCP("Pivot On Call MCP")

from src.use_cases.xb.payout_service import find_transaction_by_uuid, find_transaction_by_client_id

@mcp.tool()
def get_payout_transaction(identifier: str, by_client_id: bool = False) -> str:
    """
    Retrieves a payout transaction from the XB database.
    
    Args:
        identifier: The UUID or Client Transaction ID of the transaction.
        by_client_id: Set to True if the identifier is a Client Transaction ID. Defaults to False (UUID).
    """
    try:
        if by_client_id:
            txn = find_transaction_by_client_id(identifier)
        else:
            txn = find_transaction_by_uuid(identifier)
            
        if txn:
            return txn.model_dump_json(indent=2)
        return "Transaction not found."
    except Exception as e:
        return f"Error fetching payout transaction: {str(e)}"
