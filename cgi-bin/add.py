import cgi,pymysql

print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()
data = {}

for key in fs:
    data[key]=fs[key].value

db =pymysql.connect("192.168.0.171", "sjl", "123456", "myserver")
cursor = db.cursor()

sql = "insert into user value(0,'{name}','{email}',{age},{sex})".format(name=data["username"], email=data["email"], age=data["age"], sex=data["sex"])
# print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("<script>alert('添加成功');</script>")
except:
    db.rollback()
    print("<script>alert('添加失败!');location.href='/index.html'</script>")

cursor.close()
db.close()