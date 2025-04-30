FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install uv for faster package installation
RUN pip install uv

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies using uv
RUN uv pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose MCP port
EXPOSE 6274

# Run the MCP server
CMD ["mcp", "run", "mongodb_mcp_server.py"]