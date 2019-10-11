import cgi,pymysql

import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

print("Content-Type: text/html")
print()

fs = cgi.FieldStorage()

input = {}

for key in fs:
    input[key] = fs[key].value


id = input['id']

sql = "select * from user where id={}".format(id)

db =pymysql.connect("192.168.0.171", "sjl", "123456", "myserver")
cursor = db.cursor()
cursor.execute(sql)

content = cursor.fetchone()
# print(content)

ses = ""
if content[4] == 0:
    sex = """性别: <input type="radio" name="sex" value="0" value={id} checked>女<input type="radio" name="sex" value="1">男<br>"""
else:
    sex = """性别: <input type="radio" name="sex" value="0" value={id}>女<input type="radio" name="sex" value="1" checked>男<br>"""

# print(content[0:4],s)

html = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>MyWeb</title>
</head>

<body>
    <form action="update.py" method="post">
        <input type="hidden" name="id" value={id}>
        用户名: <input type="text" name="username" value={name}><br>
        邮箱: <input type="text" name="email" value={email}><br>
        年龄: <input type="text" name="age" value={age}><br>
        {sex}
        <button>添加</button>
    </form>
</body>

</html>
""".format(id=content[0], name=content[1], email=content[2], age=content[3], sex=sex)

print(html)

