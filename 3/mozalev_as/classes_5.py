class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discounted_price(self, discount):
        discounted_price = self.price * (1 - discount)
        return discounted_price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price}"


class ShoppingCartItem(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def calculate_total_price(self, discount):
        discounted_price = self.calculate_discounted_price(discount)
        total_price = discounted_price * self.quantity
        return total_price
    
    def __str__(self):
        return f"Товар: {self.name}, Количество: {self.quantity}, Общая цена: {self.calculate_total_price(0)}"
    
    def to_str(self):
        return f"Товар: {self.name}, Количество: {self.quantity}, Общая цена: {self.calculate_total_price(0)}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        cart_item = ShoppingCartItem(product.name, product.price, quantity)
        self.cart.append(cart_item)

    def view_cart(self):
        #(f"Корзина {self.name}:")
        items = ""
        for item in self.cart:
            #print(item)
            items=items+item.to_str()+"\n"
        return items
            
