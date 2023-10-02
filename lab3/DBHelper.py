import psycopg2
import psycopg2.extras

class DBHelper:

    def __init__(self):
        self.host = "localhost"
        self.port = "5432"
        self.user = "postgres"
        self.password = "postgres"
        self.db = "CPE231"

    def __connect__(self):
        self.con = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, dbname=self.db)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        columns = []
        for desc in self.cur.description:
            columns.append(desc.name)
        columns = tuple(columns)
        self.__disconnect__()
        return data, columns

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.con.commit()
        self.__disconnect__()