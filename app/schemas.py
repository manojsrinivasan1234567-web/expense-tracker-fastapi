

from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class ExpenseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0, allow_inf_nan=False)
    category: str = Field(min_length=1, max_length=50)
    expense_date: date
    description: str | None = Field(
        default=None,
        max_length=500,
    )


class ExpenseUpdate(BaseModel):
    title: str | None = Field(
        default=None, min_length=1, max_length=100
    )
    amount: float | None = Field(
        default=None, gt=0, allow_inf_nan=False
    )
    category: str | None = Field(
        default=None, min_length=1, max_length=50
    )
    expense_date: date | None = None
    description: str | None = Field(
        default=None, max_length=500
    )


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    expense_date: date
    description: str | None

    model_config = ConfigDict(from_attributes=True)
