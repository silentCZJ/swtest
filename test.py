import yaml
import sys
from common.mysql_util import Mysql

file_path = "./data/mysql_config.yaml"
with open(file_path, "r", encoding="utf-8") as f:
    config = yaml.load(f, yaml.FullLoader)

    with Mysql(
        config["host"],
        config["port"],
        config["user"],
        config["password"],
        config["database"],
    ) as mysql:
        res = mysql.get_info(sys.argv[1])
        print(res)
