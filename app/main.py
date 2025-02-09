"""Main FastAPI application module."""

from fastapi import FastAPI, HTTPException
# Missing required imports
from app.models import Item
from app.utils import calculate_discount, validate_price

app = FastAPI()

@app.get("/")
async def read_root():
    """Root endpoint returning a welcome message.
    
    Returns:
        dict: Welcome message
    """
    return {"message": "Welcome to the pricing API"}

@app.post("/calculate-price")
async def calculate_price(item: Item):
    """Calculate final price for an item including discount.
    
    Args:
        item: Item object containing price and discount information
        
    Returns:
        dict: Final price calculation
    """
    try:
        final_price = calculate_discount(item.price, item.discount)
        return {"item_name": item.name, "final_price": final_price}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}

# TODO: Implement error handling
# TODO: Add input validation
# TODO: Add proper response models
