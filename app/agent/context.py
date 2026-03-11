from dataclasses import dataclass

import httpx


@dataclass
class AgentDeps:
    http_client: httpx.AsyncClient
