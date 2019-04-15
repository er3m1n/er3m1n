#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from db_object import DBworker
database = DBworker()
form = cgi.FieldStorage()
username = form.getfirst("username","none")
username=cgi.escape(username)
email = form.getfirst("email","none")
email = cgi.escape(email)
password = form.getfirst("password","none")
password= cgi.escape(password)
password1 = form.getfirst("password","none")
password1= cgi.escape(password1)
if password1!=password:
    passwarn=True
else:
    passwarn=False
info = form.getfirst("info","none")
info = cgi.escape(info)
data=[username, email, password, info]
if database.UserExist(username)==True or passwarn==True :
    validate="<H1>REGISTRATION FAILED!</H1><p>user already register or pass not equal</p>"
    pass
else:
    database.AddUser(username, email, password, info)
    validate="<H1>REGISTRATION SUCCESS!</H1>"
print("html")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
	<meta charset="utf-8">
	<title>REGISTRATION</title>	
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>""")
print(validate)
for i in data:
    print("<p><b>{}</b></p>".format(i))
#print("<p>{}</p>".format(database.WievAllUsers()), sep="\n")

print("<p><H1>{}</H1></p>".format(database.GetCountUsers()))
#for q in database.WievAllUsers():
#    print("<b>{}</b>".format(q))
database.Close()
