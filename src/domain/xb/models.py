from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from decimal import Decimal

class PayoutTransactionRead(BaseModel):
    uuid: str
    merchant_id: str
    purpose_id: str
    acquirer_transaction_id: str
    client_transaction_id: str
    partner_request_id: str
    partner_transaction_id: str
    source_currency: str
    target_currency: str
    source_account: str
    destination_amount: Decimal
    markup_fx_rate: Decimal
    original_fx_rate: Decimal
    provider_fx_rate: Optional[Decimal] = None
    spread_rate: Decimal
    spread_type: str
    total_amount: Decimal
    statement_narrative: str
    remitter_uuid: str
    beneficiary_uuid: str
    provider: str
    status: str
    partner_status: str
    routing_code: str
    routing_value: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    expired_at: datetime

    model_config = ConfigDict(from_attributes=True)
