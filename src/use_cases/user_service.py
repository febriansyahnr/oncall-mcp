from src.infrastructure.database import get_db_connection, get_user_table
from src.domain.models import UserRead
from sqlalchemy import select

def list_users(limit: int = 10, db_alias: str = 'xb') -> list[UserRead]:
    """Fetch users from DB and convert to Pydantic models."""
    users_table = get_user_table(db_alias)
    if users_table is None:
        raise RuntimeError(f"Database table 'users' not available for alias '{db_alias}'")

    with get_db_connection(db_alias) as conn:
        stmt = select(users_table).limit(limit)
        result = conn.execute(stmt).fetchall()
        
        # Convert raw DB rows -> Pydantic Models
        return [UserRead.model_validate(row) for row in result]

def create_user_logic(username: str, email: str) -> str:
    """Business logic for creating a user."""
    # Add validation logic here if needed (e.g., check email format)
    if "@" not in email:
        raise ValueError("Invalid email format")
    
    # In a real app, you'd call a repository method here
    return f"Logic processed for {username}. Ready to insert."
