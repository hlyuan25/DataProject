import mysql.connector


class Database(object):
    @classmethod
    def create_connection(cls):
        connection = mysql.connector.connect(user='root', password='admin', database='BookDB', charset='utf8')
        return connection

    @classmethod
    def query(cls):
        sql = "select * from book where price < 70 and date(date) >= '2017-01-01';"
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        cursor.close()
        conn.close
        return result_set


if __name__ == "__main__":
    books = Database.query()
    for book in books:
        date = str(book[3])
        print('图书:%s, 价格:%s, 出版日期:%s' % (book[1], book[2], date[0:11]))
