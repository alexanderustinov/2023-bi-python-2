class Fr:
    def __init__(s, name, color, taste):
        s.name = name
        s.color = color
        s.taste = taste
    def vkysn(s):
        return True
    def cislo(s):
        return False
class Ci(Fr):
    def __init__(s, name, color, taste, cisl):
        super().__init__(name, color, taste)
        s.cisl = cisl

    def des(s):
        return f"{s.color} цитрусовый фрукт это {s.name},который очень {s.taste} на вкус"

    def cislo(s):
        return s.cisl > 5
class B(Fr):
    def __init__(s, name, color, taste, size):
        super().__init__(name, color, taste)
        s.size = size
    def vkysn(s):
        return s.taste == "вкусная"
    def des(s):
        return f"{s.color} ягода это {s.name},которая очень {s.taste} и немного {s.size}"

