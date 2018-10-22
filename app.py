import mysql.connector
import MySQLdb as mdb
from mysql.connector import Error
from mysql.connector import errorcode
import subprocess

connection = mdb.connect(host='localhost',user='me',password='vtac123',database='Routers')
cur = connection.cursor()
#cur.execute("DROP TABLE IF EXISTS RTRS")
#cur.execute("CREATE TABLE RTRS(Id INT PRIMARY KEY AUTO_INCREMENT, hostname VARCHAR(25))")
#cur.execute("ALTER TABLE RTRS ADD USED VARCHAR(25)" )
#with open('ip.txt', 'r+') as f:
#    a = f.readlines()
    #b = ' '.join(a)
#    b = []
 #   for i in a:
  #      b.append(i.strip())
#b = [('10.195.169.140', 'NO'),('10.195.169.141', 'NO'),('10.195.169.142','NO')]
#cur.execute("INSERT INTO RTRS(IP,USED) VALUES (%s,'NO') % b")
#cur.execute("INSERT INTO RTRS(USED) VALUES ('Yes')")
#query_string = 'INSERT INTO RTRS(IP) VALUES (%s);' % b
#cur.execute(query_string, a)
#for j in b:
#    cur.execute("INSERT INTO RTRS(IP) VALUES (%s)" % b)
#    connection.commit()
#stmt = "INSERT INTO RTRS (IP, USED) VALUES (%s, %s)"
#cur.executemany(stmt,b)
#stmt = "UPDATE RTRS SET USED = @USED := 'Yes' WHERE USED='NO'limit 1"
#cur.execute(stmt)
stmt1 = "SElECT * FROM RTRS WHERE USED='NO' limit 1"
cur.execute(stmt1)
a = cur.fetchall()
for i in a:
    print i[2]
    p = subprocess.Popen('ping' + ' ' + i[2] + '-c 2', stdout=subprocess.PIPE)
    output = p1.communicate()[0]
    if 'unreachable' not in output:
        print 'dont use this IP'
connection.commit()
#print a


















































































