# a = "Buddha"

# print(str(a)) # __str__
# print(repr(a)) # __repr__

class A:

    a = 20

    # def __str__(self):
    #     return "THe value of a is " + str(self.a)

    # def __repr__(self):
    #     return "THe value of a is " + str(self.a)

a = A()
print(repr(a))
print(__name__)