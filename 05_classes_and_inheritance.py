# === CLASSES ===

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """
        This is an example of a doctring.
        """

        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()
cat.speak()

# Practice:
# 1. Create a class `Person` with `name` and `age` attributes
# 2. Add a method `introduce()` that prints: "Hi, I'm [name], and I'm [age] years old."
# 3. Create a class `Student` that inherits from `Person`, and add a `grade` attribute