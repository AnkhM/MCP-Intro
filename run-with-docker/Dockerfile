FROM python:3.11-slim

WORKDIR /app

# Install uv for quicker package management
RUN pip install uv

# Copy requirements file
COPY requirements.txt .

# Install dependencies using uv
RUN uv venv
RUN uv pip install -r requirements.txt

# Copy application code
COPY client.py .
COPY server.py .

# Expose the port the server runs on
EXPOSE 8050 

# Command to run the server
CMD ["uv", "run", "server.py"]

# Use docker build -t mcp-server . to build the image
# Use docker run -p 8050:8050 mcp-server to run the container