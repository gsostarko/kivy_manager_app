import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()

c.execute("""CREATE TABLE if not exists users(
	username text,
	password text,
	first_name text,
	last_name text,
	ev_br integer,
	email text,
	is_admin integer

)""")

c.execute("INSERT INTO users VALUES ('gsostarko','3107','Goran','Šostarko','5907','goran.sostarko@hep.hr','1')")

conn.commit()

conn.close()