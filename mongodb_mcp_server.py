from mcp.server.fastmcp import FastMCP, Context
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from typing import List, Dict, Any
import asyncio
import logging
import sys
import os
from datetime import datetime
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger("mongodb-mcp")

# Load environment variables
load_dotenv()

@asynccontextmanager
async def lifespan(app):
    """MongoDB connection lifecycle management"""
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise ValueError("MONGODB_URI environment variable is not set")
    
    client = None
    try:
        client = AsyncIOMotorClient(uri)
        await client.admin.command('ping')
        logger.info("MongoDB connection established")
        yield {"client": client}
    except Exception as e:
        logger.error(f"MongoDB connection error: {str(e)}")
        if client:
            client.close()
        raise
    finally:
        if client:
            client.close()

# Create MCP server instance
mcp = FastMCP("MongoDB MCP Server", lifespan=lifespan)

@mcp.tool()
async def ping(ctx: Context) -> Dict[str, Any]:
    """Test MongoDB connection"""
    try:
        client = ctx.request_context.lifespan_context["client"]
        await client.admin.command('ping')
        return {"status": "ok", "message": "Connected to MongoDB"}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@mcp.tool()
async def list_databases(ctx: Context) -> Dict[str, Any]:
    """List all available databases"""
    try:
        client = ctx.request_context.lifespan_context["client"]
        databases = await client.list_database_names()
        return {"status": "ok", "databases": databases}
    except Exception as e:
        return {"status": "error", "error": str(e)}

@mcp.tool()
async def find_documents(
    database: str,
    collection: str,
    ctx: Context,
    query: Dict[str, Any] = None,
    limit: int = 10
) -> Dict[str, Any]:
    """Find documents in a collection"""
    try:
        client = ctx.request_context.lifespan_context["client"]
        db = client[database]
        coll = db[collection]
        cursor = coll.find(query or {}).limit(limit)
        documents = await cursor.to_list(length=limit)
        return {"status": "ok", "documents": documents}
    except Exception as e:
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    logger.info("Starting MongoDB MCP Server...")
    mcp.run()