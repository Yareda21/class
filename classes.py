# this is where you declare all the class

# def calculator(num1)


# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address



# class Laptop:
#     def __init__(self, brandname, capacity, battry, ram):
#         self.brandname = brandname
#         self.capacity = capacity
#         self.battry = battry
#         self.ram = ram


# person1 = Person("etse", 30, "female", "aa")

# print(person1.address)


# car, bottle, Table 

class Car:
    def __init__(self, name, color, energy, machinetype):
        self.name = name
        self.color = color
        self.energy = energy
        self.type = machinetype

    def transport(self, element):
        print (self.name, "is transporting", element)

    def tour(self, place):
        print(self.name, "is in tour of", place)


car1 = Car("honda", "white", 1500, "gasoline")

car1.transport("people")
car1.tour("Hawassa")

class bottle:
    def __init__(self, kind, size, liter):
        self.kind = kind
        self.size = size
        self.liter = liter

bottle1 = bottle("water", "midium", 1)

print(bottle1.kind)
        

class Table:
    def __init__(self, kind, shape, color, material):
        self.kind = kind
        self.shape = shape
        self.color = color
        self.material = material

Table1 = Table("dining", "oval", "black", "wooden")

print(Table1.kind)
print(Table1.material)


