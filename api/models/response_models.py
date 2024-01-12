from pydantic import BaseModel


class TwitterSentiment(BaseModel):
    tweet_id: str
    entity: str
    sentiment: str
    text: str
