# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 9:59
# @Author  : msy
# @File    : simple_edit.cgi.py
# @Software: PyCharm

import cgi
form=cgi.FieldStorage()
text=form.getavalue('text',open('simple_edit.dat').read())
f=open('simple_edit.dat','w')
f.write(text)
f.close()
print """ Content-type:text/html

<html>
 <head>
  title> A Simple Edit</title>
 </head>
 <body>
  <form action 'simple_deit.cgi' method='POST'>
  <textarea rows='10', cols='20' name='text'>%s</textarea><br/>
  <innput type='Submit'/>
  </form>
 </body>
</html>
""" %text