import requests

def main():
    food_products = [
        {"name": "Яблоки", "price": 51.5},
        {"name": "Молоко", "price": 60.},
        {"name": "Хлеб", "price": 50.},
        {"name": "Картофель", "price": 30.8}
    ]

    for product in food_products:
        response = requests.post("http://localhost:8080/products/", json=product)
        print(response.text)

    response = requests.get("http://localhost:8080/products/")
    print("All products:")
    print(response.text)

    product_name = "Яблоки"
    response = requests.get(f"http://localhost:8080/products/{product_name}")
    print(f"Product '{product_name}':")
    print(response.text)

    discount = .1
    response = requests.get(f"http://localhost:8080/products/discounted/?discount={discount}")
    print(f"Discounted products (discount={discount}):")
    print(response.text)

if __name__ == "__main__":
    main()
