class Person:
    # Konstruktor __init__
    def __init__(self,name,age):
        self.name = name #Attribute name
        self.age = age #Attribute Age

    # Method untuk menampilkan sapaan
    def great(self):
        return "Hello, " + self.name
    
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday, {self.name}! your are {self.age} now"
    
    def set_ages(self,age):
        if age >= 0:
            self.age = age


person1 = Person("Joe",34)

print(person1.set_age(35))