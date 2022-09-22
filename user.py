# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.mail = data['mail']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('users_schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for user in results:
            users.append( cls(user) )
        return users
        
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre , apellido , mail , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(mail)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, data ):
        query = "DELETE from usuarios WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_schema').query_db( query, data )

    