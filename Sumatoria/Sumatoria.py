import unittest

from Sumatoria_clase import sumatoria


class TestSumatoria(unittest.TestCase):
    def test_sumatoria_5(self):
        resultado = sumatoria(5)
        self.assertEqual(resultado,15)

    def test_sumatoria_6(self):
        resultado = sumatoria(6)
        self.assertEqual(resultado,21)

    def test_sumatoria_30(self):
        resultado = sumatoria(30)
        self.assertEqual(resultado,465)
    
    def test_sumatoria_61(self):
        resultado = sumatoria(61)
        self.assertEqual(resultado,1891)
    
    def test_sumatoria_100(self):
        resultado = sumatoria(100)
        self.assertEqual(resultado,5050)

    def test_sumatoria_101(self):
        resultado = sumatoria(101)
        self.assertEqual(resultado,5151)

    def test_sumatoria_109(self):
        resultado = sumatoria(109)
        self.assertEqual(resultado,5995)
    
    def test_sumatoria_313(self):
        resultado = sumatoria(313)
        self.assertEqual(resultado,49141)

    def test_sumatoria_465(self):
        resultado = sumatoria(465)
        self.assertEqual(resultado,108345)

    def test_sumatoria_523(self):
        resultado = sumatoria(523)
        self.assertEqual(resultado,137026)
    
    def test_sumatoria_632(self):
        resultado = sumatoria(632)
        self.assertEqual(resultado,200028)
    
    def test_sumatoria_754(self):
        resultado = sumatoria(754)
        self.assertEqual(resultado,284635)
    
    def test_sumatoria_888(self):
        resultado = sumatoria(888)
        self.assertEqual(resultado,394716)
    
    def test_sumatoria_937(self):
        resultado = sumatoria(937)
        self.assertEqual(resultado,439453)
    
    def test_sumatoria_997(self):
        resultado = sumatoria(997)
        self.assertEqual(resultado,497503)
    


    
    


if __name__ == '__main__':
    unittest.main()