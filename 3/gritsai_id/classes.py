class Laundry:
    def __init__(self):
        self.basket = []

    def add_item(self, item):
        self.basket.append(item)

    def wash(self):
        print("Стирка белья...")
        for item in self.basket:
            item.mark_clean()

    def show_items(self):
        print("Список белья в прачечной:")
        for item in self.basket:
            print(f"{item.name} ({'чистое' if item.clean else 'грязное'})")


class Item:
    def __init__(self, name):
        self.name = name
        self.clean = False

    def mark_dirty(self):
        self.clean = False

    def mark_clean(self):
        self.clean = True


class Clothing(Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def resize(self, new_size):
        self.size = new_size

    def iron(self):
        print(f"Глажка {self.name}")
