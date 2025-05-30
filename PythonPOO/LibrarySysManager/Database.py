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
    
    def make_query(self, query, *args):

        cur, cnx = self.create_con()

        if len(args) == 0:
            cur.execute(query)
        else:
            cur.execute(query, args)

        result = cur.fetchall()

        cnx.commit()

        cur.close()
        cnx.close()

        if result:
            return True, result
        else:
            return False, 0
