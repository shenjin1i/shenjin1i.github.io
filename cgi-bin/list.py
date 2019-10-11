#!usr/bin/env python3
#!_*_ conding:utf-8 _*_
#!@Author: God1i
#!@Time:2019-07-31 下午 12:10



import cgi,pymysql
#
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

print("Content-Type: text/html")
print()

db =pymysql.connect("192.168.0.171", "sjl", "123456", "myserver")
cursor = db.cursor()

sql = "select * from user"
cursor.execute(sql)
res = cursor.fetchall()

html = ""

for text in res:
    #print(text, "<br>")
    s = ""
    if text[4] == 0:
        s = "女"
    else:
        s = "男"
    html += """
        <tr>
            <td>{id}</td>
            <td>{name}</td>
            <td>{email}</td>
            <td>{age}</td>
            <td>{sex}</td>
            <td>
                <a href = "/cgi-bin/delete.py?id={id}">删除</a>
                <a href = "/cgi-bin/edit.py?id={id}">修改</a>
            </td>
        </tr>
        """.format(id = text[0], name = text[1], email = text[2], age = text[3], sex = s)

indexHtml1 = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Demo</title>
    <style type="text/css">
    	*{
				margin: 0;
				padding: 0;
				list-style: none;
			}
		table{
			width: 500px;
			height: 500px;
			margin: 0 auto;
			margin-top: 20px;
			background-color: yellowgreen;
			text-align: center;
			line-height: 25px;
			font-family: "微软雅黑";
		}
		.tou{
			
		}
    </style>
</head>
<body>
    <table><tr class="tou">
        	<th>ID</th>
        	<th>用户名</th>
        	<th>邮箱</th>
        	<th>年龄</th>
        	<th>年龄</th>
            <th>功能</th>
        </tr>
        """

indexHtml2 = """
    </table>
</body>
</html>
"""

print(indexHtml1, html ,indexHtml2)