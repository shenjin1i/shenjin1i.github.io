import cgi,pymysql

print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()

input = {}

for key in fs:
    input[key] = fs[key].value

# print(input["id"])

sql = "delete from user where id={id}".format(id=input["id"])
# print(sql)

db =pymysql.connect("192.168.0.171", "sjl", "123456", "myserver")
cursor = db.cursor()

# print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("<script>alert('删除成功');location.href='list.py'</script>")
except:
    db.rollback()
    print("<script>alert('删除失败!');</script>")

cursor.close()
db.close()