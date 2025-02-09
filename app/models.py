"""Module containing data models for the application."""

from pydantic import BaseModel, Field


class Item(BaseModel):
    """Represents an item with its price and discount information."""
    name: str
    price: float = Field(gt=0, description="Price must be greater than 0")
    discount: float = Field(
        default=0.0,
        ge=0,
        le=1,
        description="Discount must be between 0 and 1 (e.g., 0.2 for 20%)"
    )
