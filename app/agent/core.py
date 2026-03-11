from pydantic_ai import Agent

from app.agent.context import AgentDeps
from app.agent.prompts import SYSTEM_PROMPT

agent = Agent(
    "openai:gpt-4o-mini",
    deps_type=AgentDeps,
    system_prompt=SYSTEM_PROMPT,
)
