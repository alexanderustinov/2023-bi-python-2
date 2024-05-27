from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

    def calculate_discounted_price(self, discount):
        discounted_price = self.price * (1 - discount)
        return discounted_price

    def to_string(self):
        return f"Товар: {self.name}, Цена: {self.price}"

    def __str__(self):
        return self.to_string()

inventory = []

@app.post("/products/")
async def create_product(product: Product):
    inventory.append(product)
    return {f"Продукт успешно добавлен: {product}"}

@app.get("/products/")
async def get_products():
    return inventory

@app.get("/products/{product_name}")
async def get_product_by_name(product_name: str):
    for product in inventory:
        if product.name == product_name:
            return product
    raise HTTPException(status_code=404, detail="Продукт не найден :(")

@app.get("/products/discounted/")
async def get_discounted_products(discount: float):
    discounted_products = []
    for product in inventory:
        discounted_price = product.calculate_discounted_price(discount)
        discounted_product = Product(name=product.name, price=round(discounted_price, 2))
        discounted_products.append(discounted_product)
    return discounted_products


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
