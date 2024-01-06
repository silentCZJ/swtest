import pymysql

class Mysql:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        """enter和exit用来实现with上下文管理"""
        self._conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
          )
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, *exc_info):
        self._conn.commit()
        self._cursor.close()
        self._conn.close()

    def create_table(self):
      sql = """
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL
        );
        """
      self.cursor.execute(sql)

    def _exists(self, username):
      sql = f"SELECT username FROM users WHERE username=%s"
      self.cursor.execute(sql, (username,))
      result = self.cursor.fetchone()
      return True if result else False

    def add(self, username, password):
        if not self._exists(username):
          sql = f"INSERT INTO users (username,password_hash) VALUES (%s, %s)"
          self.cursor.execute(sql, (username, password))
        else:
            print(f"User {username} already exists")

    def delete(self, username):
        if self._exists(username):
          sql = f"DELETE FROM users WHERE username=%s"
          self.cursor.execute(sql, (username,))
        else:
            print(f"User {username} does not exist")

    def update(self, username, new_password):
        if self._exists(username):
          sql = f"UPDATE users SET password_hash=%s WHERE username=%s"
          self.cursor.execute(sql, (new_password, username))
        else:
            print(f"User {username} does not exist")

    def get_info(self, username):
        if self._exists(username):
          sql = f"SELECT password_hash FROM users WHERE username=%s"
          self.cursor.execute(sql, (username,))  # 注意username这里是元组
          result = self.cursor.fetchone()  # 返回的是一个元组
          if result:
            return result[0]
          else:
            return None
        else:
            print(f"User {username} does not exist")

    @property
    def cursor(self):
        return self._cursor


if __name__ == '__main__':
  import yaml
  file_path = "../data/mysql_config.yaml"
  with open(file_path, "r", encoding="utf-8") as f:
      config = yaml.load(f, yaml.FullLoader)

      print(type(config['host']))
      print(type(config['password']))
      with Mysql(
          config["host"],
          config["port"],
          config["user"],
          config["password"],
          config["database"],
      ) as mysql:
          res = mysql.get_info("kevin")