from abc import ABC, abstractmethod

# Strategy pattern (для атаки)

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass

class SwordAttack(AttackStrategy):
    def attack(self):
        return "Атакує мечем!"

class BowAttack(AttackStrategy):
    def attack(self):
        return "Атакує з лука!"

class MagicAttack(AttackStrategy):
    def attack(self):
        return "Атакує магією!"

# State pattern (стан персонажа) 

class State(ABC):
    @abstractmethod
    def handle(self, character):
        pass

class HealthyState(State):
    def handle(self, character):
        print("Персонаж здоровий і готовий до бою.")

class WoundedState(State):
    def handle(self, character):
        print("Персонаж поранений. Його атаки слабші.")

class CriticalState(State):
    def handle(self, character):
        print("Персонаж майже мертвий! Потрібно лікування.")

class DeadState(State):
    def handle(self, character):
        print("Персонаж загинув... ")

# Клас персонажа, який використовує Strategy та State 

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_strategy = SwordAttack()
        self.state = HealthyState()

    def set_attack_strategy(self, strategy: AttackStrategy):
        self.attack_strategy = strategy

    def take_damage(self, amount):
        if isinstance(self.state, DeadState):
            print("Персонаж вже мертвий. Додаткова шкода немає сенсу.")
            return
        self.health -= amount
        self.update_state()

    def heal(self, amount):
        if isinstance(self.state, DeadState):
            print("Неможливо лікувати мертвого персонажа!")
            return
        self.health += amount
        if self.health > 100:
            self.health = 100
        self.update_state()

    def update_state(self):
        if self.health <= 0:
            self.health = 0
            self.state = DeadState()
        elif self.health <= 30:
            self.state = CriticalState()
        elif self.health <= 70:
            self.state = WoundedState()
        else:
            self.state = HealthyState()

    def perform_attack(self):
        if isinstance(self.state, DeadState):
            print("Мертвий персонаж не може атакувати.")
        else:
            print(self.attack_strategy.attack())

    def status(self):
        print(f"\n[{self.name}] Здоров'я: {self.health}")
        self.state.handle(self)

# Демонстрація 

def main():
    hero = Character("Артур")

    while True:
        hero.status()
        print("\n1. Атакувати")
        print("2. Змінити стратегію атаки")
        print("3. Отримати шкоду")
        print("4. Вилікуватись")
        print("5. Вийти")

        choice = input("Виберіть дію: ")

        if choice == "1":
            hero.perform_attack()
        elif choice == "2":
            print("Оберіть нову стратегію атаки:")
            print("1. Меч")
            print("2. Лук")
            print("3. Магія")
            strat = input(">> ")
            if strat == "1":
                hero.set_attack_strategy(SwordAttack())
            elif strat == "2":
                hero.set_attack_strategy(BowAttack())
            elif strat == "3":
                hero.set_attack_strategy(MagicAttack())
        elif choice == "3":
            dmg = int(input("Скільки шкоди отримати? "))
            hero.take_damage(dmg)
        elif choice == "4":
            heal = int(input("Скільки здоров'я відновити? "))
            hero.heal(heal)
        elif choice == "5":
            print("Вихід з гри.")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()
