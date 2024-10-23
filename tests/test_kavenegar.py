from unittest.mock import AsyncMock, patch

import pytest

from src import APIException, KavenegarAPI


@pytest.mark.asyncio
class TestKavenegarAPI:
    API_KEY = "TEST_API_KEY"

    @pytest.fixture
    def api(self):
        """Fixture for initializing the KavenegarAPI."""
        return KavenegarAPI(self.API_KEY)

    @patch("aiohttp.ClientSession.post")
    async def test_sms_send_success(self, mock_post, api):
        mock_response = AsyncMock()
        mock_response.text.return_value = (
            '{"return": {"status": 200}, "entries": ["test_entry"]}'
        )
        mock_post.return_value.__aenter__.return_value = mock_response

        result = await api.sms_send({"receptor": "test"})
        assert result == ["test_entry"]

    @patch("aiohttp.ClientSession.post")
    async def test_sms_send_failure(self, mock_post, api):
        mock_response = AsyncMock()
        mock_response.text.return_value = (
            '{"return": {"status": 400, "message": "Bad Request"}}'
        )
        mock_post.return_value.__aenter__.return_value = mock_response

        with pytest.raises(APIException, match=r"APIException\[400\] Bad Request"):
            await api.sms_send({"receptor": "test"})
