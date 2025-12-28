# MCP Alchemy Server

A Model Context Protocol (MCP) server that provides access to transaction data from the XB database. This server is designed to be used with MCP clients (like Claude Desktop or other AI agents) to retrieve financial transaction details.

## Features

- **Payout Transaction Lookup**: Retrieve payout transaction details using either a UUID or a Client Transaction ID.
- **MCP Standard**: Built using the `fastmcp` SDK, compatible with any MCP client.

## prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd oncall-mcp
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your database connection strings:
   ```env
   XB_DATABASE_URL="mysql+pymysql://user:password@host:port/database"
   SNAP_DATABASE_URL="mysql+pymysql://user:password@host:port/database"
   ```

## Running the Server

### Development / Local Run

To run the server locally with hot-reloading (if supported by the runner) or for testing:

```bash
uv run main.py
```

### Using with an MCP Client

You can configure your MCP client to run this server directly. For example, in `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "PivotOnCall": {
        "serverUrl": "http://localhost:8000/mcp"
    }
  }
}
```

## Available Tools

### `get_payout_transaction`

Retrieves a payout transaction from the XB database.

- **Arguments**:
  - `identifier` (string): The UUID or Client Transaction ID.
  - `by_client_id` (boolean, optional): Set to `True` if searching by Client Transaction ID. Defaults to `False` (UUID).

- **Example Prompts**
```
check payout transaction with this uuid bc09aa1e-005a-48da-9837-bf68fa4969a9
```

```
check payout transaction with this client id 0199fd4f-b542-79fd-9666-a4b8397ace29
```