#! C:\Users\91906\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html\r\n\r\n")
import cgi

import json
import mysql.connector
con=mysql.connector.connect(host='localhost', user='shoes', passwd='shoes',database='shoes')
x=con.cursor()
f=cgi.FieldStorage()
try:
    cond=f.getvalue('cond')
    if cond == 'enquiry_entry':
        name=f.getvalue('name')
        cont_no=f.getvalue('cont_no')
        email=f.getvalue('email')
        message=f.getvalue('message')
        query="insert into enquiry (sname,cont_no,email,message) values(%s,%s,%s,%s)"
        x.execute(query,(name,cont_no,email,message))
        con.commit()
        print("Enquiry Successfully Entered!!")
    elif cond== 'login':
        username = form.getvalue('username')
        password = form.getvalue('password')
    users = {
            "correctUsername": "correctPassword"
        }

        if cond == 'login':
            if username in users and users[username] == password:
                print(json.dumps(1))  # Login success
            else:
                print(json.dumps(0))  # Invalid username or password
        else:
            print(json.dumps(-1))  # Invalid request
        query='select * from login where username=%s and password=%s'
        x.execute(query,(username,password))
        data=x.fetchall()
        if len(data)==0:
            print(0)
        else:
            print(1)
    elif cond=='address':
        name=f.getvalue('name')
        mobile_no=f.getvalue('mobile_no')
        address=f.getvalue('address')
        pincode=f.getvalue('pincode')
        email=f.getvalue('email')
        itemid=f.getvalue('itemid')
        query='insert into order_details(name,mobile_no,address,pincode,email,itemid) values(%s,%s,%s,%s,%s,%s)'
        x.execute(query,(name,mobile_no,address,pincode,email,itemid))
        con.commit()
        print(1)
    elif cond=='record':
        x.execute('select * from order_details')
        data=x.fetchall()
        if len(data)==0:
            print('<tr><td colspan="7" style="color:red;background-color:pink;">There is no record in order yet!!</td></tr>')
        else:
            num=0
            for i in data:
                num+=1
                print('<tr><td>'+str(num)+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+i[3]+'</td><td>'+i[4]+'</td><td>'+i[5]+'</td><td>'+i[6]+'</td></tr>')
        print('&&1')
except Exception as e:
    print("Unsuccesss",e)
finally:
    if con.is_connected:
        con.close()
        x.close()