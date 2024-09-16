# Protected Members: Members prefixed with a single underscore (e.g., _attribute)
# are protected and should not be accessed outside the class or subclasses.
# However, they are still accessible in Python but are considered
# a convention to indicate they should not be directly used.
# Private Members: Members prefixed with double underscores (e.g., __attribute) are private
# and cannot be accessed directly from outside the class.
class Parent:
    def __init__(self):
        self._protected_attr = "protected"
        self.__private_attr = "private"

class Child(Parent):
    def show_attributes(self):
        print(self._protected_attr)  # Accessible
        # print(self.__private_attr)  # Would raise an error

child = Child()
child.show_attributes()
