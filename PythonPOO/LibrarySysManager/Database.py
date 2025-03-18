import mysql.connector as con

class Database:

    def create_con(self):
        # Estabelecendo a conexão
        cnx = con.connect(
            user='root',
            password='21535030',
            database='Libraries',
            host='localhost'
        )
        mycursor = cnx.cursor()
        return mycursor, cnx

    def consultaBiblioteca(self, id):

        cur, cnx = self.create_con()

        query = f"SELECT lib_name FROM Library WHERE lib_id = {id}"

        cur.execute(query)

        result = cur.fetchone()

        cnx.commit()

        cur.close()
        cnx.close()

        return True if result else None
    
    def cadastraLivro(self, lib_id, name, author, pages, num):

        cur, cnx = self.create_con()

        query = "INSERT INTO Book (lib_id, book_name, book_author, book_pages, book_qtd) VALUES (%s, %s, %s, %s, %s)"

        cur.execute(query, (lib_id, name, author, pages, num))

        cnx.commit()

        cur.close()
        cnx.close()

