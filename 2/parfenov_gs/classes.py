#Классификация персонажей в Genshin Impact

class name_and_element:
    def __init__(self, name, element):
        self._name = name
        self._element = element
    def print_name(self):
        print(f"My name is {self._name}")
    def print_element(self):
        print(f"My element is {self._element}")

class vision_archon(name_and_element):
    def archon_title(self):
        if self._element == "Anemo":
            archon_name = "Lord Barbatos"
        if self._element == "Geo":
            archon_name = "Rex Lapis"
        if self._element == "Electro":
            archon_name = "Raiden Shogun"
        if self._element == "Dendro":
            archon_name = "Lesser Lord Kusanali"
        if self._element == "Hydro":
            archon_name = "Lady Furina"
        if self._element == "Pyro":
            archon_name = "God of War"
        if self._element == "Cryo":
            archon_name = "The Tsaritsa"
        print(f"Hello, my name is {self._name} and my vision was given to me by {archon_name}")
    def archon_name(self):
        if self._element == "Anemo":
            archon_name = "Barbatos"
        if self._element == "Geo":
            archon_name = "Morax"
        if self._element == "Electro":
            archon_name = "Raiden Ei"
        if self._element == "Dendro":
            archon_name = "Nahida"
        if self._element == "Hydro":
            archon_name = "Furina"
        if self._element == "Pyro":
            archon_name = "Murata"
        if self._element == "Cryo":
            archon_name = "Tsaritsa"
        print(f"Hello, my name is {self._name} and my vision was given to me by {archon_name}")
    def archon_nation(self):
        if self._element == "Anemo":
            archon_name = "Lord Barbatos"
            archon_nation = "Mondstadt"
        if self._element == "Geo":
            archon_name = "Rex Lapis"
            archon_nation = "Liyue"
        if self._element == "Electro":
            archon_name = "Raiden Shogun"
            archon_nation = "Inazuma"
        if self._element == "Dendro":
            archon_name = "Lesser Lord Kusanali"
            archon_nation = "Sumeru"
        if self._element == "Hydro":
            archon_name = "Lady Furina"
            archon_nation = "Fontaine"
        if self._element == "Pyro":
            archon_name = "God of War"
            archon_nation = "Natlan"
        if self._element == "Cryo":
            archon_name = "The Tsaritsa"
            archon_nation = "Snezhnaya"
        print(f"{archon_name} is the archon of {archon_nation}")

class character(name_and_element):
    def greet(self):
        print(f"Hello, my name is {self._name} and I have {self._element} vision")
    def notforget(self):
        print(f"Don't forget about {self._name}")
    def lostvision(self):
        print(f"Oh no, {self._name} lost {self._element} vision")
