
class Father:

    def __init__(self):
        self.name = "Ahmed"


class Child(Father):

    def __init__(self):
        super().__init__()
        self.age = 20


child1 = Child()

print(child1.name, child1.age)
