"""Interface for all sync network clients to follow."""
from __future__ import annotations

import asyncio

from xrpl.asyncio.clients.client import Client
from xrpl.models.requests.request import Request
from xrpl.models.response import Response


class SyncClient(Client):
    """
    Interface for all sync network clients to follow.

    :meta private:
    """

    def request(self: SyncClient, request: Request) -> Response:
        """
        Makes a request with this client.

        Arguments:
            request: The Request to send.

        Returns:
            The Response for the given Request.
        """
        return asyncio.run(self.request_impl(request))
