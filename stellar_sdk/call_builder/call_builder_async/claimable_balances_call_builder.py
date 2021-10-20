from ...call_builder.base import BaseClaimableBalancesCallBuilder
from ...call_builder.call_builder_async.base_call_builder import BaseCallBuilder
from ...client.base_async_client import BaseAsyncClient
from ...type_checked import type_checked

__all__ = ["ClaimableBalancesCallBuilder"]


@type_checked
class ClaimableBalancesCallBuilder(BaseCallBuilder, BaseClaimableBalancesCallBuilder):
    """Creates a new :class:`ClaimableBalancesCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.ServerAsync.claimable_balance`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(self, horizon_url, client: BaseAsyncClient) -> None:
        super().__init__(horizon_url=horizon_url, client=client)
