import json
from functools import lru_cache
from logging import getLogger
from typing import Any, Optional

import pandas as pd
import requests

from .config import get_settings

settings = get_settings()
logger = getLogger(__name__)


class YahooFinanceDataGrabber:
    """
    NOTE: Do not initialise this class directly, see 'get_yf_data_grabber()'
    at the very bottom of this script.
    """

    def __init__(self, api_key: str) -> None:
        self.headers = {
            "accept": "application/json",
            "X-API-KEY": api_key,
        }

    def _fetch_response_dict(self, api_args: str) -> Optional[dict[str, Any]]:
        try:
            response = json.loads(
                requests.get(
                    f"https://yfapi.net/v8/finance/{api_args}",
                    headers=self.headers,
                ).text
            )
            if response:
                # Catch API failures as they come through in JSON format too
                if "message" in response.keys():
                    logger.error(
                        f"Query failed to return any results.\n"
                        f"Query used: {api_args}\n"
                        f"Message: {response['message']}"
                    )
                    return None

                # Successful response
                return response

            else:
                # No response provided by API
                logger.error(f"Query failed to return any results.\nQuery used: {api_args}")
                return None

        except ConnectionError as e:
            logger.error(f"Failed to connect to Yahoo Finance API! {e}")
            return None

    def spark(self, asx_codes: list[str]) -> pd.DataFrame:
        api_args = "spark?interval=1d&range=1mo&symbols=AAPL"
        response = self._fetch_response_dict(api_args)

        if response:
            # Iterate through each code, then concatentate
            response_dfs = []
            for code in asx_codes:
                reponse_current = response[code]
                response_df = pd.DataFrame(
                    {
                        "timestamp": reponse_current["timestamp"],
                        "close": reponse_current["close"],
                    }
                )
                response_df.insert(loc=0, column="asx_code", value=code)
                response_dfs.append(response_df)
            return pd.concat(response_dfs)
        else:
            return None


@lru_cache
def get_yf_data_grabber():
    """
    This function is used to create a singleton factory of the
    data grabber - so that it can be used all throughout the different
    dashboards without needing to re-initialise the class each time.
    """
    return YahooFinanceDataGrabber(settings.YAHOO_FINANCE_API_KEY)
