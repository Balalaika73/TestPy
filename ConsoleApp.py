class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        if self.age >= 18:
            return f"Привет, {self.name}! Вы совершеннолетний."
        else:
            return f"Привет, {self.name}! Вы несовершеннолетний."

def main():
    name = input("Введите ваше имя: ")
    age = int(input("Введите ваш возраст: "))
    
    person = Person(name, age)
    print(person.greet())

    for i in range(age):
        if i % 2 == 0:
            print(f"{i} - четное число")
        else:
            print(f"{i} - нечетное число")

if __name__ == "__main__":
    main()
