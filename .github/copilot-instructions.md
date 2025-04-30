<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

This is a Model Context Protocol (MCP) server project that provides MongoDB integration capabilities. The server implements tools for interacting with MongoDB databases, collections, and documents.

You can find more info and examples at https://modelcontextprotocol.io/llms-full.txt

Key components:
1. MongoDB connection handling using PyMongo
2. MCP tools for database operations (CRUD)
3. Async context management for MongoDB connections
4. Error handling and connection lifecycle management

When suggesting code for this project:
- Use type hints for better code clarity
- Follow async/await patterns for MongoDB operations
- Implement proper error handling for MongoDB operations
- Use MongoDB best practices for querying and updates