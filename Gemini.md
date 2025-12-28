# Gemini.md - Project Blueprint

## Architecture: Clean Architecture + MCP
This project follows a unidirectional data flow:
1. **Interface (MCP Layer)**: Receives requests from Claude/LLM.
2. **Use Cases (Application)**: orchestrates logic (e.g., "Find high-value customers").
3. **Domain (Entities)**: Pure Pydantic models. No DB logic here.
4. **Infrastructure (DB)**: SQLAlchemy implementation.

## Tech Stack
- **Server**: `mcp` (FastMCP)
- **ORM**: SQLAlchemy (Core + Reflection)
- **Validation**: Pydantic
- **Database**: Existing MySQL (Auto-reflected)
