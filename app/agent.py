"""Azure AI Foundry agent wiring (azure-ai-agents).

Creates one Horizon Helper agent + a shared conversation thread at startup and
relays chat messages to it. Auth is Microsoft Entra via DefaultAzureCredential
(no API keys), matching MCAPS policy.
"""
import os
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from .excursions import instructions

ENDPOINT = os.environ["AI_FOUNDRY_PROJECT_ENDPOINT"]
MODEL = os.environ.get("AI_FOUNDRY_MODEL_DEPLOYMENT", "gpt-4o-mini")


class Concierge:
    def __init__(self) -> None:
        self._client = AgentsClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
        self._agent = self._client.create_agent(
            model=MODEL, name="horizon-helper", instructions=instructions()
        )
        self._thread = self._client.threads.create()

    def ask(self, message: str) -> str:
        self._client.messages.create(thread_id=self._thread.id, role="user", content=message)
        run = self._client.runs.create_and_process(
            thread_id=self._thread.id, agent_id=self._agent.id
        )
        if run.status == "failed":
            raise RuntimeError(f"agent run failed: {run.last_error}")
        msg = self._client.messages.get_last_message_text_by_role(
            thread_id=self._thread.id, role="assistant"
        )
        return msg.text.value if msg else "Sorry, I couldn't come up with a suggestion just now."

    def close(self) -> None:
        try:
            self._client.delete_agent(self._agent.id)
        except Exception:
            pass
