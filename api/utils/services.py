from typing import Any, Dict, List

import pandas as pd
from pathlib import Path


def get_tweets() -> List[Dict[str, Any]]:
    """Get treending topics persisted in MongoDB.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    current_script_path = Path(__file__).parents[0]
    tweet_data = pd.read_csv(
        f"{current_script_path}/twitter-dataset/twitter_training.csv"
    )
    trends = tweet_data.to_json()
    return trends
