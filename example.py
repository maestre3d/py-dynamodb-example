class Parent:
    age = 0
    def setAge(self, age):
        self.age = age

# Inheritance
class Foo(Parent):
    __name = "Elver"
    def foo(self, lastname):
        print(self.__greet(self.__name + " " + lastname))
    
    def __greet(self, completeName):
        return "Hello, " + completeName



lastName = input("Enter last name: ")
f = Foo()
f.foo(lastName)

f.setAge(18)
print(f.age)