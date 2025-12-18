import os
import httpx
from fastmcp import FastMCP

KOLADA_BASE = "https://api.kolada.se/v3"

mcp = FastMCP("Kolada KPI MCP")

@mcp.tool
async def get_kpi(kpi_id: str):
    """Hämta metadata för ett Kolada-KPI, t.ex. N52001."""
    url = f"{KOLADA_BASE}/kpi/{kpi_id}"
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(url)
        r.raise_for_status()
        return r.json()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port,
        path="/mcp"
    )
