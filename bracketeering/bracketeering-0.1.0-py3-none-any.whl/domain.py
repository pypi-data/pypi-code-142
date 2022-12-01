"""
Pydantic Objects etc.
"""
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FilingStatus(Enum):
    SINGLE = "single"
    MARRIED_FILING_JOINTLY = "jointly"
    MARRIED_FILING_SEPARATELY = "separately"
    HEAD_OF_HOUSEHOLD = "head"


class Bracket(BaseModel):
    tax_rate: Decimal = Field(..., ge=0, le=1)
    min_value: Decimal = Field(..., ge=0)
    max_value: Optional[Decimal] = Field(..., ge=0)
