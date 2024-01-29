import unittest     # this makes Python unittest module available

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
    """
    if (type(a) != (int or float)) or (type(b) != (int or float)) or (type(c) != (int or float)):
        return 'WrongInput'
    
    if (a >= b+c) or (b >= a+c) or (c >= a+b):
        return 'NotATriangle'
    
    if a==b or a==c or b==c:
        if a==b and a==c and b==c:
            return 'Equilateral'
        elif (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)):
            return 'Right'
        else:
            return 'Isoceles'
    elif a!=b and a!=c and b!=c:
        if (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)):
            return 'Right'
        else:
            return 'Scalene'


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=', classifyTriangle(a,b,c), sep=" ")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests

    def test_Set1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral', 'should be Equilateral')
        self.assertEqual(classifyTriangle(3,4,3), 'Isoceles', 'should be Isoceles')
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene', 'should be Scalene')
        self.assertEqual(classifyTriangle(3,4,5), 'Right', 'should be Right')

    def test_Set2(self):
        self.assertEqual(classifyTriangle(3,4,7), 'NotATriangle', 'Is NotATriangle')
        self.assertEqual(classifyTriangle(3,4,8), 'NotATriangle', 'Is NotATriangle')
        self.assertEqual(classifyTriangle(1,3,4), 'NotATriangle', 'Is NotATriangle')

    def test_Set3(self):
        self.assertNotEqual(classifyTriangle(10,10,10), 'Isoceles', 'Should be Equilateral')
        self.assertNotEqual(classifyTriangle(10,10,5), 'Equilateral', 'Should be Isoceles')
        self.assertNotEqual(classifyTriangle(6,8,10), 'Scalene', 'Should be Right')
        self.assertNotEqual(classifyTriangle(7,8,10), 'Right', 'Should be Scalene')

    def test_Set4(self):
        self.assertEqual(classifyTriangle('a',10,10), 'WrongInput', 'Should be WrongInput')
        self.assertEqual(classifyTriangle('a','b',10), 'WrongInput', 'Should be WrongInput')
        self.assertEqual(classifyTriangle('a',10,'c'), 'WrongInput', 'Should be WrongInput')

        self.assertNotEqual(classifyTriangle(10,10,10),' WrongInput', 'Should be Equilateral')


    def ManageTestSet(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.test_Set1
        self.test_Set2
        self.test_Set3
        self.test_Set4
        

if __name__ == '__main__':
    # examples of running the code
    # runClassifyTriangle(1,2,3)
    # runClassifyTriangle(1,1,1)
   
    #unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    TestTriangles.ManageTestSet
