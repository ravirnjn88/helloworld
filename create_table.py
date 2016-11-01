from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


users_data = [{"userid":"ravirnjn88" ,"email":"ravirnjn88@gmail.com" ,"name":"Ravi Ranjan" ,"address":"Koramangala, Bangalore" }, {"userid":"ab1993" ,"email":"ankitbansal0802@gmail.com" ,"name":"Ankit Bansal" ,"address":"Venkatpura Main Road Bangalore" }, {"userid":"ravi.ranjan" ,"email":"raviranjan@practo.com" ,"name":"Ranjan Ravi" ,"address":"First Block Koramangala, Bangalore" }, {"userid":"venky" ,"email":"vshukla@gmail.com" ,"name":"Venkatesh Shukla" ,"address":" Marathali, Bangalore" }, {"userid":"sitesh" ,"email":"siteshjaiswal@gmail.com" ,"name":"Sitesh Ranjan" ,"address":"Hyderabad" }]

db_names = ["A","B","C","D"]
mysql_root = 'mysql://root:ravirnjn88@localhost:3306/'

def create_db(db_names):
	engine = create_engine(mysql_root)
	connection = engine.connect()
	for elem in db_names:
		query = "create database %s" % elem
		connection.execute(query)

def create_table(db_names,users_data):
	for elem in db_names:
		#create engine url
		sql_url = mysql_root + elem
		engine = create_engine(sql_url)

		#create table
		metadata = MetaData()
		users = Table('users', metadata, Column('userid', String(50), primary_key=True), Column('email', String(50)), Column('name', String(50)),Column('address', String(50)),)
		received_msg = Table('received_msg', metadata, Column('id', Integer, primary_key=True, autoincrement=True) , Column('msgid', String(50)), Column('msgdata', String(200)),)
		metadata.create_all(engine)

		#insert data into tables
		conn = engine.connect()
		conn.execute(users.insert(),users_data)

def create_mps_db():
	engine = create_engine(mysql_root)
	conn = engine.connect()
	conn.execute("create database mps")

	engine = create_engine(mysql_root + 'mps')
	metadata = MetaData()
	endpoint_rel = Table('endpoint_rel', metadata, Column('id', Integer, primary_key=True, autoincrement=True), Column('from_endpoint', String(100)), Column('to_endpoint', String(100)),)
	msg_dump = Table('msg_dump', metadata, Column('id', Integer, primary_key=True, autoincrement=True) , Column('msgid', String(50), primary_key=True), Column('msgdata', String(200)), Column('senders_endpoint', String(200)),)
	metadata.create_all(engine)

	data = [{"from_endpoint":"a/userdetails","to_endpoint":"b/userdetails"},{"from_endpoint":"a/userdetails","to_endpoint":"c/userdetails"}, {"from_endpoint":"a/userdetails","to_endpoint":"d/userdetails"}]
	conn = engine.connect()
	conn.execute(endpoint_rel.insert(),data)


create_db(db_names)
create_mps_db()
create_table(db_names,users_data)



