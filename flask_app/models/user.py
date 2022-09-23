from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.mail = data['mail']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_by_id(cls, id):
        query = f'SELECT * FROM usuarios where id = {id};'
        results = connectToMySQL('users_schema').query_db(query)
        if len(results)>0:
            return cls(results[0])
        else:
            return None

    @classmethod
    def get_last(val):
        query = 'SELECT MAX(id) as id FROM usuarios;'
        results = connectToMySQL('users_schema').query_db(query)
        val=results[0]['id']
        if results:
            return (val) 
        else:
            return None
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre , apellido , mail , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(mail)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def update(cls, data ):
        query = "UPDATE usuarios SET nombre=%(nombre)s , apellido=%(apellido)s , mail= %(mail)s, updated_at=NOW() where id =%(id)s"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, id ):
        query = "DELETE from usuarios WHERE id = %(id)s;"
        data={
            'id':id
        }
        return connectToMySQL('users_schema').query_db( query, data )

    