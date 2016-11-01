from sqlalchemy.sql import select
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
mysql_root = 'mysql://root:ravirnjn88@localhost:3306/'

#mps msg_dump
def msg_dump(msgid,msgdata,senders_endpoint):
	sql_url = mysql_root + 'mps'
	engine = create_engine(sql_url)
	conn = engine.connect()

	metadata = MetaData()
	msg_dump = Table('msg_dump', metadata, Column('id', Integer, primary_key=True, autoincrement=True) , Column('msgid', String(50), primary_key=True), Column('msgdata', String(200)), Column('senders_endpoint', String(200)))

	conn.execute(msg_dump.insert(),[{"msgid":msgid,"msgdata":msgdata, "senders_endpoint":senders_endpoint}])

#get list of endpoint of services to ping
def get_endpoint(senders_endpoint):
	sql_url = mysql_root + 'mps'
	engine = create_engine(sql_url)
	conn = engine.connect()

	metadata = MetaData()
	endpoint_rel = Table('endpoint_rel', metadata, Column('id', Integer, primary_key=True, autoincrement=True), Column('from_endpoint', String(100)), Column('to_endpoint', String(100)),)

	s = select([endpoint_rel]).where(endpoint_rel.c.from_endpoint == senders_endpoint)
	d = []
	a = conn.execute(s).fetchall()
	for elem in a:
		d.append(elem[2])
	print d
	return d



#print get_userdetail("A","ravirnjn88")
#update_userdetail("A",{"userid":"ravirnjn88" ,"email":"ravirnjn88@gmail.com" ,"name":"Ravi Ranjan" ,"address":"Koramangala, Bangalore"})
#print get_userdetail("A","ravirnjn88")
#msg_dump("1234","hello","a")
#get_endpoint("a/userdetails")
	