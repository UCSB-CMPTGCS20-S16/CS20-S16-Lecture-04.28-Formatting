import unittest

class TestCircleFunctions(unittest.TestCase):

    def test_areaCircle_1(self):
        self.assertAlmostEqual(areaCircle(1.0),3.1415926535)

    def test_circumfernceCircle_1(self):
        self.assertAlmostEqual(circumferenceCircle(1.0),6.2831853) 

    def test_areaCircle_3(self):
        self.assertAlmostEqual(areaCircle(3.0),28.2743338)

    def test_circumfernceCircle_3(self):
        self.assertAlmostEqual(circumferenceCircle(3.0),18.8495559)

if __name__ == "__main__":
    unittest.main()
