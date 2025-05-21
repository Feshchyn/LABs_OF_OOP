from abc import ABC, abstractmethod


#  Composite  
class FileComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass


class File(FileComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(' ' * indent + f"- File: {self.name}")


class Folder(FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileComponent):
        self.children.append(component)

    def show(self, indent=0):
        print(' ' * indent + f"+ Folder: {self.name}")
        for child in self.children:
            child.show(indent + 2)


#  Facade  
class FileManager:
    def __init__(self):
        self.root = Folder("Root")

    def create_file(self, folder: Folder, file_name: str):
        file = File(file_name)
        folder.add(file)

    def create_folder(self, parent: Folder, folder_name: str) -> Folder:
        folder = Folder(folder_name)
        parent.add(folder)
        return folder

    def show_structure(self):
        self.root.show()


#  Використання (Console Interface) 
def main():
    manager = FileManager()

    docs = manager.create_folder(manager.root, "Documents")
    pics = manager.create_folder(manager.root, "Pictures")

    manager.create_file(docs, "resume.pdf")
    manager.create_file(docs, "report.docx")

    vacation = manager.create_folder(pics, "Vacation")
    manager.create_file(vacation, "beach.png")
    manager.create_file(vacation, "mountain.jpg")

    manager.create_file(manager.root, "readme.txt")

    print("\n Файлова структура:")
    manager.show_structure()


if __name__ == "__main__":
    main()
