import asyncio
from dotenv import load_dotenv
load_dotenv(override=True)
from src.interface.server import mcp

async def main():
    await mcp.run_streamable_http_async()


if __name__ == "__main__":
    asyncio.run(main())
