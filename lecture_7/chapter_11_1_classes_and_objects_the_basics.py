# 11.1.1 - Object-oriented programming
# 11.1.2 - User-defined compound data types


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0


p = Point()  # Instantiate an object of type Point
q = Point()  # Make a second point

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y

# This is similar to what we ued to do before with Turtles
from turtle import Turtle

tess = Turtle()  # Instantiate objects of type Turtle
alex = Turtle()

# 11.1.3 - Attributes
p.x = 3
p.y = 4

print(p.y)
x = p.x  # The expression p.x means go to the object p refers to and get the value of x
print(x)

print("(x={0}, y={1})".format(p.x, p.y))  # We can use dot notation as part of any expression
distance_squared_from_origin = p.x * p.x + p.y * p.y
print(distance_squared_from_origin)


# 11.1.4 - Improving our initializer
class Point2:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):  # If the caller does not supply arguments they will get the values of 0
        """ Create a new point at x, y """
        self.x = x
        self.y = y


p = Point2(4, 2)
q = Point2(6, 3)
r = Point2()  # r represents the origin (0, 0)
print(p.x, q.y, r.x)


# 11.1.5 - Adding other methods to our class
class Point3:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):  # Basically, by having this here I will be able to call it similarly to other
        """ Compute my distance from the origin """  # methods (e.g., tess.right(90))
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point3(3, 4)
print(p.x)
print(p.y)
print(p.distance_from_origin())

q = Point3(5, 12)
print(q.x)
print(q.y)
print(q.distance_from_origin())

r = Point3()  # The point gets the default value of (0,0)
print(r.x)
print(r.y)
print(r.distance_from_origin())


# 11.1.6 - Instances as arguments and parameters
def print_point(pt):
    """" print_point takes a point as an argument and formats the output
    in whichever way we choose. If we call print_point(p) with point p as
    defined previously, the output is (3, 4).
    """
    print("({0}, {1})".format(pt.x, pt.y))


# 11.1.7 - Converting an instance to a string
class Point4:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self):
        """" Other option. Python interpreter will use our code whenever
         it needs to convert a Point to a string """
        return "({0}, {1})".format(self.x, self.y)


p = Point4(3, 4)
print(p.to_string())  # With this, by having created the "to_string" function I dont have to
# use the function in 11.6 every time to get the point in the (x,y) format.
# Thus, by having this this second way its a method and its easier to call.

str(p)  # Python now uses the __str__ method that we wrote.
print(p)


# 11.1.8 - Instances as return values
def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point4(mx, my)


p = Point4(3, 4)
q = Point4(5, 12)
r = midpoint(p, q)
print(r)


# We can add the above to our class as a method
class Point5:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        """" Other option. Python interpreter will use our code whenever
         it needs to convert a Point to a string """
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point5(mx, my)


p = Point5(3, 4)
q = Point5(5, 12)
r = p.halfway(q)  # p is the self and q the target. Pretty cool.
print(r)
# Or
print(Point5(3, 4).halfway(Point5(5, 12)))

# 11.1.9 - A change of perspective
# 11.1.10 - Objects can have state

