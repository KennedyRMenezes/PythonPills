import mysql.connector as con

class Database:

    def create_con(self):
        # Estabelecendo a conexão
        cnx = con.connect(
            user='root',
            password='****',
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

        result = cur.fetchone()

        cnx.commit()

        cur.close()
        cnx.close()

        return True if result else False
