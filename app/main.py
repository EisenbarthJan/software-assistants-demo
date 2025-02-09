from fastapi import FastAPI
# Missing required imports
# from app.models import Item
# from app.utils import calculate_discount

app = FastAPI()

@app.get("/")
def read_root()  # Missing colon
    return {"message": "Welcome to the Software Assistants Demo"}

@app.post("/items/")
def create_item(item: Item):
    # No error handling
    discounted_price = calculate_discount(item.price, item.discount)
    return {"name": item.name, "discounted_price": discounted_price}

# TODO: Implement error handling
# TODO: Add input validation
# TODO: Add proper response models

