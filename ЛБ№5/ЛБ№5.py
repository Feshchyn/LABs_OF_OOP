from abc import ABC, abstractmethod

#  STRATEGY 

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата готівкою: {amount} грн")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата карткою: {amount} грн")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата криптовалютою: {amount} грн")

#  STATE 

class OrderState(ABC):
    @abstractmethod
    def next_state(self, order):
        pass

    @abstractmethod
    def handle(self):
        pass

class CreatedState(OrderState):
    def next_state(self, order):
        order.state = PaidState()
    
    def handle(self):
        print("Замовлення створено.")

class PaidState(OrderState):
    def next_state(self, order):
        order.state = DeliveredState()
    
    def handle(self):
        print("Замовлення оплачено.")

class DeliveredState(OrderState):
    def next_state(self, order):
        print("Замовлення вже доставлено. Немає наступного стану.")
    
    def handle(self):
        print("Замовлення доставлено.")

#  Order Class 

class Order:
    def __init__(self, amount):
        self.amount = amount
        self.state = CreatedState()
        self.payment_strategy = None

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def process_payment(self):
        if not self.payment_strategy:
            print("Стратегія оплати не встановлена!")
            return
        self.payment_strategy.pay(self.amount)
        self.state.next_state(self)

    def advance_state(self):
        self.state.next_state(self)

    def show_status(self):
        self.state.handle()

#  Головна програма 

def main():
    order = Order(500)

    while True:
        print("\n1. Показати стан замовлення")
        print("2. Встановити метод оплати")
        print("3. Оплатити замовлення")
        print("4. Перейти до наступного стану")
        print("5. Вийти")
        choice = input("Виберіть дію: ")

        if choice == "1":
            order.show_status()
        elif choice == "2":
            print("Виберіть спосіб оплати: 1 - Готівка, 2 - Картка, 3 - Криптовалюта")
            p = input("Ваш вибір: ")
            if p == "1":
                order.set_payment_strategy(CashPayment())
            elif p == "2":
                order.set_payment_strategy(CardPayment())
            elif p == "3":
                order.set_payment_strategy(CryptoPayment())
            else:
                print("Невірний вибір.")
        elif choice == "3":
            order.process_payment()
        elif choice == "4":
            order.advance_state()
        elif choice == "5":
            print("Вихід.")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()
