import pytest
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from mongodb_mcp_server import mcp, ping, list_databases, find_documents
from mcp.server.fastmcp import Context
from unittest.mock import AsyncMock, MagicMock

@pytest.fixture
def mock_mongodb_client():
    client = AsyncMock(spec=AsyncIOMotorClient)
    client.admin.command = AsyncMock(return_value={"ok": 1})
    client.list_database_names = AsyncMock(return_value=["test_db", "admin"])
    return client

@pytest.fixture
def mock_context(mock_mongodb_client):
    context = MagicMock(spec=Context)
    context.request_context.lifespan_context = {"client": mock_mongodb_client}
    return context

@pytest.mark.asyncio
async def test_ping(mock_context):
    result = await ping(mock_context)
    assert result["status"] == "ok"
    assert "message" in result

@pytest.mark.asyncio
async def test_list_databases(mock_context):
    result = await list_databases(mock_context)
    assert result["status"] == "ok"
    assert "databases" in result
    assert len(result["databases"]) == 2
    assert "test_db" in result["databases"]

@pytest.mark.asyncio
async def test_find_documents(mock_context, mock_mongodb_client):
    test_docs = [{"_id": 1, "name": "test"}]
    collection_mock = AsyncMock()
    collection_mock.find().limit().to_list = AsyncMock(return_value=test_docs)
    
    mock_mongodb_client.__getitem__.return_value.__getitem__.return_value = collection_mock
    
    result = await find_documents(
        database="test_db",
        collection="test_collection",
        ctx=mock_context
    )
    
    assert result["status"] == "ok"
    assert result["documents"] == test_docs
    assert len(result["documents"]) == 1