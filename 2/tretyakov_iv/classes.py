class Person():
    def __init__(self, name, age, access):
        self.name = name
        self.age = age
        self.access = access
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_access(self):
        return self.access

class Student(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age, 3)
        self.subject = subject
    def get_subj(self):
        return self.subject
    def inf(self):
        return f"My name {self.name}, I am studying {self.subject}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age, 4)
        self.subject = subject
    def get_subj(self):
        return self.subject
    def inf(self):
        return f"My name {self.name}, I teach {self.subject}"

class Guest(Person):
    def __init__(self, name, age, reason):
        Person.__init__(self, name, age, 1)
        self.reason = reason
    def get_reason(self):
        return self.reason
    def inf(self):
        return f"My name {self.name}, Reason of my visiting is {self.reason} "

# a = Student("Ivan", 17, "Bioinformatic")
# print(a.inf(), a.get_access())

# b = Teacher("Maksim", 51, "Algebra")
# print(b.inf(), b.get_access())

# c = Guest("Fedor", 73, "swimming")
# print(c.inf(), c.get_access())