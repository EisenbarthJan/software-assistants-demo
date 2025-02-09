"""Utility functions for price calculations and currency conversions."""

def validate_price(price: float) -> bool:
    """Validates if the given price is valid.
    
    Args:
        price: The price to validate
        
    Returns:
        bool: True if price is valid, False otherwise
    """
    return price > 0

def calculate_discount(price: float, discount: float) -> float:
    """Calculates the final price after applying discount.
    
    Args:
        price: Original price
        discount: Discount as a decimal (e.g., 0.2 for 20% discount)
        
    Returns:
        float: Price after discount
    """
    return price * (1 - discount)

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """Converts an amount from one currency to another.
    
    Args:
        amount: The amount to convert
        from_currency: Source currency code
        to_currency: Target currency code
        
    Returns:
        float: Converted amount
    """
    # Implementation pending
    return amount
