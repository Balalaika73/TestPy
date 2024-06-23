class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        if self.age >= 18:
            return f"Hello, {self.name}! You are an adult."
        else:
            return f"Hello, {self.name}! You are not an adult."

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    person = Person(name, age)
    print(person.greet())

    for i in range(age):
        if i % 2 == 0:
            print(f"{i} - even number")
        else:
            print(f"{i} - odd number")

if __name__ == "__main__":
    main()
