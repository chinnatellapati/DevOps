# Classes in Python
# classes will be used to create new data types such as shopping cart...etc. Shopping cart will not a list, dictionary, tuple, boolean , string,array...et

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point() # object

point1.move()
point1.x = 20
print(point1.x)
point1.y=30
point1.draw()


point2 = Point()
point2.x = 10
print(point2.x)


# Example programs 

class Employee:
    def addition(self):
        print("Addition of numbers")
    def subtration(self):
        print("substration of numbers")
        
arthemeric = Employee()
p1 = arthemeric.addition()
p2 = arthemeric.subtration()




