from pydantic import BaseModel
class Fr(BaseModel):
    name: str
    taste: str
    size: str
    color: str
    def vkysn(self):
        return True

    def cislo(self):
        return False
class B(Fr):

    def vkysn(self):
        return self.taste == "вкусная"

    def des(self):
        return f"{self.color} ягода это {self.name},которая очень {self.taste} и немного {self.size}"
