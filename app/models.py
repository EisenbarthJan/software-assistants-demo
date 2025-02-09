"""Module containing data models for the application."""

from pydantic.main import BaseModel


class Item(BaseModel):
    """Represents an item with its price and discount information."""
    name: str
    price: float
    discount: float = 0.0

    # TODO: Add validation rules
