""""
problem description
create a class called Triangle that accepts 3 integers as arguments
the class has:
    self.side1, self.side2, self.side3 instance variables set to arguments
    self.kind instance variable set to either equilateral, isosceles, or scalene

    property getter and setter for self.kind
        getter = private variable
        setter = dynamically computed from method to determine self.kind from arguments

    property getter and setter for side1, side2, side3
        getter = private variable
        setter = validated values

    method to determine self.kind from arguments
        assign string to self.kind

    validation method for
        self.side values are not zero 0
            raise ValueError
        self.side values are not negative
            raise ValueError
        self.side values create a valid triangle
            raise ValueError

determine self.kind from arguments
input
three integers representing three sides

output
string representing type of triangle
    equilateral
    isosceles
    scalene

boundaries/assumptions
equilateral => three sides are the same length
isosceles => only two sides are the same length
scalene => all three sides are different lengths

test cases
below

d/s
comparison, math.isclose()

algo -
if all three sides are equal, return equilateral
if two of the three sides are equal, return isosceles
if all three sides are different, return scalene

algo
if side1 is equal to side2 and side1 is equal to side 3: return equilateral
if side1 is equal to side2 or side2 is equal to side 3 or side1 is equal to side3: return isosceles
return scalene




validation method
input


"""
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1, self.side2, self.side3 = side1, side2, side3
        self._is_valid_triangle()

    @property
    def kind(self):
        return self._determine_triangle_kind()

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, new_side):
        if self._is_valid_side(new_side):
            self._side1 = new_side

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, new_side):
        if self._is_valid_side(new_side):
            self._side2 = new_side

    @property
    def side3(self):
        return self._side3

    @side3.setter
    def side3(self, new_side):
        if self._is_valid_side(new_side):
            self._side3 = new_side

    def _determine_triangle_kind(self):
        if (self.side1 == self.side2) and (self.side1 == self.side3):
            return 'equilateral'
        elif (self.side1 == self.side2) or (self.side1 == self.side3) or (self.side2 == self.side3):
            return 'isosceles'

        return 'scalene'

    def _is_valid_side(self, new_side):
        if new_side <= 0:
            raise ValueError('length of side must be above zero!')

        return True

    def _is_valid_triangle(self):
        lengths = sorted([self.side1, self.side2, self.side3])
        if (lengths[0] + lengths[1]) <= lengths[2]:
            raise ValueError('Please choose values that form a valid Triangle')


import unittest

class TestTriangle(unittest.TestCase):

    def test_equilateral_equal_sides(self):
        triangle = Triangle(2, 2, 2)
        self.assertEqual(triangle.kind, "equilateral")


    def test_larger_equilateral_equal_sides(self):
        triangle = Triangle(10, 10, 10)
        self.assertEqual(triangle.kind, "equilateral")


    def test_isosceles_last_two_sides_equal(self):
        triangle = Triangle(3, 4, 4)
        self.assertEqual(triangle.kind, "isosceles")


    def test_isosceles_first_last_sides_equal(self):
        triangle = Triangle(4, 3, 4)
        self.assertEqual(triangle.kind, "isosceles")


    def test_isosceles_first_two_sides_equal(self):
        triangle = Triangle(4, 4, 3)
        self.assertEqual(triangle.kind, "isosceles")


    def test_isosceles_exactly_two_sides_equal(self):
        triangle = Triangle(10, 10, 2)
        self.assertEqual(triangle.kind, "isosceles")


    def test_scalene_no_equal_sides(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.kind, "scalene")


    def test_scalene_larger_no_equal_sides(self):
        triangle = Triangle(10, 11, 12)
        self.assertEqual(triangle.kind, "scalene")


    def test_scalene_no_equal_sides_descending(self):
        triangle = Triangle(5, 4, 2)
        self.assertEqual(triangle.kind, "scalene")


    def test_small_triangles_are_legal(self):
        triangle = Triangle(0.4, 0.6, 0.3)
        self.assertEqual(triangle.kind, "scalene")


    def test_no_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 0)


    def test_negative_size_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, -5)


    def test_size_inequality_is_illegal(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)


    def test_size_inequality_is_illegal_2(self):
        with self.assertRaises(ValueError):
            Triangle(7, 3, 2)


    def test_size_inequality_is_illegal_3(self):
        with self.assertRaises(ValueError):
            Triangle(10, 1, 3)


    def test_size_inequality_is_illegal_4(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 2)

if __name__ == "__main__":
    unittest.main()
