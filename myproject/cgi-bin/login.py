#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from db_object import DBworker
database = DBworker()
form = cgi.FieldStorage()
email=cgi.escape(form.getfirst("e-mail","not"))
password = cgi.escape(form.getfirst("password","not"))
print("html")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
	<meta charset="utf-8">
	<title>LOGIN</title>
    <link rel="stylesheet" href="../css/styles.css">	
</head>
<body>""")
if database.UserLogin(email, password)[1]==True:
    print("<p>login as: <b>{}</b></p>".format(email))
    print("<p>HI, <b>{}</b>!</p>".format(database.UserLogin(email, password)[0]))
    print("Now in table USERS {} records<br>".format(database.GetCountUsers()))
    print("id|name|email|pass|info<br>")
    for i in database.WievAllUsers():
        for j in i:
            print("{}".format(j))
        print("<br>")
else:
    print("<div class='stop'><b>LOGIN FAILED<br>ACCESS DENIED</b></div>")
print("""</body></html>""")
