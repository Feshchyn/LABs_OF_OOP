from abc import ABC, abstractmethod

# Принцип єдиної відповідальності: кожен клас має одну відповідальність

class UserInput:
    def get_input(self):
        name = input("Введіть ваше ім'я: ")
        age = input("Введіть ваш вік: ")
        return name, int(age)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Принцип відкритості/закритості: клас Greeting розширюється новими привітаннями без зміни існуючого коду

class Greeting(ABC):
    @abstractmethod
    def greet(self, user: User):
        pass

class CasualGreeting(Greeting):
    def greet(self, user: User):
        print(f"Привіт, {user.name}!")

class FormalGreeting(Greeting):
    def greet(self, user: User):
        print(f"Добрий день, {user.name}. Вам {user.age} років.")

# Клас, який обробляє логіку виводу
class Greeter:
    def __init__(self, greeting: Greeting):
        self.greeting = greeting

    def greet_user(self, user: User):
        self.greeting.greet(user)

# Основна функція
def main():
    user_input = UserInput()
    name, age = user_input.get_input()
    user = User(name, age)

    # Змінюючи об'єкт Greeting, не змінюємо логіку в інших класах (Open/Closed)
    greeting = FormalGreeting()  # або CasualGreeting()
    greeter = Greeter(greeting)
    greeter.greet_user(user)

if __name__ == "__main__":
    main()
