#!/usr/bin/python
# This programme calculates the sum of  all emmail address
#in the file given below and store them in the database

import sqlite3

conn=sqlite3.connect('emailDB.sqlite')
cur=conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS counts ''')
cur.execute('''
CREATE TABLE counts(org TEXT,count INTEGER)''')
fname=raw_input("Please Enter the file name:")

if len(fname)<1:fname="mbox.txt"
fh=open(fname)

for line in fh:

	if not line.startswith('From: '):continue
	newline=line.split()
	ems=newline[1].split('@')
	org=ems[1]
	cur.execute('SELECT count FROM counts WHERE org=?',(org,))
	row=cur.fetchone()
	if row is None:
		cur.execute('INSERT INTO counts(org,count) VALUES(?,1)', (org,))

	else:
		cur.execute('UPDATE counts SET count= count + 1 WHERE org=?',(org,))

	conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC '
for row in cur.execute(sqlstr):
	  print str(row[0]), row[1]
cur.close()


