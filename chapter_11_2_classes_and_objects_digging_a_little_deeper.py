from lecture_7.chapter_11_1_classes_and_objects_the_basics import Point5 as Point


# 11.2.1 - Rectangles
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn  # Corner of the rectangle
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})"\
            .format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)  # In my video game
print("box: ", box)
print("bomb: ", bomb)

# 11.2.2 - Objects are mutable
box.width += 50
box.height += 100

# In order to provide a method that encapsulates the above inside a class we
# add the "grow" and "move" function

r = Rectangle(Point(10, 5), 100, 50)
print(r)
r.grow(25, -10)  # Now I can grow the rectangle by calling the functions inside the class. Pretty cool.
print(r)
r.move(-10, 10)  # Same
print(r)

# 11.2.3 - Sameness
p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 is p2)  # Even tho they contain the same coordinates, they are not the same object

p3 = p1
print(p1 is p3)  # The two variables are aliases of the same object


def same_coordinates(p1, p2):  # Finds if two points have the same coordinates
    return (p1.x == p2.x) and (p1.y == p2.y)


print(same_coordinates(p1, p2))  # If the two variables refer to the same object, they have
# both shallow and deep quality

# 11.2.4 - Copying
import copy
p1 = Point(3, 4)
p2 = copy.copy(p1)  # I think copying does the same as if we did p2 = p1
print(p1 is p2)
print(same_coordinates(p1, p2))
