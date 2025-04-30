# MongoDB MCP Server 🚀

A powerful Model Context Protocol (MCP) server implementation for MongoDB integration, providing seamless interaction with MongoDB databases through a standardized protocol.

## 🌟 Author
**Syed Asad**

## 📋 Overview

This MCP server implementation provides a robust interface for interacting with MongoDB databases through the Model Context Protocol. It supports operations on databases, collections, and documents with proper async/await patterns and error handling.

## ✨ Features

- 🔄 Full MongoDB CRUD operations support
- 🔐 Secure connection handling with MongoDB Atlas
- 🚦 Async/await patterns for optimal performance
- 🛡️ Comprehensive error handling
- 📦 Docker support for easy deployment
- 🔍 Query execution with proper type hints

## 🚀 Quick Start

### Using uvx (Python)

```bash
# Run directly with uvx
uvx mongodb-mcp-bridge

# With SSE transport for remote connections
uvx mongodb-mcp-bridge --transport=sse
```

### Using npx (Node.js)

```bash
# Run directly with npx
npx mongodb-mcp-bridge

# With SSE transport for remote connections
npx mongodb-mcp-bridge --transport=sse
```

### Environment Variables

Set these environment variables before running the server:

```bash
# Required
MONGODB_URI="your_mongodb_connection_string"

# Optional
MONGODB_DB="default_database_name"
MCP_PORT="6274"  # Default port for MCP Inspector
```

### Using Docker 🐳

```bash
# Build the Docker image
docker build -t mongodb-mcp-server .

# Run the container
docker run -e MONGODB_URI="your_mongodb_uri" -p 6274:6274 mongodb-mcp-server
```

## 🔗 IDE Integration

### VS Code Setup

Add this to your VS Code settings.json:

```json
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "mongodbUri",
        "description": "MongoDB Connection URI"
      }
    ],
    "servers": {
      "mongodb": {
        "command": "uvx",
        "args": ["mongodb-mcp-bridge", "--transport=sse"],
        "env": {
          "MONGODB_URI": "$(mongodbUri)"
        }
      }
    }
  }
}
```

### Cursor/Windsurf Setup

For Cursor or Windsurf, configure the MCP server with:

```json
{
  "mcp": {
    "servers": {
      "mongodb": {
        "url": "http://localhost:6274"
      }
    }
  }
}
```

## 📚 Available Tools

1. **ping**
   - Quick connection test to verify MongoDB connectivity

2. **list_databases**
   - List all available databases in the MongoDB instance

3. **find_documents**
   - Query documents in a collection with filtering options
   - Parameters:
     - `database`: Database name
     - `collection`: Collection name
     - `query`: MongoDB query object (optional)
     - `limit`: Maximum number of documents to return (default: 10)

## 🔍 Example Usage

Using the MCP Inspector (http://127.0.0.1:6274):

```json
// List all databases
{
    "tool": "list_databases"
}

// Find documents in a collection
{
    "tool": "find_documents",
    "database": "your_database",
    "collection": "your_collection",
    "query": {"status": "active"},
    "limit": 5
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Model Context Protocol (MCP) team for the protocol specification
- MongoDB team for the excellent database and drivers
- All contributors and users of this project

---
Made with ❤️ by Syed Asad