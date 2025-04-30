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

## 🛠️ Technologies

- Python 3.12+
- MongoDB
- Model Context Protocol (MCP)
- Docker
- uv package manager
- Motor (async MongoDB driver)

## 🚀 Quick Start

### Using uv (Recommended)

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -r requirements.txt

# Run the server
mcp dev mongodb_mcp_server.py
```

### Using pip

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# OR
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
mcp dev mongodb_mcp_server.py
```

### Using Docker 🐳

```bash
# Build the Docker image
docker build -t mongodb-mcp-server .

# Run the container
docker run -e MONGODB_URI="your_mongodb_uri" -p 6274:6274 mongodb-mcp-server
```

## 🔧 Configuration

Set the following environment variables:

- `MONGODB_URI`: Your MongoDB connection string
- `MONGODB_DB`: (Optional) Default database name
- `MCP_PORT`: (Optional) Port for the MCP server (default: 6274)

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