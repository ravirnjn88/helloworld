from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


db_names = ["A", "B", "C", "D"]
mysql_root = 'mysql://root:ravirnjn88@localhost:3306/'


def create_db(db_names):
    engine = create_engine(mysql_root)
    connection = engine.connect()
    for elem in db_names:
        query = "create database %s" % elem
        connection.execute(query)


def create_table(db_names):
    for elem in db_names:
        sql_url = mysql_root + elem
        engine = create_engine(sql_url)
        metadata = MetaData()
        received_msg = Table('received_msg', metadata,
                             Column('id', Integer, primary_key=True,
                                    autoincrement=True),
                             Column('msgid', String(50)),
                             Column('msgdata', String(200)),)
        metadata.create_all(engine)


def create_mps_db():
    engine = create_engine(mysql_root)
    conn = engine.connect()
    conn.execute("create database mps")

    engine = create_engine(mysql_root + 'mps')
    metadata = MetaData()
    endpoint_rel = Table('endpoint_rel', metadata,
                         Column('id', Integer, primary_key=True,
                                autoincrement=True),
                         Column('from_endpoint', String(100)),
                         Column('to_endpoint', String(100)),)
    msg_dump = Table('msg_dump', metadata,
                     Column('id', Integer, primary_key=True,
                            autoincrement=True),
                     Column('msgid', String(50), primary_key=True),
                     Column('msgdata', String(200)),
                     Column('senders_endpoint', String(200)),)
    metadata.create_all(engine)

    data = [{"from_endpoint": "a/userdetails", "to_endpoint": "b/userdetails"},
            {"from_endpoint": "a/userdetails", "to_endpoint": "c/userdetails"},
            {"from_endpoint": "a/userdetails", "to_endpoint": "d/userdetails"},
            {"from_endpoint": "b/userdetails", "to_endpoint": "a/userdetails"},
            {"from_endpoint": "c/userdetails", "to_endpoint": "b/userdetails"},
            {"from_endpoint": "c/userdetails", "to_endpoint": "a/userdetails"}]
    conn = engine.connect()
    conn.execute(endpoint_rel.insert(), data)


create_db(db_names)
create_mps_db()
create_table(db_names)
