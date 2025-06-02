from abc import ABC, abstractmethod

# ==== STRATEGY PATTERN ====

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass

class SwordAttack(AttackStrategy):
    def attack(self):
        return "Б'є мечем!"

class BowAttack(AttackStrategy):
    def attack(self):
        return "Стріляє з лука!"

class MagicAttack(AttackStrategy):
    def attack(self):
        return "Атакує магією!"

# ==== STATE PATTERN ====

class State(ABC):
    @abstractmethod
    def react(self):
        pass

class NormalState(State):
    def react(self):
        return "Спокійний і зосереджений."

class AngryState(State):
    def react(self):
        return "Злий! Атакує агресивно!"

class TiredState(State):
    def react(self):
        return "Втомлений. Повільна реакція."

# ==== CONTEXT ====

class Character:
    def __init__(self, name):
        self.name = name
        self.attack_strategy = SwordAttack()
        self.state = NormalState()

    def set_attack_strategy(self, strategy: AttackStrategy):
        self.attack_strategy = strategy

    def set_state(self, state: State):
        self.state = state

    def perform_attack(self):
        return self.attack_strategy.attack()

    def current_reaction(self):
        return self.state.react()

# ==== DEMO ====

def main():
    hero = Character("Герой")

    while True:
        print("\n--- Меню ---")
        print("1. Атакувати")
        print("2. Змінити стратегію атаки")
        print("3. Змінити стан")
        print("4. Показати реакцію")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("Атака:", hero.perform_attack())
        elif choice == "2":
            print("Оберіть стратегію: 1 - меч, 2 - лук, 3 - магія")
            strat = input("-> ")
            if strat == "1":
                hero.set_attack_strategy(SwordAttack())
            elif strat == "2":
                hero.set_attack_strategy(BowAttack())
            elif strat == "3":
                hero.set_attack_strategy(MagicAttack())
        elif choice == "3":
            print("Оберіть стан: 1 - нормальний, 2 - злий, 3 - втомлений")
            state = input("-> ")
            if state == "1":
                hero.set_state(NormalState())
            elif state == "2":
                hero.set_state(AngryState())
            elif state == "3":
                hero.set_state(TiredState())
        elif choice == "4":
            print("Стан:", hero.current_reaction())
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print("Невідомий вибір!")

if __name__ == "__main__":
    main()
