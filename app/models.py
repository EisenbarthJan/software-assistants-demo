from pydantic import BaseModel

class Item(BaseModel:  # Missing parenthesis
        name: str     # Incorrect indentation
    price: float
        discount: float = 0.0  # Inconsistent indentation

    # TODO: Add validation rules