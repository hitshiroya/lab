import httpx
from mcp.server.fastmcp import FastMCP

from src.auth.schemas import RegisterReq
from src.core.config import settings

mcp = FastMCP("Cluster Resource Management MCP Server", port=8001)

BASE_URL = settings.mcp_base_url


@mcp.tool()
async def register_user(user_data: RegisterReq) -> dict:
    """
    Register a new user in the system.

    Args:
        user_data: User details including name, username, password, and email.
    Returns:
        dict: Registered user data (id, name, username, email).
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/auth/register", json=user_data.model_dump())
        return response.json()


@mcp.resource("clusters://")
async def get_all_clusters() -> str:
    """
    Returns all clusters available in the infra.
    Load this to answer any questions about clusters - ownership, status, org.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/clusters/")
        return response.text


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
