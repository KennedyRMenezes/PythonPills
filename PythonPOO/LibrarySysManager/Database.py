import mysql.connector as con

class Database:

    def create_con(self):
        # Estabelecendo a conexão
        cnx = con.connect(
            user='root',
            password='***',
            database='Libraries',
            host='localhost'
        )
        mycursor = cnx.cursor()
        return mycursor, cnx
