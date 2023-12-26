import pymysql

class Mysql:

  def __init__(self):
    self.conn = pymysql.connect(
      host = '127.0.0.1', # port is default 3306
      user = 'kevin',
      password = '123456',
      database = 'mydbs')

  def create_table(self):
    with self.conn.cursor as cursor:
      sql = """
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
        );
        """
      cursor.execute(sql)

  def add(self):
    pass
  def delete(self):
    pass
  def update(self):
    pass
  def query(self):
    pass
