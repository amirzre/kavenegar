import json
from typing import Any, Dict, Optional

import aiohttp

from config import config
from exception import APIException, HTTPException


class KavenegarAPI:
    """
    https://kavenegar.com/rest.html
    """

    version = "v1"
    host = "api.kavenegar.com"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "charset": "utf-8",
    }

    def __init__(
        self,
        apikey: str,
        timeout: Optional[int] = None,
        proxies: Optional[Dict[str, str]] = None,
    ):
        """
        :param str apikey: Kavenegar API Key
        :param int timeout: request timeout, default is 10 seconds
        :param dict proxies: Dictionary mapping protocol to the URL of the proxy:
        """
        self.apikey = apikey
        self.apikey_mask = f"{apikey[:2]}********{apikey[-2:]}"
        self.timeout = timeout or config.DEFAULT_TIMEOUT
        self.proxies = proxies

    def __repr__(self):
        return f"KavenegarAPI({self.apikey_mask})"

    def __str__(self):
        return f"KavenegarAPI({self.apikey_mask})"

    def _parse_params_to_json(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Convert lists to JSON-like strings due to Kavenegar server expectation.
        """
        if params is None:
            return {}

        formatted_params = {
            key: json.dumps(value) if isinstance(value, (dict, list, tuple)) else value
            for key, value in params.items()
        }
        return formatted_params

    async def _request(
        self, action: str, method: str, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Send an asynchronous POST request to the Kavenegar API.
        """
        params = self._parse_params_to_json(params)
        url = f"https://{self.host}/{self.version}/{self.apikey}/{action}/{method}.json"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    url,
                    headers=self.headers,
                    data=params,
                    timeout=self.timeout,
                    proxy=self.proxies.get("http") if self.proxies else None,
                ) as response:
                    content = await response.text()
                    try:
                        data = json.loads(content)
                        if data["return"]["status"] == 200:
                            return data["entries"]
                        else:
                            raise APIException(
                                f"APIException[{data['return']['status']}] {data['return']['message']}"
                            )
                    except json.JSONDecodeError as e:
                        raise HTTPException(f"Error decoding response: {e}")
            except aiohttp.ClientError as e:
                message = str(e).replace(self.apikey, self.apikey_mask)
                raise HTTPException(message)

    async def sms_send(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("sms", "send", params)

    async def sendarray(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("sms", "sendarray", params)

    async def sms_status(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("sms", "status", params)

    async def sms_statuslocalmessageid(
        self, params: Optional[Dict[str, Any]] = None
    ) -> Any:
        return await self._request("sms", "statuslocalmessageid", params)

    async def sms_select(self, params=None):
        return await self._request("sms", "select", params)

    async def sms_selectoutbox(self, params=None):
        return await self._request("sms", "selectoutbox", params)

    async def sms_latestoutbox(self, params=None):
        return await self._request("sms", "latestoutbox", params)

    async def sms_countoutbox(self, params=None):
        return await self._request("sms", "countoutbox", params)

    async def sms_cancel(self, params=None):
        return await self._request("sms", "cancel", params)

    async def sms_receive(self, params=None):
        return await self._request("sms", "receive", params)

    async def sms_countinbox(self, params=None):
        return await self._request("sms", "countinbox", params)

    async def sms_countpostalcode(self, params=None):
        return await self._request("sms", "countpostalcode", params)

    async def sms_sendbypostalcode(self, params=None):
        return await self._request("sms", "sendbypostalcode", params)

    async def verify_lookup(self, params=None):
        return await self._request("verify", "lookup", params)

    async def call_maketts(self, params=None):
        return await self._request("call", "maketts", params)

    async def call_status(self, params=None):
        return await self._request("call", "status", params)

    async def account_info(self) -> Any:
        return await self._request("account", "info")

    async def account_config(self, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("account", "config", params)
