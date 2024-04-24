def buscar_datos(*args, **kwargs):
    for key, value in database.items():
        persona_coincide = True
        for arg in args:
            if arg not in value.values():
                persona_coincide = False
                break
        if persona_coincide:
            return key
    return None

database = {
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
