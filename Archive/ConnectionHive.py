import jaydebeapi

database='default'
driver='com.amazon.hive.odbc.HS2Driver'
server='ec2-3-235-44-213.compute-1.amazonaws.com'

port=10000

# JDBC connection string
url=("jdbc:hive2://" + server + ":" + str(port)
+ "/"+ database + ";")

#Connect to HiveServer2
conn=jaydebeapi.connect("com.amazon.hive.odbc.HS2Driver", url)
cursor = conn.cursor()

# Execute SQL query
sql="select * from temp_covid limit 10"
cursor.execute(sql)
results = cursor.fetchall()
print (results)