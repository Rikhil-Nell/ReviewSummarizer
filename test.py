class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello " + self.name)
        print("I am " + self.age + " years old")

    @classmethod
    def create_anonymous(cls):
        return Test('Anonymous', 18)
