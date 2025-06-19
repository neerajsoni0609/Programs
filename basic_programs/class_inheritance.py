class Parent:
    def __init__(self) -> None:
        print("Parent Class")
        self.var1 = "Parent"

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("Child Class")
        self.var2 = "Child"

child = Child()
print(child.var1)
