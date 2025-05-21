import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Клас документу, який потрібно клонувати
class Document(Prototype):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"Заголовок: {self.title}")
        print(f"Зміст: {self.content}")

# Демонстрація використання патерну Prototype
def main():
    print("Оригінальний документ:")
    original = Document("Звіт", "Це звіт за квітень.")
    original.display()

    print("\nКлонований документ:")
    clone = original.clone()
    clone.title = "Копія звіту"
    clone.content = "Це клон звіту з невеликими змінами."
    clone.display()

    print("\nПеревірка, що об'єкти різні:")
    print(f"original is clone? {original is clone}")
    print(f"original == clone? {original == clone}")  # Вони мають однакові дані, але це різні об'єкти

if __name__ == "__main__":
    main()
