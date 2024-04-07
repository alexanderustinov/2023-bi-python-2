#Классификация персонажей в Genshin Impact

from pydantic import BaseModel

class name_and_element(BaseModel):
    name: str
    element: str

    def print_name(self):
        print(f'My name is {self.name}')

    def print_element(self):
        print(f"My element is {self.element}")

    def archon_name(self):
        if self.element == "Anemo":
            archon_name = "Lord Barbatos"
        if self.element == "Geo":
            archon_name = "Rex Lapis"
        if self.element == "Electro":
            archon_name = "Raiden Shogun"
        if self.element == "Dendro":
            archon_name = "Lesser Lord Kusanali"
        if self.element == "Hydro":
            archon_name = "Focalors"
        if self.element == "Pyro":
            archon_name = "God of War"
        if self.element == "Cryo":
            archon_name = "The Tsaritsa"
        return archon_name
