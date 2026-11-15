"""Windsor.ai adapter boundary; confirm provider endpoints before implementation."""
import httpx
from app.core.config import settings

class WindsorClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.api_key = settings.windsor_api_key

    async def get(self, path: str, params: dict | None = None) -> dict:
        if not self.api_key:
            raise RuntimeError("WINDSOR_API_KEY is not configured.")
        async with httpx.AsyncClient(base_url=self.base_url, timeout=30.0) as client:
            response = await client.get(path, params=params, headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()
            return response.json()
