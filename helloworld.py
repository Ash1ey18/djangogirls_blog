# print("Hello, World!")

# """
# if 5 > 2:
#   print("Five is greater than two!")

# """

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# a = "Hello, World!"
# print(a[10])

# a = "Hello,  World!"
# print(len(a))

# b = "Hello, World!"
# print(b[2:5])

# a = "Hello, World!"
# print(a.replace("H", "J"))

# b = a.count("l")
# print(b)

# print(a.encode())

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 20

# print(mytuple)


# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.clear()
# thisset.add("asahi")
# print(thisset)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection(y)

# print("x: ",x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)

# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.symmetric_difference(y)

# print(z)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change


# for x in range(2, 30, 3):
#   print(x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)


class Sample:
		def __init__(self, a, b):
				self.ab = a
				self.b = b

s = Sample(1, 2)
print(dir(s))

print(hasattr(s, 'a')) # True
print(hasattr(s, 'c')) # False