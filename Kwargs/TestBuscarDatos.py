import unittest

from BuscarDatos import buscar_datos

class TestBuscarDatos(unittest.TestCase):
    
    def setUp(self):
        self.database = {
            1:{
                "nombre1": "Emanuel",

               "apellido1":"Perez",

                "apellido2":"Gianolini" },
            
            2: {"nombre1":"Chandler",
                
                "nombre2":"Muriel",

                "apellido1":"Bing"},
            
            3: {"nombre1":"Rachel",
                
                "apellido1":"Grenn"},
            
            4:{"nombre1":"Regina",
               
                "apellido1":"Phalange"}

        }

    def test_persona_existente(self):
        resultado = buscar_datos("Emanuel","Perez","Gianolini",database=self.database)
        self.assertEqual(resultado,1)
    
    def test_persona_no_existente(self):
        resultado = buscar_datos("Pablo",database=self.database)
        self.assertEqual(resultado,None)

if __name__ == '__main__':
    unittest.main()