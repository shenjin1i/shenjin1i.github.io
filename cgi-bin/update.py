import cgi,pymysql

print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()
data = {}

for key in fs:
    data[key]=fs[key].value

sql = "update user set username='{name}',email='{email}',age={age},sex={sex} where id={id}".format(id=data["id"],name=data["username"], email=data["email"], age=data["age"], sex=data["sex"])
"""
利用print()打印查找bug位置，
1，打印输出sql语句找bug
2，把打印得到的sql语句放到Navicat中找bug

SQL语句不能打印输出：
format出现bug，看参数是否一一对应
"""

db =pymysql.connect("192.168.0.171", "sjl", "123456", "myserver")
cursor = db.cursor()

# print(sql)
try:
    cursor.execute(sql)
    db.commit()
    print("<script>alert('修改成功');</script>")
except:
    db.rollback()
    print("<script>alert('修改失败!');</script>")

cursor.close()
db.close()