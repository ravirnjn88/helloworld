from sqlalchemy.sql import select
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
mysql_root = 'mysql://root:ravirnjn88@localhost:3306/'


# get user details from the database given userid
def get_userdetail(db_name, userid):
    sql_url = mysql_root + db_name
    engine = create_engine(sql_url)
    conn = engine.connect()

    metadata = MetaData()
    users = Table('users', metadata, Column('userid', String(50),
                  primary_key=True), Column('email', String(50)),
                  Column('name', String(50)), Column('address', String(50)),)

    s = select([users]).where(users.c.userid == userid)
    a = conn.execute(s).fetchone()
    result = {"userid": a[0], "email": a[1], "name": a[2], "address": a[3]}
    return result


# update the user details
def update_userdetail(db_name, user_detail):
    sql_url = mysql_root + db_name
    engine = create_engine(sql_url)
    conn = engine.connect()

    metadata = MetaData()
    users = Table('users', metadata, Column('userid', String(50),
                  primary_key=True), Column('email', String(50)),
                  Column('name', String(50)), Column('address', String(50)),)

    s = users.update().where(users.c.userid == user_detail["userid"])\
        .values(email=user_detail["email"], name=user_detail["name"],
                address=user_detail["address"])
    conn.execute(s)


# for services store received msgs
def store_msg(db_name, msg_detail):
    sql_url = mysql_root + db_name
    engine = create_engine(sql_url)
    conn = engine.connect()

    metadata = MetaData()
    received_msg = Table('received_msg', metadata, Column('id', Integer,
                         primary_key=True), Column('msgid', String(50),
                         primary_key=True), Column('msgdata', String(200)),)

    conn.execute(received_msg.insert(), [{"msgid": msg_detail["msgid"],
                                          "msgdata": msg_detail["msgdata"]}])
