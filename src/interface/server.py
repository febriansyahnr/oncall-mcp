from mcp.server.fastmcp import FastMCP
from src.use_cases.user_service import list_users, create_user_logic
from pydantic import ValidationError

# Initialize FastMCP
mcp = FastMCP("My Alchemy Server")

@mcp.tool()
def get_recent_users(limit: int = 5, source: str = 'xb') -> str:
    """
    Retrieves a list of recent users from the database.
    Use this to see who has signed up recently.
    
    Args:
        limit: Number of users to return.
        source: Database source. Options: 'xb' or 'snap'. Defaults to 'xb'.
    """
    try:
        users = list_users(limit, db_alias=source)
        # Return as JSON string or formatted text for the LLM
        return "\n".join([f"{u.id}: {u.username} ({u.email})" for u in users])
    except Exception as e:
        return f"Error fetching users from {source}: {str(e)}"

@mcp.tool()
def register_user(username: str, email: str) -> str:
    """
    Registers a new user in the system.
    """
    try:
        # Call the Use Case
        result = create_user_logic(username, email)
        return f"Success: {result}"
    except ValueError as e:
        return f"Validation Error: {e}"

from src.use_cases.payout_service import find_transaction_by_uuid, find_transaction_by_client_id

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

if __name__ == "__main__":
    mcp.run()
