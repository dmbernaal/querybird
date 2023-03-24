# API entry point
from fastapi import FastAPI
# from starlette.middleware.sessions import SessionMiddleware # TO IMPLMENT

import openai

from .api import api_router
from .config import (
    OPENAI_ORG,
    OPENAI_KEY,
)


# OpenAI
openai.organization = OPENAI_ORG
openai.api_key = OPENAI_KEY

# FastAPI
app = FastAPI()

# Web API Framework, we seperate to include other frameworks in the future
api = FastAPI(
    title="QueryBird",
    description="Summarize transcriptions, automate tickets, and much more.",
    root_path="/",
    docs_url=None,
)

# router, include router here
api.include_router(api_router)

# mount app
app.mount("/", api)
