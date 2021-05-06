import os
import cx_Oracle
import yaml

# It's not recommended to push config files to github. This is only for learning purposes.
with open("config.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.BaseLoader)

os.environ['PATH'] = cfg["icpath"]

# Create connection
connection = cx_Oracle.connect(cfg["database"])
cursor = connection.cursor()

sql = "select user from dual"
for i in cursor.execute(sql):
    print(i)

cursor.close()
connection.close()
