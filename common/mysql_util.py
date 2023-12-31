import pymysql

class Mysql:

  def __init__(self):
    self.conn = pymysql.connect(
      host = '192.168.1.102', # port is default 3306
      user = 'kevin',
      password = '123456',
      database = 'mydbs')

  def create_table(self):
    with self.conn.cursor() as cursor:
      sql = """
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
        );
        """
      cursor.execute(sql)

  def _exists(self, username):
    with self.conn.cursor() as cursor:
      sql = f"SELECT username FROM users WHERE username=%s"
      cursor.execute(sql,(username,))
      result = cursor.fetchone()
      return True if result else False

  def add(self,username,password):
    if not self._exists(username):
      with self.conn.cursor() as cursor:
        sql = f"INSERT INTO users (username,password_hash) VALUES (%s, %s)"
        cursor.execute(sql,(username,password))
      self.conn.commit()
    else:
      print(f'User {username} already exists')

  def delete(self,username):
    if self._exists(username):
      with self.conn.cursor() as cursor:
        sql = f"DELETE FROM users WHERE username=%s"
        cursor.execute(sql,(username,))
      self.conn.commit()
    else:
      print(f'User {username} does not exist')

  def update(self,username,new_password):
    if self._exists(username):
      with self.conn.cursor() as cursor:
        sql = f"UPDATE users SET password_hash=%s WHERE username=%s"
        cursor.execute(sql,(new_password,username))
      self.conn.commit()
    else:
      print(f'User {username} does not exist')

  def get_info(self,username):
    if self._exists(username):
      with self.conn.cursor() as cursor:
        sql = f"SELECT password_hash FROM users WHERE username=%s"
        cursor.execute(sql,(username,)) # 注意username这里是元组
        result = cursor.fetchone() # 返回的是一个元组
        if result:
          return result[0]
        else:
          return None
    else:
      print(f'User {username} does not exist')