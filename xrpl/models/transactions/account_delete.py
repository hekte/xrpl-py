"""
Represents an AccountDelete transaction on the XRP Ledger.

An AccountDelete transaction deletes an account and any objects it owns in the XRP
Ledger, if possible, sending the account's remaining XRP to a specified destination
account. See Deletion of Accounts for the requirements to delete an account.

`See AccountDelete <https://xrpl.org/accountdelete.html>`_
`See Deletion of Accounts <https://xrpl.org/accounts.html#deletion-of-accounts>`_
"""
from dataclasses import dataclass
from typing import Optional

from xrpl.models.transactions.transaction import REQUIRED, Transaction, TransactionType


@dataclass(frozen=True)
class AccountDelete(Transaction):
    """
    Represents an AccountDelete transaction on the XRP Ledger.

    An AccountDelete transaction deletes an account and any objects it owns in the XRP
    Ledger, if possible, sending the account's remaining XRP to a specified destination
    account. See Deletion of Accounts for the requirements to delete an account.

    `See AccountDelete <https://xrpl.org/accountdelete.html>`_
    `See Deletion of Accounts <https://xrpl.org/accounts.html#deletion-of-accounts>`_
    """

    destination: str = REQUIRED
    destination_tag: Optional[int] = None
    transaction_type: str = TransactionType.AccountDelete