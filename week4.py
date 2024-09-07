# Creating the Python class
class Person:
    def __init__(self, name, age, gender):  # Double underscores on both sides
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am {self.gender}.")
        
# Create an instance of the Person class
person = Person("Elizabeth", 22, "Female")

# Call the introduce method
person.introduce()
