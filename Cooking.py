class Parent:

    def cook_dish(self):
        return "Cooking Delisius Food"

class Child(Parent):

    def cook_dish(self):
        dish = super().cook_dish()
        return dish + " with oil mixup"


p1 = Parent()
c1 = Child()

print(p1.cook_dish())
print(c1.cook_dish())