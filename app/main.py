"""Horizon Helper - FastAPI backend serving the chat UI and the /api/chat endpoint."""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .agent import Concierge

_state: dict[str, Concierge] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    _state["concierge"] = Concierge()
    yield
    c = _state.pop("concierge", None)
    if c:
        c.close()


app = FastAPI(title="Horizon Helper", lifespan=lifespan)


class ChatIn(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "horizon-helper"}


@app.post("/api/chat")
def chat(body: ChatIn):
    text = (body.message or "").strip()
    if not text:
        return JSONResponse(status_code=400, content={"error": "message is required"})
    try:
        reply = _state["concierge"].ask(text)
        return {"reply": reply}
    except Exception:
        return JSONResponse(
            status_code=502,
            content={"reply": "Our concierge is unavailable right now - please try again in a moment."},
        )


_here = os.path.dirname(__file__)
app.mount("/", StaticFiles(directory=os.path.join(_here, "..", "static"), html=True), name="static")
