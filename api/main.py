from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, Header, responses, status

from api.models.response_models import TwitterSentiment

from api.utils.services import get_tweets

app = FastAPI(
    # openapi_url=True,
    # docs_url=True,
    # redoc_url=True,
)


@app.get("/health-check")
def get_tweets_route_health():
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK, content={"content": "is running"}
    )


@app.get("/trends")
def get_tweets_route():
    return responses.JSONResponse(status_code=status.HTTP_200_OK, content=get_tweets())
