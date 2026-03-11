from fastapi import APIRouter, Depends, Request

from app.agent.context import AgentDeps
from app.agent.core import agent
from app.auth import verify_api_key
from app.schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(
    request: Request,
    body: ChatRequest,
    _api_key: str = Depends(verify_api_key),
):
    deps = AgentDeps(http_client=request.app.state.http_client)
    result = await agent.run(body.message, deps=deps)

    return ChatResponse(
        response=result.output,
        conversation_id=body.conversation_id,
    )
